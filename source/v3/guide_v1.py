"""DOT's layout guide v1 (buttons & key visual), applied on top of the build. Exec'd by build_mp.py.
Defines GUIDE_CSS (appended last, so it wins), guide_hero(js) for the hero drawing, guide_html(html) for markup order."""
import re as _re

GUIDE_CSS = r"""
/* ═════════ LAYOUT GUIDE v1 — buttons and the key visual. u = 8px; spacings are 1, 1.5, 2, 3, 6, 9 u ═════════ */

/* buttons: 52px (48 in the header), radius 10, flat; no shadow, no gradient, no lit dot */
.btn{min-height:52px;padding:0 24px;gap:8px;border-radius:10px;border:1px solid transparent;background-image:none;box-shadow:none;
  -webkit-backdrop-filter:none;backdrop-filter:none;translate:none;transition:background-color .16s ease-out,border-color .16s ease-out,color .16s ease-out,scale .12s ease-out}
.btn::before,.btn::after{display:none}
.btn:hover,.btn:active,.btn[aria-current],.btn[aria-pressed="true"]{background-image:none;box-shadow:none;translate:none}
.btn:active{scale:.98}
.btn-sm{min-height:48px;padding:0 20px;font-size:15px}
.btn:focus-visible{outline:2px solid var(--green);outline-offset:3px}

/* filled: the main path only (book a session · start a conversation · send) */
.btn-primary{background-color:#006E62;border-color:#006E62;color:#F9F5EC}
@media (hover:hover){.btn-primary:hover{background-color:#007E70;border-color:#007E70}}
.btn-primary:active{background-color:#00564D;border-color:#00564D}

/* outline: continue, call, see all */
.btn:not(.btn-primary){background-color:transparent;border-color:rgba(20,22,21,.55);color:var(--ink)}
@media (hover:hover){.btn:not(.btn-primary):hover{background-color:rgba(0,110,98,.06);border-color:var(--green);color:var(--green)}}
.btn:not(.btn-primary):active{background-color:rgba(0,110,98,.1)}
.on-dark .btn:not(.btn-primary),.vcta .btn:not(.btn-primary),.contact .btn:not(.btn-primary),.lab .btn:not(.btn-primary){background-color:transparent;border-color:rgba(249,245,236,.55);color:var(--cream)}
@media (hover:hover){.on-dark .btn:not(.btn-primary):hover,.vcta .btn:not(.btn-primary):hover,.contact .btn:not(.btn-primary):hover,.lab .btn:not(.btn-primary):hover{background-color:rgba(249,245,236,.08);border-color:var(--cream);color:var(--cream)}}
.on-dark .btn:focus-visible,.vcta .btn:focus-visible,.contact .btn:focus-visible,.lab .btn:focus-visible{outline-color:var(--teal-l)}

/* glass: only the home hero's second button, the header and the bottom bar */
.hero .actions .btn:not(.btn-primary),.hero[data-look="fresco"] .actions .btn:not(.btn-primary){background-color:rgba(249,245,236,.6);border-color:rgba(20,22,21,.16);color:var(--ink);
  -webkit-backdrop-filter:blur(14px) saturate(160%);backdrop-filter:blur(14px) saturate(160%)}
@media (hover:hover){.hero .actions .btn:not(.btn-primary):hover{background-color:rgba(249,245,236,.85);border-color:var(--green);color:var(--green)}}
.chip,.navpill,.bar-pill{background-color:rgba(249,245,236,.6);background-image:none;box-shadow:none;border:1px solid rgba(20,22,21,.1);
  -webkit-backdrop-filter:blur(16px) saturate(160%);backdrop-filter:blur(16px) saturate(160%)}
.chip::before,.navpill::before,.bar-pill::before{display:none}
.chip:hover,.chip:active{background-color:rgba(249,245,236,.85);background-image:none;box-shadow:none;translate:none;scale:1}
.chip,.navpill{border-radius:14px}
@media (min-width:1024px){.navpill{padding:0 4px;gap:4px}.navpill .cta{min-height:48px}}

/* every other control that was glass is outline now (back link, filters, step arrows, close, contact ways, card arrows) */
.glass{background-color:transparent;background-image:none;box-shadow:none;-webkit-backdrop-filter:none;backdrop-filter:none;border:1px solid rgba(20,22,21,.3);translate:none}
.glass::before{display:none}
@media (hover:hover){.glass:hover{background-color:rgba(0,110,98,.06);background-image:none;border-color:var(--green);color:var(--green);box-shadow:none;translate:none}}
.glass:active{background-color:rgba(0,110,98,.1);box-shadow:none}
.glass[aria-pressed="true"],.glass.on{background-color:rgba(0,110,98,.1);border-color:var(--green);color:var(--green);box-shadow:none}
.on-dark .glass,.lab .glass,.contact .glass,.vcta .glass{border-color:rgba(249,245,236,.32);color:var(--cream)}
@media (hover:hover){.on-dark .glass:hover,.lab .glass:hover,.contact .glass:hover,.vcta .glass:hover{background-color:rgba(249,245,236,.08);border-color:var(--cream);color:var(--cream)}}
.on-dark .glass[aria-pressed="true"],.lab .glass[aria-pressed="true"],.on-dark .glass.on,.lab .glass.on{background-color:rgba(54,224,200,.12);border-color:var(--teal-l);color:var(--cream)}
.crumb,.gbtn,.fbtn{border-radius:10px}
.path .go{border:1px solid rgba(20,22,21,.3)}
@media (hover:hover){.path:hover .go{background-color:transparent;border-color:var(--green);color:var(--green)}}

/* the hero pause: a quiet glass circle, never in the header row */
.pause{background-color:rgba(249,245,236,.6);background-image:none;box-shadow:none;border:1px solid rgba(20,22,21,.16);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.pause::before{display:none}
@media (hover:hover){.pause:hover{box-shadow:none;translate:none;background-color:rgba(249,245,236,.85)}}
@media (max-width:859px){.pause{top:calc(var(--copyTop,80vh) - 56px);left:max(var(--pad),env(safe-area-inset-left))}}

/* hero copy, vertical rhythm: kicker 12 · headline 16 · text 24 · buttons 12 · caption */
.kicker{margin-bottom:12px}
.hero .lead{margin-top:16px}
.actions{flex-direction:column;gap:12px;margin-top:24px}
.actions .btn{width:100%}
.note{margin-top:12px}
@media (min-width:641px){.actions{flex-direction:row;flex-wrap:wrap;gap:16px}.actions .btn{width:auto;min-width:120px}}
@media (min-width:860px){.hero .kicker{margin-bottom:12px}.hero .lead{margin-top:16px}.hero .actions{gap:16px;margin-top:24px}.hero .actions .btn{padding:0 24px;gap:8px}}
@media (max-width:859px) and (max-height:700px){.hero .lead{margin-top:8px}.actions{margin-top:16px}}
@media (max-width:859px) and (max-height:620px){.kicker{margin-bottom:8px}.actions .btn:not(.btn-primary){min-height:48px}}

/* continue: 32px after the section's content; full width on phones, sized to its text from 641px, from the right */
.next-step{margin-top:32px;gap:12px;align-items:stretch}
@media (min-width:641px){.next-step{flex-direction:row;align-items:center;justify-content:flex-start;gap:16px}}
.vcta .row{gap:12px;margin-top:24px}
@media (min-width:641px){.vcta .row{flex-direction:row;flex-wrap:wrap;gap:16px}}
.form .btn{margin-top:24px}

/* bottom bar: two equal 50px buttons, start a conversation (filled) on the right, call (outline) on the left */
.bar-pill{gap:8px;padding:6px;border-radius:16px}
.bar-pill .btn{flex:1 1 0;min-height:50px;padding:0 12px}

/* menu sheet: a numbered line badge instead of the mark; filled on the right, call on the left */
.bsheet .row{grid-template-columns:24px 1fr auto;gap:16px;padding:8px 8px}
.bsheet .row .num{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;border:1px solid rgba(20,22,21,.5);font-size:12px;font-weight:500;line-height:1;color:var(--ink)}
.bsheet .row[aria-current] .num{border-color:var(--green);color:var(--green)}
.bsheet .acts{gap:16px;margin-top:24px}
.bsheet .acts .btn{min-height:52px}

/* the "your path" steps are links inside a card: never filled; the current step is a green outline */
.jn a{border-radius:10px;border:1px solid transparent}
.jn.on>a{background:rgba(0,110,98,.08);border-color:var(--green);color:var(--green)}
.jn.on>a::before{background:var(--green);box-shadow:none}

/* engineering layer: a 6u ruler under every section heading, 1px ink at 35% */
.eyebrow+h2::after{content:"";display:block;width:49px;height:6px;margin-top:16px;opacity:.35;pointer-events:none;
  background:linear-gradient(currentColor,currentColor) left bottom/100% 1px no-repeat,repeating-linear-gradient(to left,currentColor 0 1px,transparent 1px 8px)}
"""

_HERO = (
  ("const pbEl = $('#pause'), np = $('.navpill'); if (pbEl && np) pbEl.style.left = narrow ? Math.round(np.getBoundingClientRect().right + 8) + 'px' : '';",
   "const pbEl = $('#pause'); if (pbEl) pbEl.style.left = '';"),
  ("let W, H, DPR, S, O, U, cx, cy, startGap, galaxy = null;", "let W, H, DPR, S, O, U, cx, cy, startGap, galaxy = null, ZN = 72, GP = true;"),
  ("startGap = narrow ? 44 : 108;", "startGap = narrow ? 44 : 108; ZN = narrow ? 48 : 72;   // guide: the meeting point keeps 6u (48) on phones, 9u (72) on wide screens clear"),
  ("const up = (s) => Math.max((P[1] - BOX.t) * s, 128 * s + 50), down = (s) => Math.max((BOX.b - P[1]) * s, INK ? 0 : 166 * s + 26);",
   "const up = (s) => Math.max((P[1] - BOX.t) * s, Math.max(128 * s, ZN) + 50), down = (s) => Math.max((BOX.b - P[1]) * s, INK ? (GP ? Math.max(128 * s, ZN) + 36 : 0) : 166 * s + 26);"),
  ("""    let lo = .08, hi = narrow ? .6 : .85;
    for (let i = 0; i < 28; i++) { const m = (lo + hi) / 2; if (wide(m) <= W - 2 * side && up(m) + down(m) <= bot - top) lo = m; else hi = m; }
    S = lo; U = 64 * S;""",
   """    const fit = () => { let lo = .08, hi = narrow ? .6 : .85;
      for (let i = 0; i < 28; i++) { const m = (lo + hi) / 2; if (wide(m) <= W - 2 * side && up(m) + down(m) <= bot - top) lo = m; else hi = m; } return lo; };
    const zn = ZN; GP = true; S = fit(); ZN = 0; GP = false; const S0 = fit();
    // short screens: the hands keep their size; the GAP reading and the wide clear zone give way first
    if (S < S0 * .82) S = S0; else { ZN = zn; GP = true; }
    U = 64 * S;"""),
  ("cy = top + Math.max(0, (bot - top) - (up(S) + down(S))) / 2 + up(S);",
   "cy = top + Math.max(0, (bot - top) - (up(S) + down(S))) / 2 + up(S);\n    cy = Math.min(Math.max(cy, H / 3), bot - down(S));   // guide: the point sits between a third and half of the frame's height"),
  ("const mono = (txt, x, y, a, align) => { ctx.font = `500 11px \"DM Mono\", monospace`;",
   "const mono = (txt, x, y, a, align) => { ctx.font = `500 11px \"DM Mono\", monospace`; ctx.letterSpacing = '1.2px';"),
  ("const faTxt = (txt, x, y, a, align) => { ctx.font = `500 14px Estedad, Tahoma, sans-serif`;",
   "const faTxt = (txt, x, y, a, align) => { ctx.font = `500 14px Estedad, Tahoma, sans-serif`; ctx.letterSpacing = '0px';"),
  ("ctx.strokeStyle = `rgba(${INKC},${INK ? .2 : .4})`;", "ctx.strokeStyle = `rgba(${INKC},${INK ? .34 : .4})`;"),
  ("""      const dy = cy + R2 + U * .6; ctx.strokeStyle = `rgba(${INKC},.5)`;
      if (!INK) { line(a0[0], dy, h0[0], dy); line(a0[0], dy - 5, a0[0], dy + 5); line(h0[0], dy - 5, h0[0], dy + 5); }
      const gtxt = 'GAP ' + (gu < 1.05 ? '1u' : gu.toFixed(1) + 'u');
      if (!INK) mono(gtxt, cx, dy + 17, .75, 'center');""",
   """      // guide: the GAP reading sits under the point, outside its clear zone: a measure line, two ticks, DM Mono 11 at 50%
      const dy = INK ? cy + Math.max(R2, ZN) + 10 : cy + R2 + U * .6, tk = INK ? 4 : 5; ctx.strokeStyle = `rgba(${INKC},${INK ? .45 : .5})`;
      const gtxt = 'GAP ' + (gu < 1.05 ? '1u' : gu.toFixed(1) + 'u');
      if (GP || !INK) { line(a0[0], dy, h0[0], dy); line(a0[0], dy - tk, a0[0], dy + tk); line(h0[0], dy - tk, h0[0], dy + tk); mono(gtxt, cx, dy + 18, INK ? .5 : .75, 'center'); }"""),
  ("const lx = R2 * .15, ly = Math.min(a0[1], h0[1]) - R2 - 14;",
   "const lx = R2 * .15, ly = Math.min(a0[1], h0[1]) - (INK ? Math.max(R2, ZN) : R2) - 14;   // the labels stay above the fingers, outside the clear zone"),
)
def guide_hero(js):
    for a, b in _HERO:
        assert a in js, a[:80]; js = js.replace(a, b)
    return js

_FA = '۰۱۲۳۴۵۶۷۸۹'
def guide_html(s):
    # primary first: on the right when side by side (RTL), on top when stacked
    s, n1 = _re.subn(r'(<div class="acts">)(<a class="btn" [^>]*>.*?</a>)(<a class="btn btn-primary"[^>]*>.*?</a>)', r'\1\3\2', s)
    s, n2 = _re.subn(r'(<div class="bar-pill"[^>]*>)(<a class="btn" [^>]*>.*?</a>)(<a class="btn btn-primary"[^>]*>.*?</a>)', r'\1\3\2', s)
    # filled is only for the main path: «شروع گفت‌وگو» becomes the filled one, «روش کار را ببینید» the outline beside it
    s = _re.sub(r'<a class="btn btn-primary" href="([^"]*)">(روش کار را ببینید[^<]*<span class="arr" aria-hidden="true">←</span>)</a><a class="btn" href="#contact">(.*?)</a>',
                r'<a class="btn btn-primary" href="#contact">\3</a><a class="btn" href="\1">\2</a>', s)
    # menu rows: a numbered line badge in place of the mark
    k = [0]
    def num(m):
        k[0] += 1; d = f'{k[0]:02d}'.translate(str.maketrans('0123456789', _FA))
        return m.group(1) + f'<span class="num" aria-hidden="true">{d}</span>'
    s = _re.sub(r'(<a class="row" href="[^"]*"(?: aria-current="page")?>)<span class="ic">.*?</span>', num, s)
    assert n1 == 1 and n2 == 1 and k[0] == 5, (n1, n2, k[0])
    return s
