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
