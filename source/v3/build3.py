"""Assemble DOT's v3. usage: python3 -I build3.py"""
import re, math
B=open('/home/claude/v3/base.html',encoding='utf-8').read()
I=open('/home/claude/v2/index2.html',encoding='utf-8').read()
T=open('/home/claude/v3/site3.src.html',encoding='utf-8').read()
J=open('/home/claude/v3/script_v2.js',encoding='utf-8').read()
MID=open('/home/claude/v3/mid.js',encoding='utf-8').read()
def cut(src,a,b,inc_b=False):
    i=src.index(a); j=src.index(b,i); return src[i:j+(len(b) if inc_b else 0)]
# intro / hands / photo from the previous build
intro_css=cut(B,'/* intro: glass backdrop (WebGL) + flat mark (SVG) */','.top{transition:opacity .6s ease,background-color .3s,border-color .3s}').replace('body.intro-on .top{opacity:0}\n','')
intro_css=intro_css.replace('.intro-skip{position:absolute;top:calc(var(--in) + 18px + env(safe-area-inset-top));left:calc(var(--in) + 18px);min-height:36px;padding:0 16px;','.intro-skip{position:absolute;top:calc(var(--in) + 18px + env(safe-area-inset-top));left:calc(var(--in) + 18px);min-height:44px;padding:0 20px;')
intro_markup=cut(B,'<!-- ورود','<a class="skip"').rstrip()
intro_js=cut(B,'const INTRO_FS = `','  intro();\n',True)
intro_js=intro_js.replace("const chipMark = document.querySelector('.brand svg'), chipWord = document.querySelector('.brand span');","const chipMark = document.querySelector('.chip svg'), chipWord = document.querySelector('.chip .word');")
o="word.style.opacity = (RM ? 1 : oC(sg(T.word))) * fade;"; assert o in intro_js
intro_js=intro_js.replace(o,"word.style.opacity = (RM ? 1 : oC(sg(T.word))) * fade * (wr.width ? 1 : 0);   // phones show the mark alone")
hands='\n  '.join(re.findall(r"  ((?:human|ai)\.src = 'data:image/webp;base64,[^']+';)",B))
photo=re.search(r'(<g clip-path="url\(#cs\)">.*?</g>)',B,re.S).group(1)
# the map from the reference page
i2css=cut(I,'/* lab (method) */','/* process (pinned) */')+cut(I,'/* ═════ Method map v3','/* ═════════ DOT’s control system')+cut(I,'/* method panel: switch','/* fields: the same material')+cut(I,'/* method map v4','</style>')
i2css+="""@media (max-width:900px){.tool-detail{grid-template-columns:1fr}.phases{grid-template-columns:1fr}.ph{opacity:1}.seg{--sw:80px}}
@media (max-width:560px){.gp-head{flex-direction:column;align-items:flex-start}.seg{--sw:74px}.gpanel{padding:12px;border-radius:26px}}
.lab{padding:0 0 56px;background:var(--glow)}"""
panel=cut(I,'<div class="gpanel mpanel">','\n    </div>\n  </div>\n</section>')
panel=panel.replace('class="btn btn-cream btn-sm"','class="btn btn-primary btn-sm"')
panel=panel.replace('<div class="gp-status"><span class="live" aria-hidden="true"></span><span id="segStatus"></span></div>','<div class="gp-status"><span class="live" aria-hidden="true"></span><span id="segStatus"></span><button type="button" class="glass mpause" id="mPause" aria-pressed="false" aria-label="توقف حرکت نقشه"><svg viewBox="0 0 14 14" aria-hidden="true"><path d="M3 2h3v10H3zM8 2h3v10H8z"/></svg></button></div>')
assert 'mPause' in panel
method_fix=("addEventListener('resize', () => { size(); focusPhase(false); draw(); });","addEventListener('resize', () => { size(); draw(); focusPhase(false); });")
helpers=cut(I,"  const $ = (s, r = document) => r.querySelector(s);","  /* ───────── 1 · INTRO")
method=cut(I,"  function method() {","  /* ───────── 6 · PROCESS")
assert method_fix[0] in method; method=method.replace(*method_fix)
# script
hero_part=J[:J.index('  /* ───── blocks & steps chart')]
form_part=J[J.index('  /* ───── contact form'):J.index('  route(true); solid(); bar();')]
script=hero_part+MID+form_part+"  route(true); tone(); bar();\n})();\n"
script=script.replace('{{INTRO_JS}}',intro_js).replace('{{HAND_SRC}}',hands)
# glyphs: the Cornerstone module, turned a quarter each time (modules rotate; the mark never does)
MP='M1 0H3V2A1 1 0 0 0 2 3H1A1 1 0 0 0 0 2V1A1 1 0 0 0 1 0Z'
mod=lambda r:f'<svg viewBox="0 0 3 3" aria-hidden="true"><path class="mod" transform="rotate({r} 1.5 1.5)" d="{MP}"/></svg>'
mod4=f'<svg viewBox="-0.3 -0.3 6.73 6.73" aria-hidden="true"><g class="mod"><g transform="rotate(-90 1.5 1.5)"><path d="{MP}"/></g><g transform="translate(3.13 0)"><path d="{MP}"/></g><g transform="translate(0 3.13) rotate(180 1.5 1.5)"><path d="{MP}"/></g><g transform="translate(3.13 3.13) rotate(90 1.5 1.5)"><path d="{MP}"/></g><circle cx="3.065" cy="3.065" r="0.55"/></g></svg>'
rows=[('#/capabilities','خدمات','WHAT WE DO',0),('#/work','نمونه‌کار','OUR WORK',90),('#/about','درباره','ABOUT',180),('#/approach','روش کار','HOW WE WORK',270),('#contact','تماس','CONTACT',0)]
sheet_rows=''.join(f'<a class="row" href="{h}"><span class="ic">{mod(r)}</span><span><b>{t}</b><small>{e}</small></span><span class="chev" aria-hidden="true">←</span></a>' for h,t,e,r in rows)
M=[('۲٫۵','برابر','فروش آنلاین',40,100),('۳۰٪','کمتر','هزینه‌ی جذب هر مشتری',100,70),('۲۰٪','بیشتر','بازده تبلیغات آنلاین',83,100)]
bars='<div class="bars reveal-bars" role="img" aria-label="قهوه تلنت، یک سال نسبت به سال قبل: فروش آنلاین ۲٫۵ برابر، هزینه‌ی جذب هر مشتری ۳۰٪ کمتر، بازده تبلیغات آنلاین ۲۰٪ بیشتر">'+''.join(
 f'<div class="metric" aria-hidden="true"><b>{a} <small>{u}</small></b><span>{b}</span><div class="plot"><i style="--h:{x}%"></i><i class="r" style="--h:{y}%"></i></div><div class="plot-k"><span>قبل</span><span>بعد</span></div></div>' for a,u,b,x,y in M)+'</div>'
CAPS=[('۰۱','Strategy &amp; Consulting','استراتژی و مشاوره','پیش از خرج کردن، مسیر را روشن می‌کنیم.','بودجه و انرژی تیم صرف کارهای پراکنده و بی‌هدف می‌شود.','نقشه‌ی رشد با هدف عددی، اولویت‌ها و بودجه‌ی پیشنهادی.',['استراتژی کسب‌وکار و بازاریابی','استراتژی بازاریابی دیجیتال','برنامه‌ریزی بازاریابی','مشاوره‌ی رشد']),
 ('۰۲','Performance &amp; Growth','پرفورمنس و رشد','کمپین‌هایی که با فروش سنجیده می‌شوند، نه با بازدید و لایک.','تبلیغات فعال است، اما فروش به اندازه‌ی هزینه رشد نمی‌کند.','قیف جذب، تقسیم بودجه میان کانال‌ها و گزارش هزینه‌ی جذب هر مشتری.',['پرفورمنس مارکتینگ','سئو','بهینه‌سازی نرخ تبدیل','جذب مشتری']),
 ('۰۳','Data &amp; Analytics','داده و تحلیل','عددهایی که نشان می‌دهند پول کجا نتیجه می‌دهد.','تصمیم‌ها با حدس گرفته می‌شوند و معلوم نیست کدام کانال فروش می‌آورد.','داشبورد شاخص‌های اصلی و گزارش منظم، به زبان خود شما.',['تحلیل بازاریابی','سنجش عملکرد','تصمیم‌گیری بر پایه‌ی داده','گزارش و بینش']),
 ('۰۴','Technology &amp; Automation','فناوری و اتوماسیون','کارهای تکراری جذب، پیگیری و گزارش، خودکار می‌شوند.','سرنخ‌ها بی‌پیگیری می‌مانند و وقت تیم صرف کار دستی می‌شود.','پیگیری خودکار سرنخ‌ها و اتصال فرم، پیام‌رسان و سیستم مدیریت مشتری.',['اتوماسیون هوش مصنوعی','اتوماسیون بازاریابی','بهینه‌سازی گردش کار','راهکارهای مبتنی بر هوش مصنوعی'])]
caps=''.join(f'<section class="block rv" id="s{k}"><header><span class="ix">{n}</span><h2>{t}</h2><span class="mono">{en}</span><p class="lede">{d}</p></header><div><dl class="facts"><div><dt>مسئله‌ای که حل می‌کند</dt><dd>{pb}</dd></div><div><dt>نمونه‌ی خروجی</dt><dd>{o}</dd></div></dl><ul class="chips" style="margin-top:12px">'+''.join(f'<li>{c}</li>' for c in cs)+'</ul>'+f'{{{{SVC_{k}}}}}'+'</div></section>' for k,(n,en,t,d,pb,o,cs) in enumerate(CAPS,1))
# the teaser map: three diamonds end to end (RTL: the flow starts on the right), a dotted trajectory above with its key points
cy=118; D=[(575,480,30),(480,330,44),(330,40,66)]
pts=[(585,52),(527,42),(480,60),(405,34),(330,58),(185,22),(40,54)]
def catmull(p):
    d=f'M{p[0][0]} {p[0][1]}'
    for i in range(len(p)-1):
        p0=p[max(0,i-1)];p1=p[i];p2=p[i+1];p3=p[min(len(p)-1,i+2)]
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6); c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        d+=f'C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]} {p2[1]}'
    return d
trail=catmull(pts)
sv=f'<svg viewBox="0 0 620 220" role="img" aria-label="نقشه‌ی حل مسئله: سه لوزی پشت سر هم از راست به چپ، هر کدام بزرگ‌تر از قبلی؛ مسیر نقطه‌چین بالای آن‌ها از شروع گفت‌وگو تا راهکار پیشنهادی می‌رود">'
for x0,x1,h in D:
    xm=(x0+x1)/2; sv+=f'<polygon class="dm" points="{x0},{cy} {xm},{cy-h} {x1},{cy} {xm},{cy+h}"/><line class="mid" x1="{xm}" y1="{cy-h}" x2="{xm}" y2="{cy+h}"/>'
for k,(x0,x1,h) in enumerate(D):
    xm=(x0+x1)/2; n=[4,5,6][k]; span=(x0-x1)
    for j in range(n):
        x=x0-span*(j+.5)/n; y=cy+h+30+(8 if j%2 else 0)
        sv+=f'<line class="tie" x1="{xm}" y1="{cy+h}" x2="{x:.1f}" y2="{y}"/><circle cx="{x:.1f}" cy="{y}" r="{3.2 if j<n-1 or k==2 else 3.2}" fill="rgba(249,245,236,.75)"/>'
    sv+=f'<circle cx="{xm}" cy="{cy+h}" r="2.4" fill="#F9F5EC"/>'
for (x,y),(jx) in zip([pts[0],pts[2],pts[4],pts[6]],[575,480,330,40]):
    sv+=f'<line class="tie" x1="{x}" y1="{y+8}" x2="{jx}" y2="{cy-4}"/>'
sv+=f'<path class="trail" d="{trail}"/><circle class="ms0" cx="{pts[0][0]}" cy="{pts[0][1]}" r="5"/>'
for (x,y) in [pts[2],pts[4],pts[6]]: sv+=f'<circle class="ms" cx="{x}" cy="{y}" r="6"/>'
sv+=f'<circle r="14" fill="rgba(54,224,200,.22)"><animateMotion dur="7.8s" repeatCount="indefinite" path="{trail}"/></circle><circle r="4" fill="#9FF5E8"><animateMotion dur="7.8s" repeatCount="indefinite" path="{trail}"/></circle></svg>'
out=(T.replace('{{INTRO_CSS}}',intro_css).replace('{{INTRO_MARKUP}}',intro_markup).replace('{{I2_CSS}}',i2css).replace('{{I2_PANEL}}',panel)
 .replace('{{I2_HELPERS}}',helpers).replace('{{I2_METHOD}}',method).replace('{{SCRIPT_MAIN}}',script).replace('{{PHOTO}}',photo).replace('{{BARS}}',bars)
 .replace('{{CAP_BLOCKS}}',caps).replace('{{SHEET_ROWS}}',sheet_rows).replace('{{MINI_SVG}}',sv).replace('{{MOD4}}',mod4)
 .replace('{{MOD0}}',mod(0)).replace('{{MOD1}}',mod(90)).replace('{{MOD2}}',mod(180)).replace('{{MOD3}}',mod(270)))
left=[x for x in re.findall(r'\{\{[A-Za-z0-9_]+\}\}',out) if not x.startswith(('{{SVC_','{{JOURNEY_'))]; assert not left, left
open('/home/claude/v3/dots-site-v3.html','w',encoding='utf-8').write(out); print('ok',len(out))
