"""DOT's brand guide v2 (the "DOT's — Logo Symbol" design file, boards 03, 11, 12) applied on top of the build.
Exec'd by build_mp.py after guide_v1.py. Defines GUIDE2_CSS and guide2_html(page, html).
  · the logo is a signature, never a UI part: no logo modules as icons, no big symbol behind the contact section
  · green is for the button and the logo; cards and message blocks are not green surfaces
  · results are a result sheet: each metric on its own scale, grey = last year (the base), green = one year on,
    the change written on a measure line between the two bar ends, guide numbers, a spec table, a table view
  · second-level pages open with the key visual: plaster wall, the two hands, labels, a measured gap or one light point"""
import re as _re

_FA2 = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
fa = lambda n: str(n).translate(_FA2)

# ───────────── result sheet (replaces the before/after columns)
_RS = [  # name, target, last year %, one year on %, change, last year index, one year on index
    ('فروش آنلاین', 'بیشتر ↑', 40, 100, '۲٫۵ برابر', '۱۰۰', '۲۵۰'),
    ('هزینه‌ی جذب هر مشتری', 'کمتر ↓', 100, 70, '۳۰٪ کمتر', '۱۰۰', '۷۰'),
    ('بازده تبلیغات آنلاین', 'بیشتر ↑', 83.3, 100, '۲۰٪ بیشتر', '۱۰۰', '۱۲۰'),
]
def result_sheet():
    rows = ''.join(
        f'<li class="rs-row" style="--a:{a}%;--b:{b}%;--lo:{min(a,b)}%;--hi:{max(a,b)}%">'
        f'<div class="rs-name"><span class="gn" aria-hidden="true">{fa(i)}</span><span><b>{n}</b><small>هدف: {t}</small></span></div>'
        f'<div class="rs-plot"><i class="rs-b0" aria-hidden="true"></i><i class="rs-b1" aria-hidden="true"></i><span class="rs-m"><em>{c}</em></span></div></li>'
        for i, (n, t, a, b, c, _, _2) in enumerate(_RS, 1))
    tab = ''.join(f'<tr><th scope="row">{n}</th><td>{x}</td><td>{y}</td><td>{c}</td></tr>' for n, t, a, b, c, x, y in _RS)
    return ('<div class="rsheet reveal-bars">'
            '<div class="rs-head"><p><b>برگه‌ی نتیجه</b><span class="mono">Result sheet</span></p>'
            '<p class="rs-key" aria-hidden="true"><span><i class="k0"></i>سال قبل، مبنا</span><span><i class="k1"></i>یک سال بعد</span></p></div>'
            f'<ol class="rs-rows">{rows}</ol>'
            '<dl class="rs-spec"><div><dt>پروژه</dt><dd>قهوه تلنت</dd></div><div><dt>بازه</dt><dd>یک سال، نسبت به سال قبل</dd></div><div><dt>مسئول</dt><dd>علیرضا محرزی</dd></div></dl>'
            '<details class="rs-tab"><summary>نمایش به‌صورت جدول</summary><table><caption>هر شاخص با مبنای ۱۰۰ برای سال قبل</caption>'
            '<thead><tr><th scope="col">شاخص</th><th scope="col">سال قبل</th><th scope="col">یک سال بعد</th><th scope="col">تغییر</th></tr></thead>'
            f'<tbody>{tab}</tbody></table></details></div>')

# ───────────── line icons for the three paths (24px, 1.6 stroke, never the logo's shape)
_ICON = {
    'capabilities.html': '<path d="M12 3.5 3.5 8 12 12.5 20.5 8Z"/><path d="m3.5 12 8.5 4.5 8.5-4.5"/><path d="m3.5 16 8.5 4.5 8.5-4.5"/>',
    'work.html': '<path d="M3.5 20.5h17"/><path d="M6.5 20.5v-6"/><path d="M12 20.5V9"/><path d="M17.5 20.5V4.5"/>',
    'about.html': '<circle cx="9" cy="8.5" r="2.8"/><circle cx="16" cy="9.5" r="2.2"/><path d="M3.5 18.5c1-4.3 10-4.3 11 0"/><path d="M14 14.6c3-.6 5.8.7 6.5 3.4"/>',
}
def _icon(href):
    d = _ICON.get(href)
    return f'<svg viewBox="0 0 24 24" aria-hidden="true" class="li">{d}</svg>' if d else ''

# ───────────── key visual for second-level pages
# frame of the hand images: 2048×768, meeting point (1023,351), fingertips AI (1001,346) · human (1046,357); u = 64 frame units
_KV = {
    # page: crop, gap offset per hand (frame units), what the engineering layer shows
    'capabilities': dict(crop='full', g=74, gap=True, spark=False),            # the problem: a measured gap, GAP 3.0u
    'about':        dict(crop='full', g=6,  gap=False, spark=True),            # the connection: one light point
    'work':         dict(crop='near', g=-16, gap=False, spark=True, tag='GAP 0.0u · CONNECTED'),   # the result
}
def kv(page):
    c = _KV[page]
    gap = (1046 - 1001 + 2 * c['g']) / 64
    eng = ''
    if c['gap']:
        eng = f'<span class="kv-m"></span><span class="kv-r">GAP {gap:.1f}u</span>'
    tag = f'<span class="kv-tag">{c["tag"]}</span>' if c.get('tag') else ''
    return (f'<figure class="pkv pkv-{c["crop"]}" style="--g:{c["g"]}" aria-hidden="true">'
            '<img class="kv-ai" src="assets/hand-ai.webp" alt="" decoding="async">'
            '<img class="kv-hu" src="assets/hand-human.webp" alt="" decoding="async">'
            + ('' if c['spark'] and c['crop'] == 'near' else '<span class="kv-c kv-c1"></span><span class="kv-c kv-c2"></span>')
            + eng
            + '<span class="kv-l kv-l-ai">هوش مصنوعی<i>AI · AUTOMATION</i></span><span class="kv-l kv-l-hu">تجربه‌ی انسانی<i>HUMAN · EXPERIENCE</i></span>'
            + ('<span class="kv-spark"></span>' if c['spark'] else '') + tag + '</figure>')

_NOISE = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'><filter id='n'>"
          "<feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/>"
          "<feColorMatrix values='0 0 0 0 .35  0 0 0 0 .30  0 0 0 0 .24  0 0 0 .16 0'/></filter>"
          "<rect width='220' height='220' filter='url(%23n)'/></svg>\")")

GUIDE2_CSS = r"""
/* ═════════ BRAND GUIDE v2 — the logo stays a signature, results read as a result sheet, the key visual opens the inner pages ═════════ */

/* the second button: green outline (glass only on the plaster of the home hero, the header and the bottom bar) */
.btn:not(.btn-primary){border-color:var(--green);color:var(--green)}
@media (hover:hover){.btn:not(.btn-primary):hover{background-color:rgba(0,110,98,.08);border-color:var(--green);color:var(--green)}}

/* guide number: a 24px line circle with a Persian numeral */
.gn{flex:none;display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;border:1px solid currentColor;font-size:12px;font-weight:600;line-height:1}

/* services: one surface for all four; a guide number instead of a turned logo module */
.cap,.cap.hl{background:var(--surface);color:var(--ink)}
.cap.hl .mono{color:var(--mute)}
.cap .gn{color:var(--green)}
.cap.hl .gn{color:var(--green)}

/* the three paths: line icons */
.path .ic svg.li{width:24px;height:24px;fill:none;stroke:var(--green);stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}

/* "a network of specialists, one accountable lead": one small light point, not a logo collage */
.model{display:flex;align-items:center;gap:12px}
.model .spark{flex:none;width:10px;height:10px;margin-inline:4px;border-radius:50%;background:radial-gradient(circle,#FFFDF4 0%,#FFE7A8 45%,#D4AF37 100%);box-shadow:0 0 12px 5px rgba(255,205,110,.5),0 0 30px 12px rgba(255,220,150,.28)}

/* message blocks are ink on the page surface, not green */
.key{background:var(--surface);color:var(--ink);border:1px solid rgba(20,22,21,.12)}
.key .mono{color:var(--mute)}
.key p span{color:var(--mute)}
.sec.sand .key{background:var(--cream)}

/* project phases: the guide number is a line circle; open is a green line, never a filled disc */
.pn,.phase[open] .pn{width:28px;height:28px;background:transparent;border:1px solid currentColor;font-size:12.5px;font-weight:600;color:var(--green)}
.phase[open] .pn{background:rgba(0,110,98,.1)}

/* the case-study card: the basis of its numbers, always beside them */
.wm-k{display:block;margin-top:8px;font-size:12.5px;color:var(--mute)}

/* ───── the result sheet ───── */
.rsheet{display:flex;flex-direction:column;gap:16px;min-width:0}
.rs-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:8px 16px;padding-bottom:12px;border-bottom:1px solid rgba(20,22,21,.55)}
.rs-head b{font-size:15px;font-weight:700}
.rs-head p:first-child{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px}
.rs-head .mono{color:var(--mute)}
.rs-key{display:flex;flex-wrap:wrap;gap:16px;font-size:13px;color:var(--ink2)}
.rs-key span{display:inline-flex;align-items:center;gap:8px}
.rs-key i{display:block;width:16px;height:6px;background:#A39E93}
.rs-key i.k1{height:10px;background:var(--green)}
.rs-rows{display:flex;flex-direction:column;gap:24px;margin:8px 0 0;padding:0;list-style:none}
.rs-row{display:grid;gap:8px;min-width:0}
@media (min-width:641px){.rs-row{grid-template-columns:minmax(150px,13em) minmax(0,1fr);gap:24px;align-items:start}}
.rs-name{display:flex;align-items:flex-start;gap:8px}
.rs-name .gn{margin-top:2px;color:var(--green)}
.rs-name b{display:block;font-size:15px;font-weight:700;line-height:1.6}
.rs-name small{display:block;font-size:12.5px;font-weight:500;color:var(--mute)}
.rs-plot{position:relative;height:72px;
  background-image:linear-gradient(to left,rgba(20,22,21,.06) 1px,transparent 1px),linear-gradient(rgba(20,22,21,.06) 1px,transparent 1px);background-size:8px 8px;background-position:right top}
.rs-plot::before{content:"";position:absolute;right:0;top:0;height:40px;width:1px;background:var(--ink)}
.rs-plot i{position:absolute;right:0;display:block;transform-origin:right center;transition:transform .7s var(--ease)}
.rs-plot .rs-b0{top:6px;height:8px;width:var(--a);background:#A39E93}
.rs-plot .rs-b1{top:18px;height:14px;width:var(--b);background:var(--green);transition-delay:.12s}
.rs-m{position:absolute;top:40px;right:var(--lo);width:calc(var(--hi) - var(--lo));height:0;border-top:1px solid rgba(20,22,21,.6);transition:opacity .4s .6s}
.rs-m::before,.rs-m::after{content:"";position:absolute;top:-28px;width:0;height:32px;border-right:1px dashed rgba(20,22,21,.45)}
.rs-m::before{right:-1px}.rs-m::after{left:0}
.rs-m em{position:absolute;top:6px;right:50%;translate:50% 0;font-style:normal;font-size:14px;font-weight:800;white-space:nowrap}
.reveal-bars .rs-plot i{transform:scaleX(.02)}.reveal-bars .rs-m{opacity:0}
.reveal-bars.in .rs-plot i{transform:none}.reveal-bars.in .rs-m{opacity:1}
@media (prefers-reduced-motion:reduce){.reveal-bars .rs-plot i{transform:none}.reveal-bars .rs-m{opacity:1}}
.rs-spec{display:grid;grid-template-columns:repeat(3,auto);margin:8px 0 0;border:1px solid rgba(20,22,21,.55);font-size:13px}
.rs-spec div{display:flex;flex-wrap:wrap;gap:4px 8px;padding:8px 12px;min-width:0}
.rs-spec div+div{border-inline-start:1px solid rgba(20,22,21,.55)}
.rs-spec dt{color:var(--mute)}.rs-spec dd{margin:0;font-weight:700}
@media (max-width:640px){.rs-spec{grid-template-columns:1fr}.rs-spec div+div{border-inline-start:0;border-top:1px solid rgba(20,22,21,.55)}}
.rs-tab summary{display:inline-flex;align-items:center;min-height:44px;cursor:pointer;font-size:14px;font-weight:700;color:var(--green);list-style:none}
.rs-tab summary::-webkit-details-marker{display:none}
.rs-tab summary:focus-visible{outline:2px solid var(--green);outline-offset:3px}
.rs-tab table{width:100%;border-collapse:collapse;font-size:14px;font-variant-numeric:tabular-nums}
.rs-tab caption{caption-side:bottom;padding-top:8px;text-align:right;font-size:12.5px;color:var(--mute)}
.rs-tab th,.rs-tab td{padding:8px;border-bottom:1px solid rgba(20,22,21,.15);text-align:right}
.rs-tab thead th{font-size:12.5px;font-weight:600;color:var(--mute)}

/* ───── key visual for the inner pages: plaster, the two hands, labels, a measured gap or one light point ───── */
.pkv{--H:clamp(232px,26vw,340px);--yp:.5;--k:.82;--kw:1;--cr:128;position:relative;height:var(--H);margin:16px 0 24px;overflow:hidden;border-radius:var(--r);container-type:inline-size;color:var(--ink);
  background:radial-gradient(ellipse at 50% -15%,rgba(255,224,150,.55),rgba(255,224,150,0) 62%),__NOISE__,#EFE7D8;box-shadow:inset 0 0 0 1px rgba(20,22,21,.08)}
.pkv>*{position:absolute;pointer-events:none}
.pkv{--s:min(calc(var(--H) * var(--k) / 427),calc(100cqw * var(--kw) / 1388))}
.pkv-near{--k:2.1;--kw:99;--cr:46}
.pkv img{max-width:none;width:calc(2048 * var(--s));height:auto;top:calc(var(--H) * var(--yp) - 351 * var(--s));filter:drop-shadow(0 calc(14 * var(--s)) calc(18 * var(--s)) rgba(70,46,20,.26))}
.pkv .kv-ai{left:calc(50cqw - (1023 + var(--g)) * var(--s))}
.pkv .kv-hu{left:calc(50cqw - (1023 - var(--g)) * var(--s))}
.pkv .kv-c{width:calc(2 * var(--cr) * var(--s));height:calc(2 * var(--cr) * var(--s));border-radius:50%;border:1px solid rgba(20,22,21,.34);translate:-50% -50%}
.pkv .kv-c1{left:calc(50cqw - (22 + var(--g)) * var(--s));top:calc(var(--H) * var(--yp) - 5 * var(--s))}
.pkv .kv-c2{left:calc(50cqw + (23 + var(--g)) * var(--s));top:calc(var(--H) * var(--yp) + 6 * var(--s))}
.pkv .kv-m{left:calc(50cqw - (22 + var(--g)) * var(--s));width:calc((45 + 2 * var(--g)) * var(--s));top:calc(var(--H) * var(--yp) + max(var(--cr) * var(--s), 48px) + 10px);height:0;border-top:1px solid rgba(20,22,21,.45)}
.pkv .kv-m::before,.pkv .kv-m::after{content:"";position:absolute;top:-4px;width:1px;height:9px;background:rgba(20,22,21,.45)}
.pkv .kv-m::before{left:0}.pkv .kv-m::after{right:0}
.pkv .kv-r{left:50cqw;translate:-50% 0;top:calc(var(--H) * var(--yp) + max(var(--cr) * var(--s), 48px) + 18px);font-family:var(--mono);font-size:11px;letter-spacing:.12em;direction:ltr;color:rgba(20,22,21,.55)}
.pkv .kv-l{bottom:calc(var(--H) * (1 - var(--yp)) + max(var(--cr) * var(--s), 48px) + 10px);font-size:14px;font-weight:500;line-height:1.5}
.pkv .kv-l i{display:block;font-style:normal;font-family:var(--mono);font-size:11px;letter-spacing:.12em;direction:ltr;color:rgba(20,22,21,.62)}
.pkv .kv-l-ai{right:calc(50cqw + (22 + var(--g)) * var(--s) + 8px);text-align:right}
.pkv .kv-l-ai i{text-align:right}
.pkv .kv-l-hu{left:calc(50cqw + (23 + var(--g)) * var(--s) + 8px);text-align:left}
.pkv .kv-spark{left:50cqw;top:calc(var(--H) * var(--yp));width:12px;height:12px;translate:-50% -50%;border-radius:50%;background:radial-gradient(circle,#FFFDF4 0%,#FFE7A8 45%,#D4AF37 100%);
  box-shadow:0 0 17px 8px rgba(255,205,110,.55),0 0 48px 19px rgba(255,220,150,.35)}
.pkv-near .kv-spark{width:16px;height:16px}
.pkv .kv-tag{right:16px;top:14px;font-family:var(--mono);font-size:11px;letter-spacing:.12em;direction:ltr;color:rgba(20,22,21,.6)}
@media (max-width:640px){.pkv{--H:236px;--yp:.54}.pkv-near{--k:1.7}.pkv .kv-l{font-size:13px}.pkv .kv-l i{font-size:10px;letter-spacing:.08em}}
""".replace('__NOISE__', _NOISE)

_SPARK = '<span class="spark" aria-hidden="true"></span>'

def guide2_html(page, s):
    # results: the before/after columns become a result sheet
    s, nb = _re.subn(r'<div class="bars reveal-bars"[^>]*>(?:<div class="metric".*?<div class="plot-k">.*?</div></div>){3}</div>', lambda m: result_sheet(), s, flags=_re.S)
    # no logo modules as interface parts
    k = [0]
    def cap(m):
        k[0] += 1; return m.group(1) + f'<span class="gn" aria-hidden="true">{fa(k[0]).rjust(2, "۰")}</span>'
    s = _re.sub(r'(<li class="cap(?: hl)?" style="--i:\d+">)<svg viewBox="0 0 3 3" aria-hidden="true"><path class="mod"[^>]*/></svg>', cap, s)
    s = _re.sub(r'(<a class="path" href="([^"]+)"[^>]*><span class="ic">)<svg viewBox="0 0 3 3" aria-hidden="true"><path class="mod"[^>]*/></svg>',
                lambda m: m.group(1) + _icon(m.group(2)), s)
    s = _re.sub(r'<svg viewBox="-0\.3 -0\.3 6\.73 6\.73" aria-hidden="true">.*?</svg>', _SPARK, s, flags=_re.S)
    s, nbig = _re.subn(r'<svg class="big" viewBox="0 0 3 3" aria-hidden="true"><path d="[^"]*"/></svg>', '', s)
    # the case card: the basis of its numbers, visible
    s = s.replace('بازده تبلیغات</span></span>', 'بازده تبلیغات</span></span><span class="wm-k">یک سال، نسبت به سال قبل</span>')
    # inner pages open with the key visual, between the back link and the heading
    if page in _KV:
        s, nk = _re.subn(r'(<div class="wrap vhead">\s*<a class="crumb glass"[^>]*>.*?</a>)', lambda m: m.group(1) + '\n    ' + kv(page), s, count=1, flags=_re.S)
        assert nk == 1, page
    assert nbig == 1, (page, 'big')
    assert 'viewBox="0 0 3 3" aria-hidden="true"><path class="mod"' not in s.split('<footer')[0].split('</header>', 1)[-1], (page, 'module left')
    return s
