/* Tests du format cahier : lexique, .docx, notes orales. */
var assert = require("assert");
var zlib = require("zlib");
var fmt = require("./editeur-format.js");

var entries = [
  { t: "Mémoire de travail", d: "Baddeley", k: "notion", u: "livres-psychologie/07-ebook-final/categories/03-cognitive.html" },
  { t: "Stanley Milgram", d: "Obéissance", k: "auteur", u: "a.html" },
  { t: "Psychologie sociale", d: "Groupe", k: "categorie", u: "b.html" },
  { t: "Mémoire à long terme", d: "Stockage", k: "notion", u: "c.html" }
];
var lex = fmt.buildLexicon(entries);
assert.strictEqual(fmt.matchUtterance(lex, "je parle de la mémoire de travail aujourd'hui").t, "Mémoire de travail");
assert.strictEqual(fmt.matchUtterance(lex, "l'expérience de milgram").t, "Stanley Milgram");
assert.strictEqual(fmt.matchUtterance(lex, "rien à voir xyzzy"), null);
assert.strictEqual(fmt.matchUtterance(lex, "le mot mémoire tout seul"), null);
assert.strictEqual(fmt.matchUtterance(lex, "memoire de traval et puis autre chose").t, "Mémoire de travail");
assert.strictEqual(fmt.matchUtterance(lex, "stanley milgrame").t, "Stanley Milgram");
assert.strictEqual(fmt.matchUtterance(lex, "psychologie sociale au lycée").t, "Psychologie sociale");

var ramp = new Float32Array([0, 0.25, 0.5, 1]);
var down = fmt.resampleLinear(ramp, 4, 2);
assert.strictEqual(down.length, 2);
assert.ok(down[0] < down[1], "le rééchantillonnage garde l'ordre du temps");
var wav = fmt.encodeWav(ramp, 16000);
var pcm = fmt.wavPcm(wav);
assert.strictEqual(pcm.rate, 16000);
assert.strictEqual(pcm.samples.length, 4);
assert.ok(pcm.samples[0] < pcm.samples[3], "le WAV se lit dans le sens de l'enregistrement");
assert.ok(pcm.samples[3] > 0.9);

function fakeSpeech(items) {
  return {
    results: items.map(function (item) {
      var result = { isFinal: !!item.final };
      result[0] = { transcript: item.text };
      return result;
    })
  };
}
function feedSpeech(events) {
  var state = fmt.speechState();
  var wrote = [];
  events.forEach(function (event) {
    var step = fmt.applySpeechEvent(state, fakeSpeech(event.items), event.t);
    if (step.added) wrote.push(step.added);
  });
  return wrote.join(" ");
}
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: "bonjour", final: true }] },
  { t: 200, items: [{ text: "bonjour", final: true }, { text: "tout le monde", final: true }] },
  { t: 350, items: [{ text: "bonjour", final: true }, { text: "tout le monde", final: true }] }
]), "bonjour tout le monde");
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: "je vais", final: true }] },
  { t: 180, items: [{ text: "je vais bien", final: true }] },
  { t: 260, items: [{ text: "je vais bien", final: true }] }
]), "je vais bien");
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: "bonjour tout", final: true }] },
  { t: 300, items: [{ text: "tout le monde", final: true }] }
]), "bonjour tout le monde");
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: "bonjour tout le monde", final: true }] },
  { t: 500, items: [{ text: "merci beaucoup", final: true }] }
]), "bonjour tout le monde merci beaucoup");
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: "non", final: true }] },
  { t: 120, items: [{ text: "non", final: true }] }
]), "non");
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: "non", final: true }] },
  { t: 1200, items: [{ text: "non", final: true }] }
]), "non non");
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: "non", final: true }] },
  { t: 200, items: [{ text: "non non", final: true }] },
  { t: 400, items: [{ text: "non non non", final: true }] }
]), "non");
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: "plus plus complexe avec des règles qui qui qui qui organise qui organise des qui organise des relations", final: true }] }
]), "plus complexe avec des règles qui organise des relations");
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: "plus", final: true }] },
  { t: 140, items: [{ text: "plus plus", final: true }] },
  { t: 280, items: [{ text: "plus plus complexe avec des règles", final: true }] },
  { t: 420, items: [{ text: "qui qui qui qui organise", final: true }] },
  { t: 560, items: [{ text: "qui organise des", final: true }] },
  { t: 700, items: [{ text: "qui organise des relations", final: true }] },
  { t: 1600, items: [{ text: "plus plus complexe avec des règles qui qui qui qui organise qui organise des qui organise des relations", final: true }] }
]), "plus complexe avec des règles qui organise des relations");
var phrase = "bonjour j'espère que vous allez bien aujourd'hui on se retrouve pour un nouveau cours je vais parler un petit peu de tout ce qui est la psychologie sociale et inversé donc du coup";
assert.strictEqual(feedSpeech([
  { t: 0, items: [{ text: phrase, final: true }] },
  { t: 4000, items: [{ text: phrase, final: true }] },
  { t: 8000, items: [{ text: phrase + " " + phrase, final: true }] }
]), phrase);
var liveState = fmt.speechState();
fmt.commitSpeech(liveState, "bonjour tout", 0);
assert.strictEqual(fmt.speechLive(liveState.tail, "bonjour tout le monde"), "le monde");
assert.strictEqual(fmt.speechLive(liveState.tail, "bonjour tout"), "");

var html = '<p style="text-align:center"><strong>Bonjour</strong> le <font size="5">monde</font></p>' +
  '<p><voix data-voix="a1" data-sec="8"></voix></p>';
var audios = { a1: { duration: 8, transcript: "mémoire de travail" } };
var bytes = fmt.buildDocx("Cours 1", html, audios, function (raw) {
  return zlib.deflateRawSync(Buffer.from(raw));
});
assert.ok(bytes.length > 200);

fmt.docxToHtml(bytes, function (slice) {
  return zlib.inflateRawSync(Buffer.from(slice));
}).then(function (back) {
  assert.ok(back.indexOf("Bonjour") !== -1, back);
  assert.ok(back.indexOf("<strong>") !== -1, back);
  assert.ok(back.indexOf("text-align:center") !== -1, back);
  assert.ok(back.indexOf("note orale") !== -1, back);
  assert.ok(back.indexOf("mémoire de travail") !== -1, back);
  var blocks = fmt.parseBlocks(html);
  assert.strictEqual(blocks[0].align, "center");
  assert.strictEqual(blocks[0].runs[0].b, true);
  assert.ok(blocks[1].runs.some(function (run) { return run.voix && run.id === "a1"; }));
  console.log("editeur-format ok", bytes.length, "octets");
}).catch(function (err) {
  console.error(err);
  process.exit(1);
});
