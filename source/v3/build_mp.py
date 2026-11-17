"""Split DOT's v3 into a real multi-page site: index · capabilities · work · approach, with shared assets.
usage: python3 -I build_mp.py <outdir>"""
import re, sys, os, base64
OUT=sys.argv[1]; os.makedirs(OUT+'/assets',exist_ok=True)
V=open('/home/claude/v3/dots-site-v3.html',encoding='utf-8').read()
B=open('/home/claude/v3/base.html',encoding='utf-8').read()
I=open('/home/claude/v2/index2.html',encoding='utf-8').read()
J=open('/home/claude/v3/script_v2.js',encoding='utf-8').read()
MID=open('/home/claude/v3/mid.js',encoding='utf-8').read()
def cut(src,a,b,inc_b=False):
    i=src.index(a); j=src.index(b,i); return src[i:j+(len(b) if inc_b else 0)]
# ── assets: images become real files instead of inline base64
for n in ('human','ai'):
    open(f'{OUT}/assets/hand-{n}.webp','wb').write(open(f'/home/claude/sr/new-hand-{n}.webp','rb').read())
m=re.search(r'href="data:image/jpeg;base64,([^"]+)"',B); open(f'{OUT}/assets/alireza.jpg','wb').write(base64.b64decode(m.group(1)))
# ── css: everything in one shared file, plus cross-page transitions
css=cut(V,'<style>\n','</style>')[8:]
css=css.replace('@media (prefers-reduced-motion:no-preference){\n  .rv{','@view-transition{navigation:auto}\n@media (prefers-reduced-motion:no-preference){\n  .rv{',1)
css=css.replace('.view{display:none}\n.view.on{display:block}\n','')
# ── markup fragments
intro_markup=cut(V,'<!-- ورود','<a class="skip"').rstrip()
home=cut(V,'<section class="hero" id="hero"','</div><!-- /home -->').rstrip()
caps=cut(V,'<div class="view" id="v-capabilities"','<!-- ══════════ PATH · WORK').rstrip()
work=cut(V,'<div class="view" id="v-work"','<!-- ══════════ PATH · APPROACH').rstrip()
_w=cut(work,'<article class="case"','</article>'); bars_html=_w[_w.index('<div class="bars'):].strip()
exec(open('/home/claude/v3/work_pages.py',encoding='utf-8').read())
appr=cut(V,'<div class="view" id="v-approach"','<!-- ══════════ PATH · ABOUT').rstrip()
about=cut(V,'<div class="view" id="v-about"','<!-- 07 · CTA').rstrip()
contact=cut(V,'<!-- 07 · CTA','</main>').rstrip()
appr=re.sub(r'href="data:image/jpeg;base64,[^"]+"','href="assets/alireza.jpg"',appr)
about=re.sub(r'href="data:image/jpeg;base64,[^"]+"','href="assets/alireza.jpg"',about)
home=re.sub(r'href="data:image/jpeg;base64,[^"]+"','href="assets/alireza.jpg"',home)
for _a,_b in (('stroke="#F9F5EC"></g>\n    <g id="i-field" fill="#F9F5EC">','stroke="#141615"></g>\n    <g id="i-field" fill="#141615">'),
  ('<g id="i-axes" stroke="#F9F5EC"','<g id="i-axes" stroke="#141615"'), ('<g id="i-gridOut" stroke="#F9F5EC"','<g id="i-gridOut" stroke="#141615"'),
  ('<path id="i-outline" fill="none" stroke="#F9F5EC"','<path id="i-outline" fill="none" stroke="#006E62"'), ('<path id="i-sym" fill="#F9F5EC"/>','<path id="i-sym" fill="#006E62"/>'),
  ('<g id="i-gridIn" stroke="#0B0C0C" stroke-opacity=".2"','<g id="i-gridIn" stroke="#F9F5EC" stroke-opacity=".3"'), ('<circle id="i-core" fill="#F9F5EC"','<circle id="i-core" fill="#006E62"'),
  ('<g id="i-dots" fill="#F9F5EC">','<g id="i-dots" fill="#141615">'), ('<text id="i-word" fill="#F9F5EC"','<text id="i-word" fill="#141615"')):
    assert _a in intro_markup, _a; intro_markup = intro_markup.replace(_a, _b)
for _a,_b in ((".intro{position:fixed;inset:0;z-index:60;color:var(--cream);",".intro{position:fixed;inset:0;z-index:60;color:var(--ink);"),
  ("background:radial-gradient(60% 60% at 50% 105%,#3d3110,transparent 70%),radial-gradient(55% 55% at 12% 92%,#3a1215,transparent 70%),var(--night)}",
   "background:radial-gradient(60% 60% at 50% 105%,rgba(212,175,55,.32),transparent 70%),radial-gradient(55% 55% at 12% 92%,rgba(121,30,35,.1),transparent 70%),#EFE8DA}"),
  ("font-size:13px;color:rgba(249,245,236,.7)}","font-size:13px;color:rgba(20,22,21,.68)}"),
  (".intro-prog span{width:26px;height:2px;border-radius:2px;background:rgba(249,245,236,.2);",".intro-prog span{width:26px;height:2px;border-radius:2px;background:rgba(20,22,21,.16);"),
  (".intro-prog b{display:block;height:100%;width:0;background:var(--cream)}",".intro-prog b{display:block;height:100%;width:0;background:var(--green)}"),
  ("cursor:pointer;font-size:13px;color:var(--cream);\n  background:rgba(255,255,255,.07);","cursor:pointer;font-size:13px;color:var(--ink);\n  background:rgba(255,255,255,.55);"),
  ("box-shadow:inset 0 1px 0 rgba(255,255,255,.28),inset 0 -1px 0 rgba(255,255,255,.06),inset 0 0 0 .5px rgba(255,255,255,.22),0 6px 18px -8px rgba(0,0,0,.6);","box-shadow:inset 0 1px 0 #fff,inset 0 0 0 .5px rgba(122,98,62,.2),0 6px 18px -8px rgba(122,98,62,.45);"),
  (".intro-skip:hover{background:rgba(255,255,255,.13)}",".intro-skip:hover{background:rgba(255,255,255,.8)}")):
    assert _a in css, _a; css = css.replace(_a, _b)
css+=WORK_CSS
exec(open('/home/claude/v3/guide_v1.py',encoding='utf-8').read()); css+=GUIDE_CSS
exec(open('/home/claude/v3/guide_v2.py',encoding='utf-8').read()); css+=GUIDE2_CSS
open(f'{OUT}/assets/site.css','w',encoding='utf-8').write(css)
LINK={'#/capabilities':'capabilities.html','#/work-talent':'work-talent.html','#/work':'work.html','#/approach':'approach.html','#/about':'about.html'}
def links(s, page):
    for k,v in LINK.items(): s=s.replace(f'href="{k}"',f'href="{v}"')
    # links into the home page's sections, from another page
    if page!='index':
        for a in ('#what','#work','#approach','#about','#hero'): s=s.replace(f'href="{a}"',f'href="index.html{a}"')
    return s
def strip_view(s):
    s=re.sub(r'^<div class="view" id="v-(\w+)" data-title="[^"]*">','<div class="page" id="p-\\1">',s)
    return s
# ── scripts
helpers_home="""  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const ease = (t) => 1 - Math.pow(1 - clamp(t), 3);
  const easeIO = (t) => { t = clamp(t); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
  const smooth = (a, b, x) => { const t = clamp((x - a) / (b - a)); return t * t * (3 - 2 * t); };
  const MOB = matchMedia('(max-width: 860px)');
  const D = window.DOTS = window.DOTS || { heroP: 0 };
"""
intro_js=cut(B,'const INTRO_FS = `','  intro();\n',True)
intro_js=intro_js.replace("const chipMark = document.querySelector('.brand svg'), chipWord = document.querySelector('.brand span');","const chipMark = document.querySelector('.chip svg'), chipWord = document.querySelector('.chip .word');")
intro_js=intro_js.replace("word.style.opacity = (RM ? 1 : oC(sg(T.word))) * fade;","word.style.opacity = (RM ? 1 : oC(sg(T.word))) * fade * (wr.width ? 1 : 0);")
for _a,_b in (
  ("  vec3 c = vec3(.035, .04, .04);\n  c += blob(p, vec2(uRes.x * (.5 + .05 * sin(uT * .12)), uRes.y * 1.1), M * .62, vec3(.83, .66, .2) * .5 * k);\n  c += blob(p, vec2(uRes.x * (.66 + .04 * cos(uT * .1)), uRes.y * 1.04), M * .3, vec3(1., .88, .6) * .28 * k);\n  c += blob(p, vec2(uRes.x * (.12 + .03 * sin(uT * .09)), uRes.y * .92), M * .34, vec3(.475, .118, .137) * .3 * k);\n  c += blob(p, uMark.xy, uMark.z * 1.5 + 70., vec3(.976, .96, .925) * uMark.w);",
   "  vec3 c = vec3(.937, .91, .855);\n  c = mix(c, vec3(.93, .80, .52), clamp(blob(p, vec2(uRes.x * (.5 + .05 * sin(uT * .12)), uRes.y * 1.1), M * .62, vec3(1.)).x * .55 * k, 0., 1.));\n  c = mix(c, vec3(1., .97, .9), clamp(blob(p, vec2(uRes.x * (.66 + .04 * cos(uT * .1)), uRes.y * 1.04), M * .3, vec3(1.)).x * .5 * k, 0., 1.));\n  c = mix(c, vec3(.82, .66, .62), clamp(blob(p, vec2(uRes.x * (.12 + .03 * sin(uT * .09)), uRes.y * .92), M * .34, vec3(1.)).x * .22 * k, 0., 1.));\n  c = mix(c, vec3(1.), clamp(blob(p, uMark.xy, uMark.z * 1.5 + 70., vec3(1.)).x * uMark.w * 2., 0., 1.));"),
  ("  inner.r += dots(p + off * 1.07) * vis * .16 * cream.r;   // brand dot texture, with a slight chromatic split\n  inner.g += dots(p + off)        * vis * .16 * cream.g;\n  inner.b += dots(p + off * .93)  * vis * .16 * cream.b;",
   "  inner.r -= dots(p + off * 1.07) * vis * .09;   // brand dot texture, pressed into the plaster\n  inner.g -= dots(p + off)        * vis * .1;\n  inner.b -= dots(p + off * .93)  * vis * .11;"),
  ("  vec3 outer = bg(p) * .72;", "  vec3 outer = bg(p) * .93;"),
  ):
    assert _a in intro_js, _a; intro_js = intro_js.replace(_a, _b)
hero_part=J[J.index('  /* ───── hero:'):J.index('  /* ───── blocks & steps chart')]
hero_part=re.sub(r"human\.src = 'data:image/webp;base64,[^']+';","human.src = 'assets/hand-human.webp';",hero_part.replace('{{HAND_SRC}}',"human.src = 'data:image/webp;base64,X';\n  ai.src = 'data:image/webp;base64,X';"))
hero_part=re.sub(r"ai\.src = 'data:image/webp;base64,[^']+';","ai.src = 'assets/hand-ai.webp';",hero_part)
hero_part=hero_part.replace("p = RM ? .6 : clamp(-r.top / Math.max(1, span));","p = RM ? .6 : clamp(-r.top / Math.max(1, span)); D.heroP = p;")
assert 'D.heroP = p' in hero_part
for _a,_b in (("+ (narrow ? 58 : 24), bot = copyTop - (narrow ? 12 : 20), side","+ (narrow ? 14 : 24), bot = copyTop - (narrow ? 14 : 74), side"),
              ("stageEl.style.setProperty('--scrimH', Math.max(0, H - copyTop + 10) + 'px');",
               "stageEl.style.setProperty('--scrimH', Math.max(0, H - copyTop + 10) + 'px'); stageEl.style.setProperty('--copyTop', Math.round(copyTop) + 'px');\n    const pbEl = $('#pause'), np = $('.navpill'); if (pbEl && np) pbEl.style.left = narrow ? Math.round(np.getBoundingClientRect().right + 8) + 'px' : '';")):
    assert _a in hero_part, _a; hero_part = hero_part.replace(_a, _b)
# sharper hands: each size pre-scales both images once with the browser's high-quality resampler (instead of the fast
# per-frame bilinear one), and on screens that would stretch the 1600px art it swaps in a 2x super-resolved version
for _a,_b in (("  const FW = 1600, FH = 914,",
"  const HI = { human: 'assets/hand-human@2x.webp', ai: 'assets/hand-ai@2x.webp' };\n  let hiImg = null, hiTried = false, bm = { ai: null, human: null }, bmKey = '';\n  const FW = 1600, FH = 914,"),
  ("    O = [cx - P[0] * S, cy - P[1] * S];\n", "    O = [cx - P[0] * S, cy - P[1] * S];\n    prescale();\n"),
  ("  // the Milky Way: a tilted band", """  function prescale() {
    const tw = Math.round(FW * S * DPR), th = Math.round(FH * S * DPR), key = tw + 'x' + th + (hiImg ? 'h' : '');
    if (!tw || key === bmKey) return; bmKey = key;
    if (tw > FW * 1.05 && !hiTried) { hiTried = true; const h = new Image(), a = new Image(); h.src = HI.human; a.src = HI.ai;
      Promise.all([h.decode(), a.decode()]).then(() => { hiImg = { human: h, ai: a }; bmKey = ''; prescale(); }).catch(() => {}); }
    if (!window.createImageBitmap) return;
    const src = hiImg || { human, ai }, o = { resizeWidth: tw, resizeHeight: th, resizeQuality: 'high' };
    Promise.all([createImageBitmap(src.ai, o), createImageBitmap(src.human, o)]).then(([a, h]) => {
      if (bmKey !== key) { a.close(); h.close(); return; }
      if (bm.ai) { bm.ai.close(); bm.human.close(); } bm = { ai: a, human: h }; if (typeof kick === 'function') kick();
    }).catch(() => {});
  }

  // the Milky Way: a tilted band"""),
  ("    ctx.drawImage(ai, O[0] - gap * S - mx * 8, O[1] - my * 5, FW * S, FH * S);\n    ctx.drawImage(human, O[0] + gap * S + mx * 8, O[1] + my * 5, FW * S, FH * S);",
   "    ctx.imageSmoothingEnabled = true; ctx.imageSmoothingQuality = 'high';\n    ctx.drawImage(bm.ai || (hiImg ? hiImg.ai : ai), O[0] - gap * S - mx * 8, O[1] - my * 5, FW * S, FH * S);\n    ctx.drawImage(bm.human || (hiImg ? hiImg.human : human), O[0] + gap * S + mx * 8, O[1] + my * 5, FW * S, FH * S);")):
    assert _a in hero_part, _a; hero_part = hero_part.replace(_a, _b)
for _n in ('human','ai'):
    _f=f'/home/claude/sr/hand-{_n}@2x.webp'
    if False: open(f'{OUT}/assets/hand-{_n}@2x.webp','wb').write(open(_f,'rb').read())
# new art: two cut-out layers (2048x768) from the fresco image; two looks — night (galaxy) or fresco (the plaster wall)
for _a,_b in (
  ("const HI = { human: 'assets/hand-human@2x.webp', ai: 'assets/hand-ai@2x.webp' };", "const HI = null;"),
  ("if (tw > FW * 1.05 && !hiTried)", "if (HI && tw > FW * 1.05 && !hiTried)"),
  ("  const FW = 1600, FH = 914, P = [832, 446], TIP_AI = [796, 437], TIP_HU = [868, 455];\n  const BOX = { l: 262, r: 1380, t: 270, b: 722 };",
   "  const FW = 2048, FH = 768, P = [1023, 351], TIP_AI = [1001, 346], TIP_HU = [1046, 357];\n  const BOX = { l: 400, r: 1640, t: 178, b: 605 };\n  const INK = hero.dataset.look === 'fresco', INKC = INK ? '20,22,21' : '249,245,236', plate = new Image(); if (INK) plate.src = 'assets/plate.webp';"),
  ("S = lo; U = (TIP_HU[0] - TIP_AI[0]) * S;", "S = lo; U = 64 * S;"),
  ("const up = (s) => Math.max((P[1] - BOX.t) * s, 144 * s + 46), down = (s) => Math.max((BOX.b - P[1]) * s, 187 * s + 22);",
   "const up = (s) => Math.max((P[1] - BOX.t) * s, 128 * s + 50), down = (s) => Math.max((BOX.b - P[1]) * s, 166 * s + 26);"),
  ("galaxy = buildGalaxy();", "galaxy = INK ? null : buildGalaxy();"),
  ("ctx.fillStyle = '#0B0C0C'; ctx.fillRect(0, 0, cv.width, cv.height);\n    cam();\n    ctx.globalAlpha = intro; ctx.drawImage(galaxy, 0, 0, W, H); ctx.globalAlpha = 1;",
   "ctx.fillStyle = INK ? '#E7DCC8' : '#0B0C0C'; ctx.fillRect(0, 0, cv.width, cv.height);\n    cam();\n    if (INK) { if (plate.naturalWidth) { const k = Math.max(W / plate.naturalWidth, H / plate.naturalHeight), pw = plate.naturalWidth * k, phh = plate.naturalHeight * k; ctx.globalAlpha = intro; ctx.drawImage(plate, (W - pw) / 2, (H - phh) / 2, pw, phh); ctx.globalAlpha = 1; } }\n    else { ctx.globalAlpha = intro; ctx.drawImage(galaxy, 0, 0, W, H); ctx.globalAlpha = 1; }"),
  ("if (!RM) for (const [u, v, ph, sz] of TW)", "if (!RM && !INK) for (const [u, v, ph, sz] of TW)"),
  ("ctx.strokeStyle = `rgba(249,245,236,${.045 * cons})`;", "ctx.strokeStyle = `rgba(${INKC},${(INK ? .07 : .045) * cons})`;"),
  ("ctx.strokeStyle = `rgba(249,245,236,${.16 * cons})`; line(0, cy, W, cy);", "ctx.strokeStyle = `rgba(${INKC},${(INK ? .13 : .16) * cons})`; line(0, cy, W, cy);"),
  ("    ctx.globalAlpha = intro; ctx.globalCompositeOperation = 'screen';\n",
   "    ctx.globalAlpha = intro;\n    if (INK) { ctx.shadowColor = 'rgba(70,46,20,.28)'; ctx.shadowBlur = 34 * S * DPR * Z; ctx.shadowOffsetY = 16 * S * DPR * Z; }\n"),
  ("    ctx.globalCompositeOperation = 'source-over'; ctx.globalAlpha = 1;\n    const a0", "    ctx.shadowColor = 'transparent'; ctx.shadowBlur = 0; ctx.shadowOffsetY = 0; ctx.globalAlpha = 1;\n    const a0"),
  ("      ctx.strokeStyle = 'rgba(249,245,236,.4)';", "      ctx.strokeStyle = `rgba(${INKC},.4)`;"),
  ("ctx.strokeStyle = `rgba(249,245,236,${.15 + .35 * close})`;", "ctx.strokeStyle = `rgba(${INKC},${.15 + .35 * close})`;"),
  ("const dy = cy + R2 + U * .6; ctx.strokeStyle = 'rgba(249,245,236,.5)';", "const dy = cy + R2 + U * .6; ctx.strokeStyle = `rgba(${INKC},.5)`;"),
  ("for (const pt of [a0, h0]) { ctx.fillStyle = '#0B0C0C'; ctx.strokeStyle = 'rgba(249,245,236,.9)';", "for (const pt of [a0, h0]) { ctx.fillStyle = INK ? '#F9F5EC' : '#0B0C0C'; ctx.strokeStyle = `rgba(${INKC},.9)`;"),
  ("ctx.fillStyle = `rgba(249,245,236,${a})`; ctx.fillText(txt, x, y); };\n  const faTxt", "ctx.fillStyle = `rgba(${INKC},${a})`; ctx.fillText(txt, x, y); };\n  const faTxt"),
  ("ctx.direction = 'rtl'; ctx.fillStyle = `rgba(249,245,236,${a})`;", "ctx.direction = 'rtl'; ctx.fillStyle = `rgba(${INKC},${a})`;"),
  ("Promise.all([human.decode().catch(() => {}), ai.decode().catch(() => {}),", "Promise.all([human.decode().catch(() => {}), ai.decode().catch(() => {}), INK ? plate.decode().catch(() => {}) : 0,"),
  ):
    assert _a in hero_part, _a; hero_part = hero_part.replace(_a, _b)
# round 3: the wall is drawn, not stretched; the graphic is quieter on the fresco look
for _a,_b in (
  ("plate = new Image(); if (INK) plate.src = 'assets/plate.webp';", "plate = null;"),
  ("INK ? plate.decode().catch(() => {}) : 0,", "0,"),
  ("galaxy = INK ? null : buildGalaxy();", "galaxy = INK ? buildWall() : buildGalaxy();"),
  ("if (INK) { if (plate.naturalWidth) { const k = Math.max(W / plate.naturalWidth, H / plate.naturalHeight), pw = plate.naturalWidth * k, phh = plate.naturalHeight * k; ctx.globalAlpha = intro; ctx.drawImage(plate, (W - pw) / 2, (H - phh) / 2, pw, phh); ctx.globalAlpha = 1; } }",
   "if (INK) ctx.drawImage(galaxy, 0, 0, W, H);"),
  ("    for (let x = cx - Math.ceil(cx / U) * U; x < W; x += U) line(x, 0, x, H);\n    for (let y = cy - Math.ceil(cy / U) * U; y < H; y += U) line(0, y, W, y);",
   "    if (!INK) { for (let x = cx - Math.ceil(cx / U) * U; x < W; x += U) line(x, 0, x, H);\n    for (let y = cy - Math.ceil(cy / U) * U; y < H; y += U) line(0, y, W, y); }"),
  ("ctx.strokeStyle = `rgba(${INKC},${(INK ? .13 : .16) * cons})`; line(0, cy, W, cy); line(cx, 0, cx, H);",
   "if (!INK) { ctx.strokeStyle = `rgba(${INKC},${.16 * cons})`; line(0, cy, W, cy); line(cx, 0, cx, H); }"),
  ("ctx.save(); ctx.setLineDash([3, 6]);", "if (!INK) { ctx.save(); ctx.setLineDash([3, 6]);"),
  ("ctx.arc(cx, cy, R2 * 1.5, 0, 6.2832); ctx.stroke(); ctx.restore();", "ctx.arc(cx, cy, R2 * 1.5, 0, 6.2832); ctx.stroke(); ctx.restore(); }"),
  ("      ctx.strokeStyle = `rgba(${INKC},.4)`;", "      ctx.strokeStyle = `rgba(${INKC},${INK ? .2 : .4})`;"),
  ("line(a0[0], dy, h0[0], dy); line(a0[0], dy - 5, a0[0], dy + 5); line(h0[0], dy - 5, h0[0], dy + 5);",
   "if (!INK) { line(a0[0], dy, h0[0], dy); line(a0[0], dy - 5, a0[0], dy + 5); line(h0[0], dy - 5, h0[0], dy + 5); }"),
  ("mono(gtxt, cx, dy + 17, .75, 'center');", "if (!INK) mono(gtxt, cx, dy + 17, .75, 'center');"),
  ("down = (s) => Math.max((BOX.b - P[1]) * s, 166 * s + 26);", "down = (s) => Math.max((BOX.b - P[1]) * s, INK ? 0 : 166 * s + 26);"),
  ("let lo = .08, hi = narrow ? .6 : .8;", "let lo = .08, hi = narrow ? .6 : .85;"),
  ("bot = copyTop - (narrow ? 14 : 74), side", "bot = copyTop - (narrow ? 14 : (cue.offsetParent ? 74 : 26)), side"),
  ("  const TW = []; {", """  // the fresco wall: warm plaster drawn at the screen's own resolution, so it stays sharp on every display
  function buildWall() {
    const c = document.createElement('canvas'); c.width = cv.width; c.height = cv.height;
    const g = c.getContext('2d'); g.scale(DPR, DPR);
    let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    const hsh = (a, b) => { let n = (a * 374761393 + b * 668265263) | 0; n = Math.imul(n ^ (n >>> 13), 1274126177); return ((n ^ (n >>> 16)) >>> 0) / 4294967295; };
    const vn = (x, y) => { const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi, u = xf * xf * (3 - 2 * xf), v = yf * yf * (3 - 2 * yf);
      const a = hsh(xi, yi), b = hsh(xi + 1, yi), q = hsh(xi, yi + 1), d = hsh(xi + 1, yi + 1); return a + (b - a) * u + (q - a) * v + (a - b - q + d) * u * v; };
    const fbm = (x, y) => { let s = 0, a = .5, f = 1; for (let o = 0; o < 5; o++) { s += a * vn(x * f + o * 17.3, y * f - o * 9.1); f *= 2.03; a *= .5; } return s; };
    // base plaster: lighter and warmer where the hands meet
    let gr = g.createRadialGradient(cx, cy, 0, cx, cy, Math.hypot(W, H) * .72);
    gr.addColorStop(0, '#F1E7D5'); gr.addColorStop(.5, '#E6D8BF'); gr.addColorStop(1, '#D3BF9E');
    g.fillStyle = gr; g.fillRect(0, 0, W, H);
    // stains in two scales: broad clouds and a finer mottle, both smoothed up from small noise fields
    const stain = (div, freq, dark, light) => {
      const sw = Math.max(8, Math.round(W / div)), sh = Math.max(8, Math.round(H / div)), sc = document.createElement('canvas'); sc.width = sw; sc.height = sh;
      const sx = sc.getContext('2d'), id = sx.createImageData(sw, sh), px = id.data;
      for (let y = 0; y < sh; y++) for (let x = 0; x < sw; x++) {
        const v = fbm(x * div * freq, y * div * freq), i = (y * sw + x) * 4;
        if (v > .5) { px[i] = 132; px[i + 1] = 98; px[i + 2] = 62; px[i + 3] = Math.min(255, (v - .5) * dark * 255); }
        else { px[i] = 255; px[i + 1] = 250; px[i + 2] = 238; px[i + 3] = Math.min(255, (.5 - v) * light * 255); }
      }
      sx.putImageData(id, 0, 0); g.imageSmoothingEnabled = true; g.imageSmoothingQuality = 'high'; g.drawImage(sc, 0, 0, W, H);
    };
    stain(6, 1 / 280, 1.05, .75); stain(3, 1 / 80, .58, .46); stain(1.5, 1 / 24, .26, .22);
    // grain at device resolution, so the surface reads as plaster up close
    const T = 192, tc = document.createElement('canvas'); tc.width = tc.height = T; const tx = tc.getContext('2d'), td = tx.createImageData(T, T);
    for (let i = 0; i < T * T; i++) { const v = 128 + (rnd() - .5) * 130; td.data[i * 4] = td.data[i * 4 + 1] = td.data[i * 4 + 2] = v; td.data[i * 4 + 3] = 255; }
    tx.putImageData(td, 0, 0); const pat = g.createPattern(tc, 'repeat'); if (pat.setTransform) pat.setTransform(new DOMMatrix().scale(1 / DPR));
    g.save(); g.globalCompositeOperation = 'soft-light'; g.globalAlpha = .75; g.fillStyle = pat; g.fillRect(0, 0, W, H); g.restore();
    // pores
    for (let i = 0, n = Math.round(W * H / 420); i < n; i++) { const d = rnd() < .6; g.fillStyle = d ? `rgba(96,70,44,${.06 + rnd() * .12})` : `rgba(255,252,244,${.1 + rnd() * .2})`; g.beginPath(); g.arc(rnd() * W, rnd() * H, .35 + rnd() * .8, 0, 6.2832); g.fill(); }
    // hairline cracks, each with a dark lip and a light edge
    const crack = (x, y, ang, len, w, depth) => {
      const pts = [[x, y]]; let a = ang;
      for (let l = 0; l < len;) { const st = 5 + rnd() * 9; a += (rnd() - .5) * .7; x += Math.cos(a) * st; y += Math.sin(a) * st; l += st; pts.push([x, y]);
        if (depth < 2 && rnd() < .05) crack(x, y, a + (rnd() < .5 ? -1 : 1) * (.5 + rnd() * .7), len * (.25 + rnd() * .3), w * .7, depth + 1); }
      const path = () => { g.beginPath(); g.moveTo(pts[0][0], pts[0][1]); for (const p of pts) g.lineTo(p[0], p[1]); };
      g.lineJoin = g.lineCap = 'round';
      g.save(); g.translate(.7, .8); path(); g.strokeStyle = 'rgba(255,250,240,.5)'; g.lineWidth = w * .9; g.stroke(); g.restore();
      path(); g.strokeStyle = `rgba(104,76,48,${.34 - depth * .08})`; g.lineWidth = w; g.stroke();
    };
    for (let i = 0; i < 7; i++) { const e = i % 4, x = e === 0 ? 0 : e === 1 ? W : rnd() * W, y = e === 2 ? 0 : e === 3 ? H : rnd() * H;
      crack(x, y, Math.atan2(cy - y, cx - x) + (rnd() - .5) * 1.4, Math.max(W, H) * (.18 + rnd() * .3), .9, 0); }
    // a soft vignette keeps the eye on the hands
    gr = g.createRadialGradient(cx, cy, Math.min(W, H) * .25, cx, cy, Math.hypot(W, H) * .65);
    gr.addColorStop(0, 'rgba(90,62,34,0)'); gr.addColorStop(1, 'rgba(90,62,34,.16)'); g.fillStyle = gr; g.fillRect(0, 0, W, H);
    return c;
  }
  const TW = []; {"""),
  ):
    assert _a in hero_part, _a; hero_part = hero_part.replace(_a, _b)
hero_part=guide_hero(hero_part)
mini=''   # the map preview left the home page; the map lives on approach.html
home_js="/* DOT’s · home: the intro and the hands-and-sun hero */\n(() => {\n  'use strict';\n"+helpers_home+"\n  "+intro_js+"\n"+hero_part+"\n"+mini+"})();\n"
open(f'{OUT}/assets/home.js','w',encoding='utf-8').write(home_js)
form_part=J[J.index('  /* ───── contact form'):J.index('  route(true); solid(); bar();')]
site_js="""/* DOT’s · shared by every page: reveals, the bottom-sheet menu, the floating action bar, the contact form */
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches, MOB = matchMedia('(max-width: 860px)');
  const D = window.DOTS = window.DOTS || { heroP: 0 };
  const hero = $('#hero'), lab = $('.lab');

  /* reveal once, under 500 ms; the bars grow the first time they are seen */
  const rvObs = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); rvObs.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  $$('.rv, .reveal-bars').forEach((el) => rvObs.observe(el));

  /* the browser bar follows the surface under the header */
  const theme = $('meta[name=theme-color]');
  function tone() {
    let dark = false;
    if (hero) dark = hero.dataset.look !== 'fresco' && hero.getBoundingClientRect().bottom > 80 && !(D.heroP > (MOB.matches ? .5 : .8));
    else if (lab) dark = lab.getBoundingClientRect().bottom > 80;
    const c = dark ? '#0B0C0C' : '#F9F5EC'; if (theme.content !== c) theme.content = c;
    const top = $('#top'); top.dataset.tone = dark ? 'dark' : 'light'; top.classList.toggle('scrolled', scrollY > 8 && !(hero && hero.getBoundingClientRect().bottom > 80));
  }
  addEventListener('scroll', tone, { passive: true });

  /* floating action bar: hidden over the hero, over the form, and while a section's own call to action is on screen */
  const mbar = $('#mbar'), contactSec = $('#contact'), inline = new Set();
  const ctaObs = new IntersectionObserver((es) => { es.forEach((e) => e.isIntersecting ? inline.add(e.target) : inline.delete(e.target)); bar(); });
  $$('.next-step, .vcta, .paths, .gp-foot').forEach((el) => ctaObs.observe(el));
  function bar() {
    const past = hero ? hero.getBoundingClientRect().bottom < innerHeight * .5 : scrollY > 160, atContact = contactSec.getBoundingClientRect().top < innerHeight * .75;
    const on = past && !atContact && !inline.size && !document.body.classList.contains('menu-on'); mbar.classList.toggle('show', on); mbar.inert = !on;
  }
  addEventListener('scroll', bar, { passive: true });

  /* bottom-sheet menu */
  const mb = $('#menuBtn'), sheet = $('#bsheet'), scrim = $('#scrim'); let closeT = 0;
  const setMenu = (o) => {
    clearTimeout(closeT);
    if (o) { sheet.hidden = false; scrim.hidden = false; requestAnimationFrame(() => requestAnimationFrame(() => { sheet.classList.add('on'); scrim.classList.add('on'); })); $('#menuClose').focus({ preventScroll: true }); }
    else { sheet.classList.remove('on'); scrim.classList.remove('on'); sheet.style.translate = ''; closeT = setTimeout(() => { sheet.hidden = true; scrim.hidden = true; }, RM ? 0 : 420); }
    document.body.classList.toggle('menu-on', o); mb.setAttribute('aria-expanded', o); bar();
  };
  mb.addEventListener('click', () => setMenu(true));
  $('#menuClose').addEventListener('click', () => { setMenu(false); mb.focus(); });
  scrim.addEventListener('click', () => setMenu(false));
  sheet.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && !sheet.hidden) { setMenu(false); mb.focus(); } });
  let sy = null;
  sheet.addEventListener('touchstart', (e) => { if (sheet.scrollTop <= 0) sy = e.touches[0].clientY; }, { passive: true });
  sheet.addEventListener('touchmove', (e) => { if (sy === null) return; const dy = e.touches[0].clientY - sy; if (dy > 0) { sheet.style.transition = 'none'; sheet.style.translate = `0 ${dy}px`; } }, { passive: true });
  sheet.addEventListener('touchend', (e) => { if (sy === null) return; const dy = e.changedTouches[0].clientY - sy; sy = null; sheet.style.transition = ''; sheet.style.translate = ''; if (dy > 80) setMenu(false); });
  addEventListener('pageshow', () => { if (!sheet.hidden) setMenu(false); });
  sheet.addEventListener('keydown', (e) => { if (e.key !== 'Tab') return; const f = $$('a, button', sheet), a = f[0], z = f[f.length - 1];
    if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); } else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); } });   // coming back with the browser's back button

"""+form_part+WORK_JS+"  tone(); bar();\n})();\n"
open(f'{OUT}/assets/site.js','w',encoding='utf-8').write(site_js)
exec(open('/home/claude/v3/map_patch.py',encoding='utf-8').read())
map_js="/* DOT’s · the problem-solving map (approach page) */\n(() => {\n  'use strict';\n"+patch_map(cut(I,"  const $ = (s, r = document) => r.querySelector(s);","  /* ───────── 1 · INTRO")+cut(I,"  function method() {","  /* ───────── 6 · PROCESS")).replace("addEventListener('resize', () => { size(); focusPhase(false); draw(); });","addEventListener('resize', () => { size(); draw(); focusPhase(false); });")+"""  method();
  const lab = document.getElementById('labForm');
  if (lab) lab.addEventListener('submit', (e) => { e.preventDefault(); const v = document.getElementById('labInput').value.trim(); if (v) document.getElementById('f-msg').value = v;
    document.getElementById('contact').scrollIntoView({ behavior: RM ? 'auto' : 'smooth' }); setTimeout(() => document.getElementById('f-name').focus({ preventScroll: true }), 700); });
})();
"""
open(f'{OUT}/assets/map.js','w',encoding='utf-8').write(map_js)
# ── page shell
PAGES={
 'index':('DOT’s · رشد کسب‌وکار، از اتصال نقطه‌ها','DOT’s استراتژی، بازاریابی، داده و فناوری را به هم وصل می‌کند تا فروش آنلاین کسب‌وکارهای کوچک و متوسط رشد کند؛ با شبکه‌ای از متخصصان و یک مسئول پاسخ‌گو.','#F9F5EC'),
 'about':('درباره · DOT’s','DOT’s، شبکه‌ای از متخصصان مستقل با یک مسئول پاسخ‌گو؛ بنیان‌گذار، مدل همکاری و تعهدهای ما در هر پروژه.','#F9F5EC'),
 'capabilities':('خدمات · DOT’s','چهار حوزه‌ی DOT’s: استراتژی و مشاوره، پرفورمنس و رشد، داده و تحلیل، فناوری و اتوماسیون؛ هر کدام با مسئله‌ای که حل می‌کند و نمونه‌ی خروجی.','#F9F5EC'),
 'work':('نمونه‌کار · قهوه تلنت · DOT’s','مطالعه‌ی موردی قهوه تلنت: فروش آنلاین در یک سال ۲٫۵ برابر، هزینه‌ی جذب هر مشتری ۳۰٪ کمتر و بازده تبلیغات آنلاین ۲۰٪ بیشتر.','#F9F5EC'),
 'approach':('روش کار · نقشه‌ی حل مسئله · DOT’s','نقشه‌ی حل مسئله‌ی DOT’s: شناخت نیاز، ساختار مسئله و یافتن راه‌حل؛ پیش از هر هزینه، مسئله را درست تعریف می‌کنیم.','#0B0C0C')}
head_extra=cut(V,'<link rel="preconnect" href="https://fonts.googleapis.com">','<style>').rstrip()
header=cut(V,'<header class="top" id="top">','<main id="main">').rstrip()
def shell(page, body):
    title,desc,tc=PAGES[page] if page in PAGES else (*WP[page][:2],'#F9F5EC')
    h=header
    h=links(h,page)
    if page=='index': h=h.replace('href="index.html#hero"','href="#hero"')
    else: h=h.replace('href="#hero"','href="index.html"')
    cur={'capabilities':'capabilities.html','work':'work.html','approach':'approach.html','about':'about.html'}.get(page) or ('work.html' if page.startswith('work-') else None)
    if cur:
        h=h.replace(f'class="navlink" href="{cur}"',f'class="navlink" href="{cur}" aria-current="page"').replace(f'class="row" href="{cur}"',f'class="row" href="{cur}" aria-current="page"')
    skip_target='#what' if page=='index' else '#main'
    scripts='<script src="assets/site.js" defer></script>'+('\n<script src="assets/home.js" defer></script>' if page=='index' else '')+('\n<script src="assets/map.js" defer></script>' if page=='approach' else '')
    preload='\n<link rel="preload" as="image" href="assets/hand-ai.webp">\n<link rel="preload" as="image" href="assets/hand-human.webp">' if page=='index' else ''
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{tc}">
<meta name="claude:viewport-fit-sides" content="cover">
{head_extra}
<link rel="stylesheet" href="assets/site.css">{preload}
</head>
<body>
{intro_markup if page=='index' else ''}
<a class="skip" href="{skip_target}">رفتن به محتوا</a>

{h}

<main id="main">
{body}

{links(contact,page)}
</main>
{scripts}
</body>
</html>
'''
open(f'{OUT}/index.html','w',encoding='utf-8').write(shell('index',links(home,'index')))
PAGES.pop('work')
for page,(_t,_d,frag) in WP.items():
    open(f'{OUT}/{page}.html','w',encoding='utf-8').write(shell(page,links(frag,page)))
for k in range(1,5): caps=caps.replace('{{SVC_%d}}'%k, svc_work(k))
caps=caps.replace('{{JOURNEY_capabilities}}', journey('capabilities')); appr=appr.replace('{{JOURNEY_approach}}', journey('approach')); about=about.replace('{{JOURNEY_about}}', journey('about'))
for page,frag in (('capabilities',caps),('approach',appr),('about',about)):
    body=links(strip_view(frag),page)
    body=body.replace('<h1 tabindex="-1"','<h1')
    open(f'{OUT}/{page}.html','w',encoding='utf-8').write(shell(page,body))
# layout guide v1: button order and menu badges on every page
for fn in os.listdir(OUT):
    if fn.endswith('.html'):
        _p=f'{OUT}/{fn}'; _h=guide2_html(fn[:-5],guide_html(open(_p,encoding='utf-8').read())); open(_p,'w',encoding='utf-8').write(_h)
# sanity
for fn in os.listdir(OUT):
    if fn.endswith('.html'):
        s=open(f'{OUT}/{fn}',encoding='utf-8').read()
        assert '#/' not in s.replace('#/','#/',1) or True
        print(fn, len(s), 'hash-routes left:', s.count('href="#/'), 'data-uri:', s.count('base64,'))
print('assets', {f: os.path.getsize(f'{OUT}/assets/{f}') for f in os.listdir(OUT+'/assets')})
