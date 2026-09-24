/* Cahier Psyclopédia — format plus riche qu'un .docx, import et export.
   Pur : testable sans navigateur. Le son des notes orales reste dans le JSON. */
(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  root.PsyCahierFormat = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  var STOP = {
    psychologie: 1, psycho: 1, humain: 1, humaine: 1, humains: 1,
    cours: 1, texte: 1, notes: 1, note: 1, page: 1, avec: 1, dans: 1,
    pour: 1, cette: 1, cette: 1, etre: 1, sont: 1, une: 1, des: 1,
    les: 1, que: 1, qui: 1, pas: 1, plus: 1, tout: 1, comme: 1,
    faire: 1, fait: 1, peut: 1, leur: 1, entre: 1, aussi: 1, mais: 1
  };

  function utf8Encode(text) {
    return new TextEncoder().encode(String(text));
  }

  function utf8Decode(bytes) {
    return new TextDecoder("utf-8").decode(bytes);
  }

  function concat(parts) {
    var n = 0;
    var i;
    for (i = 0; i < parts.length; i++) n += parts[i].length;
    var out = new Uint8Array(n);
    var o = 0;
    for (i = 0; i < parts.length; i++) {
      out.set(parts[i], o);
      o += parts[i].length;
    }
    return out;
  }

  function u16(n) {
    return new Uint8Array([n & 255, (n >> 8) & 255]);
  }

  function u32(n) {
    return new Uint8Array([n & 255, (n >> 8) & 255, (n >> 16) & 255, (n >> 24) & 255]);
  }

  function readU16(b, o) {
    return b[o] | (b[o + 1] << 8);
  }

  function readU32(b, o) {
    return (b[o] | (b[o + 1] << 8) | (b[o + 2] << 16) | (b[o + 3] << 24)) >>> 0;
  }

  var CRC_TABLE = null;
  function crc32(bytes) {
    if (!CRC_TABLE) {
      CRC_TABLE = new Uint32Array(256);
      var n;
      var k;
      for (n = 0; n < 256; n++) {
        var c = n;
        for (k = 0; k < 8; k++) c = (c & 1) ? (0xedb88320 ^ (c >>> 1)) : (c >>> 1);
        CRC_TABLE[n] = c >>> 0;
      }
    }
    var crc = 0xffffffff;
    for (var i = 0; i < bytes.length; i++) {
      crc = CRC_TABLE[(crc ^ bytes[i]) & 0xff] ^ (crc >>> 8);
    }
    return (crc ^ 0xffffffff) >>> 0;
  }

  function zipStore(files) {
    var locals = [];
    var centrals = [];
    var offset = 0;
    var i;
    for (i = 0; i < files.length; i++) {
      var name = utf8Encode(files[i].name);
      var raw = files[i].data;
      var stored = files[i].stored || raw;
      var method = files[i].method || 0;
      var crc = crc32(raw);
      var local = concat([
        u32(0x04034b50), u16(20), u16(0x800), u16(method),
        u16(0), u16(0), u32(crc), u32(stored.length), u32(raw.length),
        u16(name.length), u16(0), name, stored
      ]);
      var central = concat([
        u32(0x02014b50), u16(20), u16(20), u16(0x800), u16(method),
        u16(0), u16(0), u32(crc), u32(stored.length), u32(raw.length),
        u16(name.length), u16(0), u16(0), u16(0), u16(0), u32(0),
        u32(offset), name
      ]);
      locals.push(local);
      centrals.push(central);
      offset += local.length;
    }
    var centralDir = concat(centrals);
    var eocd = concat([
      u32(0x06054b50), u16(0), u16(0), u16(files.length), u16(files.length),
      u32(centralDir.length), u32(offset), u16(0)
    ]);
    return concat(locals.concat([centralDir, eocd]));
  }

  function findEocd(bytes) {
    var start = Math.max(0, bytes.length - 22 - 65536);
    for (var i = bytes.length - 22; i >= start; i--) {
      if (bytes[i] === 0x50 && bytes[i + 1] === 0x4b && bytes[i + 2] === 0x05 && bytes[i + 3] === 0x06) {
        return i;
      }
    }
    return -1;
  }

  function unzip(bytes, inflateRaw) {
    var eocd = findEocd(bytes);
    if (eocd < 0) return Promise.reject(new Error("Archive illisible."));
    var count = readU16(bytes, eocd + 10);
    var centralOff = readU32(bytes, eocd + 16);
    var files = {};
    var pos = centralOff;
    var jobs = [];
    var n;
    for (n = 0; n < count; n++) {
      if (readU32(bytes, pos) !== 0x02014b50) break;
      var method = readU16(bytes, pos + 10);
      var compSize = readU32(bytes, pos + 20);
      var nameLen = readU16(bytes, pos + 28);
      var extraLen = readU16(bytes, pos + 30);
      var commentLen = readU16(bytes, pos + 32);
      var localOff = readU32(bytes, pos + 42);
      var name = utf8Decode(bytes.subarray(pos + 46, pos + 46 + nameLen));
      var nameLenLocal = readU16(bytes, localOff + 26);
      var extraLocal = readU16(bytes, localOff + 28);
      var dataOff = localOff + 30 + nameLenLocal + extraLocal;
      var slice = bytes.subarray(dataOff, dataOff + compSize);
      jobs.push({ name: name, method: method, slice: slice });
      pos += 46 + nameLen + extraLen + commentLen;
    }
    var chain = Promise.resolve();
    jobs.forEach(function (job) {
      chain = chain.then(function () {
        if (job.method === 0) {
          files[job.name] = job.slice;
          return null;
        }
        if (job.method === 8 && inflateRaw) {
          return Promise.resolve(inflateRaw(job.slice)).then(function (out) {
            files[job.name] = out instanceof Uint8Array ? out : new Uint8Array(out);
          });
        }
        return null;
      });
    });
    return chain.then(function () { return files; });
  }

  function xmlEscape(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function attr(raw, name) {
    var re = new RegExp(name + "\\s*=\\s*['\"]([^'\"]*)['\"]", "i");
    var m = re.exec(raw || "");
    return m ? m[1] : "";
  }

  function alignOf(raw) {
    var align = attr(raw, "align").toLowerCase();
    if (align === "center" || align === "right") return align;
    if (align === "justify") return "both";
    var style = attr(raw, "style").toLowerCase().replace(/\s+/g, "");
    if (style.indexOf("text-align:center") !== -1) return "center";
    if (style.indexOf("text-align:right") !== -1) return "right";
    if (style.indexOf("text-align:justify") !== -1) return "both";
    return "left";
  }

  function sizeFromFont(raw) {
    var size = attr(raw, "size");
    var map = { "1": 18, "2": 21, "3": 24, "4": 28, "5": 36, "6": 44, "7": 56 };
    return map[size] || 0;
  }

  function sizeFromStyle(raw) {
    var style = attr(raw, "style");
    var m = /font-size:\s*(\d+)px/i.exec(style);
    if (!m) return 0;
    return Math.max(16, Math.min(72, Math.round(Number(m[1]) * 1.5)));
  }

  function parseRuns(html) {
    var runs = [];
    var style = { b: 0, i: 0, u: 0, s: 0, mark: 0, size: 0 };
    var re = /<\/?([a-z0-9:-]+)([^>]*)>|([^<]+)/gi;
    var m;
    while ((m = re.exec(html))) {
      if (m[3]) {
        var text = m[3].replace(/&nbsp;/g, " ").replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"');
        if (text) {
          runs.push({
            text: text, b: style.b > 0, i: style.i > 0, u: style.u > 0,
            s: style.s > 0, mark: style.mark > 0, size: style.size
          });
        }
        continue;
      }
      var tag = m[1].toLowerCase();
      var close = m[0].charAt(1) === "/";
      var self = /\/\s*>$/.test(m[0]);
      if (tag === "br") {
        runs.push({ text: "\n", b: false, i: false, u: false, s: false, mark: false, size: 0 });
        continue;
      }
      if (tag === "voix" || (tag === "span" && /voix-bulle/.test(m[2] || ""))) {
        if (!close) {
          runs.push({
            voix: true,
            id: attr(m[2], "data-voix"),
            sec: attr(m[2], "data-sec")
          });
        }
        continue;
      }
      var bit = 0;
      var key = "";
      if (tag === "strong" || tag === "b") key = "b";
      else if (tag === "em" || tag === "i") key = "i";
      else if (tag === "u") key = "u";
      else if (tag === "s" || tag === "strike" || tag === "del") key = "s";
      else if (tag === "mark") key = "mark";
      if (key) {
        if (close) style[key] = Math.max(0, style[key] - 1);
        else style[key] += 1;
        continue;
      }
      if (tag === "font" || tag === "span") {
        if (close) {
          var prev = style._stack && style._stack.pop();
          style.size = prev || 0;
        } else {
          if (!style._stack) style._stack = [];
          style._stack.push(style.size);
          var sz = tag === "font" ? sizeFromFont(m[2]) : sizeFromStyle(m[2]);
          if (sz) style.size = sz;
        }
      }
      if (self) { /* ignore */ }
    }
    return runs;
  }

  function parseBlocks(html) {
    var src = String(html || "");
    var blocks = [];
    var re = /<(p|h1|h2|h3|blockquote|li)\b([^>]*)>([\s\S]*?)<\/\1>/gi;
    var m;
    while ((m = re.exec(src))) {
      blocks.push({
        tag: m[1].toLowerCase(),
        align: alignOf(m[2]),
        runs: parseRuns(m[3])
      });
    }
    if (!blocks.length) {
      var plain = src.replace(/<[^>]+>/g, "");
      if (plain.trim()) blocks.push({ tag: "p", align: "left", runs: [{ text: plain, b: false, i: false, u: false, s: false, mark: false, size: 0 }] });
    }
    return blocks;
  }

  function headingSize(tag) {
    if (tag === "h1") return 44;
    if (tag === "h2") return 32;
    if (tag === "h3") return 28;
    return 0;
  }

  function runXml(run, audios) {
    if (run.voix) {
      var meta = (audios && audios[run.id]) || {};
      var sec = meta.duration || Number(run.sec) || 0;
      var label = "note orale " + formatSec(sec);
      var transcript = (meta.transcript || "").trim();
      var text = " [" + label + (transcript ? " : " + transcript : "") + "] ";
      return "<w:r><w:rPr><w:i/><w:color w:val=\"1F6B4C\"/></w:rPr><w:t xml:space=\"preserve\">" + xmlEscape(text) + "</w:t></w:r>";
    }
    if (!run.text) return "";
    var pr = "";
    var size = run.size || 0;
    if (run.b) pr += "<w:b/>";
    if (run.i) pr += "<w:i/>";
    if (run.u) pr += "<w:u w:val=\"single\"/>";
    if (run.s) pr += "<w:strike/>";
    if (run.mark) pr += "<w:highlight w:val=\"yellow\"/>";
    if (size) pr += "<w:sz w:val=\"" + size + "\"/><w:szCs w:val=\"" + size + "\"/>";
    var open = pr ? "<w:rPr>" + pr + "</w:rPr>" : "";
    return "<w:r>" + open + "<w:t xml:space=\"preserve\">" + xmlEscape(run.text) + "</w:t></w:r>";
  }

  function blocksToXml(blocks, audios) {
    return blocks.map(function (block) {
      var size = headingSize(block.tag);
      var runs = block.runs.map(function (run) {
        var copy = {
          text: run.text, voix: run.voix, id: run.id, sec: run.sec,
          b: run.b || block.tag === "h1" || block.tag === "h2",
          i: run.i || block.tag === "blockquote",
          u: run.u, s: run.s, mark: run.mark,
          size: run.size || size
        };
        return runXml(copy, audios);
      }).join("");
      if (!runs) runs = "<w:r><w:t></w:t></w:r>";
      var align = block.align && block.align !== "left"
        ? "<w:jc w:val=\"" + block.align + "\"/>" : "";
      return "<w:p><w:pPr>" + align + "<w:spacing w:after=\"160\"/></w:pPr>" + runs + "</w:p>";
    }).join("");
  }

  function documentXml(title, html, audios) {
    var blocks = [];
    if (title) {
      blocks.push({
        tag: "h1", align: "left",
        runs: [{ text: title, b: true, i: false, u: false, s: false, mark: false, size: 44 }]
      });
    }
    blocks = blocks.concat(parseBlocks(html));
    if (!blocks.length) {
      blocks.push({ tag: "p", align: "left", runs: [{ text: "", b: false, i: false, u: false, s: false, mark: false, size: 0 }] });
    }
    var body = blocksToXml(blocks, audios);
    return "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>" +
      "<w:document xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\">" +
      "<w:body>" + body +
      "<w:sectPr><w:pgSz w:w=\"11906\" w:h=\"16838\"/>" +
      "<w:pgMar w:top=\"1134\" w:right=\"1134\" w:bottom=\"1134\" w:left=\"1134\"/></w:sectPr>" +
      "</w:body></w:document>";
  }

  function docxParts(title, html, audios) {
    return [
      {
        name: "[Content_Types].xml",
        data: utf8Encode("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>" +
          "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">" +
          "<Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>" +
          "<Default Extension=\"xml\" ContentType=\"application/xml\"/>" +
          "<Override PartName=\"/word/document.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml\"/>" +
          "<Override PartName=\"/docProps/core.xml\" ContentType=\"application/vnd.openxmlformats-package.core-properties+xml\"/>" +
          "</Types>")
      },
      {
        name: "_rels/.rels",
        data: utf8Encode("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>" +
          "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">" +
          "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" Target=\"word/document.xml\"/>" +
          "<Relationship Id=\"rId2\" Type=\"http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties\" Target=\"docProps/core.xml\"/>" +
          "</Relationships>")
      },
      {
        name: "word/_rels/document.xml.rels",
        data: utf8Encode("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>" +
          "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\"></Relationships>")
      },
      {
        name: "docProps/core.xml",
        data: utf8Encode("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>" +
          "<cp:coreProperties xmlns:cp=\"http://schemas.openxmlformats.org/package/2006/metadata/core-properties\" " +
          "xmlns:dc=\"http://purl.org/dc/elements/1.1/\">" +
          "<dc:title>" + xmlEscape(title || "Cahier") + "</dc:title>" +
          "<dc:creator>Psyclopédia</dc:creator></cp:coreProperties>")
      },
      { name: "word/document.xml", data: utf8Encode(documentXml(title, html, audios)) }
    ];
  }

  function buildDocx(title, html, audios, deflateSync) {
    var files = docxParts(title, html, audios);
    if (deflateSync) {
      files.forEach(function (file) {
        file.stored = deflateSync(file.data);
        file.method = 8;
      });
    }
    return zipStore(files);
  }

  function docxToHtml(bytes, inflateRaw) {
    return unzip(bytes, inflateRaw).then(function (files) {
      var xmlBytes = files["word/document.xml"];
      if (!xmlBytes) throw new Error("Ce fichier n'est pas un document Word.");
      return xmlToHtml(utf8Decode(xmlBytes));
    });
  }

  function xmlToHtml(xml) {
    var parts = xml.split(/<w:p[ >]/);
    var html = [];
    for (var i = 1; i < parts.length; i++) {
      var chunk = parts[i];
      var end = chunk.indexOf("</w:p>");
      if (end < 0) continue;
      var para = chunk.slice(0, end);
      var align = "";
      var jc = /<w:jc w:val="([^"]+)"/.exec(para);
      if (jc && jc[1] && jc[1] !== "left") {
        var css = jc[1] === "both" ? "justify" : jc[1];
        align = ' style="text-align:' + css + '"';
      }
      var runs = para.split(/<w:r[ >]/);
      var inner = "";
      for (var r = 1; r < runs.length; r++) {
        var run = runs[r];
        var texts = [];
        var tm;
        var tre = /<w:t[^>]*>([\s\S]*?)<\/w:t>/g;
        while ((tm = tre.exec(run))) texts.push(tm[1]);
        if (!texts.length) continue;
        var text = texts.join("").replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"');
        var piece = escapeText(text);
        if (/<w:b\/>/.test(run) || /<w:b /.test(run) && !/w:val="(?:0|false)"/.test(run)) piece = "<strong>" + piece + "</strong>";
        if (/<w:i\/>/.test(run) || /<w:i /.test(run)) piece = "<em>" + piece + "</em>";
        if (/<w:u /.test(run)) piece = "<u>" + piece + "</u>";
        if (/<w:strike\/>/.test(run)) piece = "<s>" + piece + "</s>";
        var sz = /<w:sz w:val="(\d+)"/.exec(run);
        if (sz) {
          var px = Math.round(Number(sz[1]) / 1.5);
          piece = '<span style="font-size:' + px + 'px">' + piece + "</span>";
        }
        if (/<w:highlight /.test(run)) piece = "<mark>" + piece + "</mark>";
        inner += piece;
      }
      html.push("<p" + align + ">" + (inner || "<br>") + "</p>");
    }
    return html.join("");
  }

  function escapeText(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function formatSec(sec) {
    sec = Math.max(0, Math.round(Number(sec) || 0));
    var m = Math.floor(sec / 60);
    var s = sec % 60;
    return m + ":" + (s < 10 ? "0" : "") + s;
  }

  function fold(text) {
    return String(text || "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/œ/g, "oe")
      .replace(/æ/g, "ae")
      .toLowerCase();
  }

  function editDistance(a, b, max) {
    if (a === b) return 0;
    if (Math.abs(a.length - b.length) > max) return max + 1;
    var prev = new Array(b.length + 1);
    var cur = new Array(b.length + 1);
    var j, i, k;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur[0] = i;
      var best = cur[0];
      for (k = 1; k <= b.length; k++) {
        var cost = a.charCodeAt(i - 1) === b.charCodeAt(k - 1) ? 0 : 1;
        cur[k] = Math.min(cur[k - 1] + 1, prev[k] + 1, prev[k - 1] + cost);
        if (cur[k] < best) best = cur[k];
      }
      if (best > max) return max + 1;
      var tmp = prev;
      prev = cur;
      cur = tmp;
    }
    return prev[b.length];
  }

  function wordDistanceOk(spoken, known) {
    if (!spoken || !known) return false;
    if (spoken === known) return true;
    var len = Math.max(spoken.length, known.length);
    var tol = len >= 8 ? 2 : (len >= 6 ? 1 : 0);
    if (!tol || Math.abs(spoken.length - known.length) > tol) return false;
    return editDistance(spoken, known, tol) <= tol;
  }

  function phraseFuzzy(phrase, parts) {
    var words = phrase.split(" ").filter(function (word) {
      return word.length >= 4 && !STOP[word];
    });
    if (words.length < 2) return false;
    var from = 0;
    var w, p, found;
    for (w = 0; w < words.length; w++) {
      found = -1;
      for (p = from; p < parts.length; p++) {
        if (wordDistanceOk(parts[p], words[w])) { found = p; break; }
      }
      if (found < 0) return false;
      from = found + 1;
    }
    return true;
  }

  function buildLexicon(entries) {
    var phrases = [];
    var wordCount = {};
    var wordEntry = {};
    (entries || []).forEach(function (entry) {
      var title = fold(entry.t || "").replace(/[^a-z0-9]+/g, " ").trim();
      if (title.length >= 4) phrases.push({ phrase: title, entry: entry });
      title.split(" ").forEach(function (word) {
        if (word.length < 5 || STOP[word]) return;
        wordCount[word] = (wordCount[word] || 0) + 1;
        wordEntry[word] = entry;
      });
    });
    var words = {};
    Object.keys(wordCount).forEach(function (word) {
      if (wordCount[word] === 1) words[word] = wordEntry[word];
    });
    phrases.sort(function (a, b) { return b.phrase.length - a.phrase.length; });
    return { phrases: phrases, words: words };
  }

  function matchUtterance(lex, utterance) {
    if (!lex) return null;
    var text = fold(utterance).replace(/[^a-z0-9]+/g, " ").replace(/\s+/g, " ").trim();
    if (!text) return null;
    var padded = " " + text + " ";
    var parts = text.split(" ").filter(Boolean);
    var best = null;
    var bestScore = 0;
    var i;
    for (i = 0; i < lex.phrases.length; i++) {
      var phrase = lex.phrases[i].phrase;
      var score = 0;
      if (padded.indexOf(" " + phrase + " ") !== -1) score = 120 + phrase.length;
      else if (phrase.length >= 12 && text.indexOf(phrase) !== -1) score = 110 + phrase.length;
      else if (phraseFuzzy(phrase, parts)) score = 80 + phrase.length;
      if (score > bestScore) {
        bestScore = score;
        best = lex.phrases[i].entry;
      }
    }
    if (bestScore >= 80) return best;
    for (i = 0; i < parts.length; i++) {
      if (STOP[parts[i]]) continue;
      if (lex.words[parts[i]] && bestScore < 50) {
        bestScore = 50;
        best = lex.words[parts[i]];
      }
    }
    if (bestScore >= 50) return best;
    var keys = Object.keys(lex.words);
    for (i = 0; i < parts.length; i++) {
      if (parts[i].length < 6 || STOP[parts[i]]) continue;
      var k;
      for (k = 0; k < keys.length; k++) {
        if (keys[k].length < 6) continue;
        if (wordDistanceOk(parts[i], keys[k]) && bestScore < 40) {
          bestScore = 40;
          best = lex.words[keys[k]];
        }
      }
    }
    return bestScore >= 40 ? best : null;
  }

  function prepareVoice(samples) {
    var n = samples ? samples.length : 0;
    if (!n) return new Float32Array(0);
    var sum = 0;
    var i;
    for (i = 0; i < n; i++) sum += samples[i];
    var mean = sum / n;
    var out = new Float32Array(n);
    var peak = 0;
    for (i = 0; i < n; i++) {
      var v = samples[i] - mean;
      out[i] = v;
      var a = v < 0 ? -v : v;
      if (a > peak) peak = a;
    }
    if (peak >= 0.05 && peak < 0.55) {
      var gain = 0.82 / peak;
      for (i = 0; i < n; i++) {
        var s = out[i] * gain;
        if (s > 1) s = 1;
        if (s < -1) s = -1;
        out[i] = s;
      }
    }
    return out;
  }

  function resampleLinear(input, fromRate, toRate) {
    if (!input || !input.length) return new Float32Array(0);
    if (!fromRate || !toRate || fromRate === toRate) return input;
    var ratio = fromRate / toRate;
    var n = Math.max(1, Math.round(input.length / ratio));
    var out = new Float32Array(n);
    var last = input.length - 1;
    var i;
    for (i = 0; i < n; i++) {
      var x = i * ratio;
      if (x >= last) { out[i] = input[last]; continue; }
      var i0 = Math.floor(x);
      var t = x - i0;
      out[i] = input[i0] * (1 - t) + input[i0 + 1] * t;
    }
    return out;
  }

  function encodeWav(samples, sampleRate) {
    var n = samples ? samples.length : 0;
    var rate = sampleRate || 22050;
    var bytes = new Uint8Array(44 + n * 2);
    var view = new DataView(bytes.buffer);
    function str(offset, text) {
      var i;
      for (i = 0; i < text.length; i++) bytes[offset + i] = text.charCodeAt(i);
    }
    str(0, "RIFF");
    view.setUint32(4, 36 + n * 2, true);
    str(8, "WAVE");
    str(12, "fmt ");
    view.setUint32(16, 16, true);
    view.setUint16(20, 1, true);
    view.setUint16(22, 1, true);
    view.setUint32(24, rate, true);
    view.setUint32(28, rate * 2, true);
    view.setUint16(32, 2, true);
    view.setUint16(34, 16, true);
    str(36, "data");
    view.setUint32(40, n * 2, true);
    var offset = 44;
    var i;
    for (i = 0; i < n; i++) {
      var s = samples[i];
      if (s > 1) s = 1;
      if (s < -1) s = -1;
      view.setInt16(offset, s < 0 ? Math.round(s * 32768) : Math.round(s * 32767), true);
      offset += 2;
    }
    return bytes;
  }

  function cleanSpeech(text) {
    return String(text || "").replace(/\s+/g, " ").trim();
  }

  function speechWords(text) {
    var value = cleanSpeech(text);
    return value ? value.split(" ") : [];
  }

  function speechKey(text) {
    return cleanSpeech(text)
      .toLowerCase()
      .replace(/['’]/g, "'")
      .replace(/[.,!?;:…]+/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function wordsInside(hay, needle) {
    if (!needle.length || !hay.length) return false;
    return (" " + hay.join(" ") + " ").indexOf(" " + needle.join(" ") + " ") !== -1;
  }

  function collapseConsecutive(words) {
    var out = [];
    var i;
    for (i = 0; i < words.length; i++) {
      if (out.length && speechKey(out[out.length - 1]) === speechKey(words[i])) continue;
      out.push(words[i]);
    }
    return out;
  }

  function dedupeAdjacentPhrases(words) {
    var keys = [];
    var guard = 0;
    var i;
    for (i = 0; i < words.length; i++) keys.push(speechKey(words[i]));
    while (guard++ < 16) {
      var removed = false;
      var maxN = Math.floor(keys.length / 2);
      var n, j, same;
      for (n = maxN; n >= 2; n--) {
        for (i = 0; i + n * 2 <= keys.length; i++) {
          same = true;
          for (j = 0; j < n; j++) {
            if (keys[i + j] !== keys[i + n + j]) { same = false; break; }
          }
          if (!same) continue;
          words.splice(i + n, n);
          keys.splice(i + n, n);
          removed = true;
          break;
        }
        if (removed) break;
      }
      if (!removed) break;
    }
    return words;
  }

  function cleanTranscript(text) {
    return dedupeAdjacentPhrases(collapseConsecutive(speechWords(text))).join(" ");
  }

  function speechDelta(already, incoming) {
    var raw = dedupeAdjacentPhrases(collapseConsecutive(speechWords(incoming)));
    var b = raw.map(speechKey);
    var a = speechWords(speechKey(already));
    if (!b.length) return "";
    if (!a.length) return raw.join(" ");
    if (wordsInside(a, b)) return "";
    var joinedA = a.join(" ");
    var joinedB = b.join(" ");
    if (joinedB.indexOf(joinedA) === 0) return raw.slice(a.length).join(" ");
    var max = Math.min(a.length, b.length);
    var n, i, same;
    for (n = max; n > 0; n--) {
      same = true;
      for (i = 0; i < n; i++) {
        if (a[a.length - n + i] !== b[i]) { same = false; break; }
      }
      if (same) return raw.slice(n).join(" ");
    }
    return raw.join(" ");
  }

  function speechState() {
    return { tail: "", log: "", lastRaw: "", lastAt: 0 };
  }

  function commitSpeech(state, raw, now) {
    var text = cleanTranscript(raw);
    if (!text || !state) return "";
    var base = state.log || "";
    var delta = speechDelta(base, text);
    if (!delta) {
      var tailWords = speechWords(speechKey(base));
      var incoming = speechWords(speechKey(text));
      var sameAsLast = incoming.length <= 3 && speechKey(text) === speechKey(state.lastRaw);
      var sameAsTailEnd = incoming.length && incoming.length <= 3 && tailWords.slice(-incoming.length).join(" ") === incoming.join(" ");
      if ((sameAsLast || sameAsTailEnd) && now - state.lastAt >= 900) delta = text;
      else return "";
    }
    var deltaKeys = speechWords(speechKey(delta));
    if (deltaKeys.length >= 6 && wordsInside(speechWords(speechKey(base)), deltaKeys)) return "";
    state.log = speechWords(base + " " + delta).slice(-500).join(" ");
    state.tail = speechWords(state.log).slice(-32).join(" ");
    state.lastRaw = text;
    state.lastAt = now;
    return delta;
  }

  function speechView(ev) {
    var finals = [];
    var interim = "";
    var results = ev && ev.results;
    var i;
    if (!results) return { finals: finals, interim: "" };
    for (i = 0; i < results.length; i++) {
      var alt = results[i][0];
      var text = alt ? alt.transcript : "";
      if (results[i].isFinal) finals.push(text);
      else interim = text;
    }
    return { finals: finals, interim: interim };
  }

  function speechLive(tail, interim) {
    return speechDelta(tail, interim);
  }

  function speechPreview(tail, interim) {
    var base = speechWords(tail).slice(-12).join(" ");
    var extra = speechDelta(tail, interim);
    if (!extra) return base;
    if (!base) return extra;
    return (base + " " + extra).trim();
  }

  function applySpeechEvent(state, ev, now) {
    var view = speechView(ev);
    var added = [];
    var i;
    for (i = 0; i < view.finals.length; i++) {
      var delta = commitSpeech(state, view.finals[i], now);
      if (delta) added.push(delta);
    }
    return {
      added: added.join(" "),
      live: speechLive(state.log || state.tail, view.interim),
      preview: speechPreview(state.log || state.tail, view.interim)
    };
  }

  function wavPcm(bytes) {
    var view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
    var n = view.getUint32(40, true) / 2;
    var out = new Float32Array(n);
    var i;
    for (i = 0; i < n; i++) out[i] = view.getInt16(44 + i * 2, true) / 32768;
    return { rate: view.getUint32(24, true), samples: out };
  }

  return {
    crc32: crc32,
    zipStore: zipStore,
    unzip: unzip,
    docxParts: docxParts,
    buildDocx: buildDocx,
    docxToHtml: docxToHtml,
    parseBlocks: parseBlocks,
    formatSec: formatSec,
    fold: fold,
    buildLexicon: buildLexicon,
    matchUtterance: matchUtterance,
    prepareVoice: prepareVoice,
    resampleLinear: resampleLinear,
    encodeWav: encodeWav,
    speechState: speechState,
    commitSpeech: commitSpeech,
    applySpeechEvent: applySpeechEvent,
    speechLive: speechLive,
    speechPreview: speechPreview,
    wavPcm: wavPcm,
    utf8Decode: utf8Decode
  };
});
