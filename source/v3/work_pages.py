"""DOT's · the "what we've done" section: one hub page (work.html) and one page per project (work-<slug>.html).
Three display types, as the brief asks: case study · campaign showcase · project showcase.
exec()'d by build_mp.py, which provides `bars_html` (the Talent results chart). Defines WP, WORK_CSS, WORK_JS."""

FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
def fa(n): return str(n).translate(FA)
def esc_attr(s): return s.replace('"', '&quot;')

CHAIN = ['شناخت و تحلیل مسئله', 'ساختن زیرساخت دیجیتال', 'توسعه‌ی برند و ارتباطات', 'فعال‌سازی کانال‌های بازاریابی و فروش',
         'اجرای کمپین و جذب مشتری', 'بهینه‌سازی عملکرد و افزایش فروش', 'اتوماسیون و سیستم‌های هوشمند']
CATS = [('growth', 'رشد کسب‌وکار', 'Business Growth'), ('digital', 'دیجیتال و فناوری', 'Digital & Technology'),
        ('campaign', 'کمپین و بازاریابی', 'Campaigns & Marketing'), ('brand', 'برند و تعامل', 'Brand & Engagement')]
CAT = {k: (f, e) for k, f, e in CATS}
STATUS = {'done': ('تکمیل‌شده', 'Completed'), 'live': ('ادامه‌دار', 'Ongoing'), 'wip': ('در حال اجرا', 'In progress'), 'dev': ('در حال توسعه', 'In development')}
TYPES = {'case': ('مطالعه‌ی موردی', 'Case study', 'مطالعه‌ی موردی جامع', 'Case studies'),
         'campaign': ('کمپین', 'Campaign showcase', 'کمپین‌ها', 'Campaigns'),
         'project': ('پروژه', 'Project showcase', 'پروژه‌های در حال توسعه', 'Projects')}

# ── content. Lines marked DRAFT are written from the brief's intent and need the brand owner's check before launch.
P = [
 dict(slug='talent', n=1, type='case', cat='growth', brand='قهوه تلنت', status='live', chain={1, 2, 3, 4, 5, 6, 7}, wip={7},
      title='قهوه تلنت', h1='قهوه تلنت:', h1b='از بازاریابی دیجیتال تا رشد کسب‌وکار.', en='From digital marketing to business growth',
      sub='مسیر رشد یک برند قهوه، از زیرساخت دیجیتال تا اتوماسیون بازاریابی.',
      desc='مطالعه‌ی موردی قهوه تلنت: پنج مرحله از زیرساخت دیجیتال تا اتوماسیون بازاریابی؛ فروش آنلاین در یک سال ۲٫۵ برابر شد.',
      challenge='رشد فروش آنلاین، بدون این‌که هزینه‌ی جذب مشتری هم‌پای آن بالا برود.',  # DRAFT
      approach='سئو، برند، اینستاگرام و تبلیغات را خدمت‌های جدا از هم ندیدیم؛ همه را یک مسیر رشد دیدیم که از زیرساخت دیجیتال شروع می‌شود و به اتوماسیون بازاریابی می‌رسد.',
      phases=[
        ('Digital foundation', 'زیرساخت دیجیتال', 'done', ['سئو و بهینه‌سازی وب‌سایت', 'داشبوردهای گزارش‌گیری', 'برنامه‌ی بازاریابی دیجیتال', 'برنامه‌ی محتوای اینستاگرام', 'تعریف شاخص‌های عملکرد (KPI)']),
        ('Brand development', 'توسعه‌ی برند', 'done', ['تحلیل وضعیت برند', 'بازنگری در جایگاه‌یابی', 'استراتژی ارتباطات', 'بهبود هویت کلامی و بصری', 'طراحی روایت برند']),
        ('Marketing & sales channels', 'کانال‌های بازاریابی و فروش', 'done', ['فعال‌سازی کانال‌های فروش', 'طراحی کمپین‌های تبلیغاتی', 'توسعه‌ی کانال‌های دیجیتال', 'بهبود مسیر تبدیل مخاطب به مشتری', 'بازاریابی یکپارچه']),
        ('Growth & optimization', 'اندازه‌گیری و بهینه‌سازی', 'done', ['تحلیل عملکرد کانال‌ها', 'بررسی هزینه‌ی جذب مشتری', 'بهبود بازده تبلیغات', 'توسعه‌ی فروش آنلاین', 'تصمیم‌گیری بر پایه‌ی داده']),
        ('AI & automation', 'هوش مصنوعی و اتوماسیون', 'wip', ['سیستم اتوماسیون بازاریابی', '<a href="work-captain.html">توسعه‌ی سیستم <bdi class="latin">Captain</bdi></a>', 'برنامه‌ریزی تولید محتوا و تبلیغات', 'پایش بازدید و شاخص‌های دقیق عملکرد', 'یکپارچه‌سازی فرایندهای بازاریابی'])],
      results=['فروش آنلاین: ۲٫۵ برابر', 'هزینه‌ی جذب هر مشتری: ۳۰٪ کمتر', 'بازده تبلیغات آنلاین: ۲۰٪ بیشتر', 'کمپین مشارکت هواداران، با بیش از ۱٬۰۰۰ شرکت‌کننده'],
      insight='رشد پایدار از جای‌دادن بودجه در نقطه‌ی درست قیف می‌آید، نه از بیشتر کردن آن.',  # DRAFT
      related=['coldbrew', 'sports', 'connections', 'captain']),
 dict(slug='partak', n=2, type='case', cat='digital', brand='پارتاک استور', status='live', chain={1, 2, 4, 6}, wip=set(),
      title='پارتاک استور', h1='پارتاک استور:', h1b='ساختن زیرساخت فروش دیجیتال.', en='Building a digital sales infrastructure',
      sub='از ساختار فروشگاه تا نرخ تبدیل؛ مطالعه‌ای که با هر نتیجه‌ی تازه کامل‌تر می‌شود.',
      desc='مطالعه‌ی موردی پارتاک استور: زیرساخت فروش دیجیتال، سئو و رشد ارگانیک، کانال‌های فروش و بهینه‌سازی نرخ تبدیل.',
      challenge='ساختن زیرساخت فروش دیجیتال و بهتر کردن عملکرد فروشگاه اینترنتی؛ مسئله‌ای جدا از تلنت، با هدفی دیگر.',
      approach='اول زیرساخت و ساختار فروشگاه، بعد ورودی ارگانیک و کانال‌ها، و در آخر نرخ تبدیل؛ هر مرحله روی مرحله‌ی قبل ساخته می‌شود.',
      phases=[
        ('Digital infrastructure', 'زیرساخت دیجیتال', 'done', ['بررسی وضعیت وب‌سایت', 'بهینه‌سازی ساختار فروشگاه', 'بهبود تجربه‌ی خرید', 'زیرساخت لازم برای فروش آنلاین']),
        ('SEO & organic growth', 'سئو و رشد ارگانیک', 'done', ['تحقیق کلمات کلیدی', 'ساختار محتوایی', 'بهینه‌سازی صفحه‌های محصول', 'بهبود رتبه و ورودی ارگانیک']),
        ('Sales channels', 'کانال‌های فروش', 'done', ['توسعه‌ی کانال‌های ارتباطی', 'اتصال مسیرهای بازاریابی به فروشگاه', 'بهبود مسیر خرید مشتری', 'طراحی فعالیت‌های تبلیغاتی']),
        ('Conversion & performance', 'نرخ تبدیل و عملکرد', 'live', ['بهینه‌سازی نرخ تبدیل', 'تحلیل رفتار کاربران', 'یافتن نقطه‌های ریزش قیف فروش', 'بهبود صفحه‌های محصول', 'بهینه‌سازی فرایند خرید'])],
      results=None, insight=None, related=['bfyalda']),
 dict(slug='coldbrew', n=3, type='campaign', cat='campaign', brand='قهوه تلنت', status='done', chain={3, 5}, wip=set(), kind='کمپین فصلی',
      title='تابستان با کلدبرو', h1='تابستان را با کلدبرو خنک کنید.', h1b='کمپین فصلی قهوه تلنت.', en='Chill the summer with cold brew',
      sub='کمپین فصلی تابستان برای قهوه تلنت.',
      desc='کمپین فصلی «تابستان را با کلدبرو خنک کنید» برای قهوه تلنت: هدف، ایده و منطق پشت کمپین.',
      objective='ایجاد حس شادی و نشاط، و تجربه‌ای متفاوت از مصرف قهوه در فصل تابستان.',
      idea='قهوه فقط نوشیدنی گرم صبح نیست؛ کلدبرو آن را به تجربه‌ای خنک و شاد برای روزهای گرم تبدیل می‌کند.',  # DRAFT
      execution=None, result=None, visual='coldbrew', cap='کلدبرو: قهوه، خنک و شاد، برای روزهای گرم.', related=['talent']),
 dict(slug='bfyalda', n=4, type='campaign', cat='campaign', brand='پارتاک استور', status='live', chain={4, 5, 6}, wip=set(), kind='کمپین فروش فصلی',
      title='از بلک‌فرایدی تا یلدا', h1='از بلک‌فرایدی تا یلدا.', h1b='کمپین فروش فصلی پارتاک استور.', en='Black Friday to Yalda',
      sub='کمپین فروش فصلی برای پارتاک استور.',
      desc='کمپین «از بلک‌فرایدی تا یلدا» برای پارتاک استور: افزایش فروش آنلاین در یک فصل فروش، با سازوکار تخفیف و برنامه‌ی تبلیغات و محتوا.',
      objective='افزایش فروش آنلاین در بازه‌ی بلک‌فرایدی تا شب یلدا.',
      idea='به‌جای یک روز تخفیف، یک فصل فروش: از بلک‌فرایدی تا بلندترین شب سال.',  # DRAFT
      execution=['طراحی سازوکار تخفیف', 'برنامه‌ریزی تبلیغات', 'برنامه‌ی انتشار محتوا', 'فعال‌سازی کانال‌های فروش', 'مدیریت بازه‌ی زمانی کمپین', 'اندازه‌گیری فروش و نرخ تبدیل'],
      result='فروش و نرخ تبدیل در طول کمپین اندازه گرفته می‌شود؛ نتیجه پس از پایان کمپین همین‌جا منتشر می‌شود.',
      visual='nights', cap='هر شب کمی بلندتر، تا بلندترین شب سال: از بلک‌فرایدی تا یلدا.', related=['partak']),
 dict(slug='sports', n=5, type='project', cat='brand', brand='قهوه تلنت', status='wip', chain={1, 3}, wip=set(), kind='تعامل با برند',
      title='تلنت × جامعه‌ی ورزشی', h1='تلنت × جامعه‌ی ورزشی', h1b='ساختن جامعه، از دل سبک زندگی مخاطب.', en='Building a community through sports',
      sub='پیوند برند با جامعه‌ی ورزشکاران.',
      desc='پروژه‌ی «تلنت × جامعه‌ی ورزشی»: ارتباط برند قهوه تلنت با جامعه‌ی ورزشکاران و ساختن نقطه‌های تماس تازه با مخاطب.',
      vision='پیوند برند با سبک زندگی مخاطب، نه فقط تبلیغ قهوه.',
      problem='برند برای رسیدن به مخاطبان تازه، به نقطه‌های تماس تازه نیاز دارد.',  # DRAFT
      solution='همکاری با ورزشکاران و تولید محتوای مشترک، تا برند در جامعه‌ی ورزشی حضوری واقعی داشته باشد.',
      features=['شناسایی جامعه‌ی هدف', 'استراتژی همکاری با ورزشکاران', 'مدل همکاری با ورزشکاران', 'تولید محتوای مشترک', 'توسعه‌ی ارتباط برند در جامعه‌ی ورزشی'],
      now='در مرحله‌ی جذب ورزشکاران.', related=['talent', 'connections']),
 dict(slug='connections', n=6, type='project', cat='brand', brand='قهوه تلنت', status='wip', chain={1, 3, 6}, wip=set(), kind='تجربه‌ی مشتری',
      title='ارتباط‌های معنادار', h1='ارتباط‌های معنادار', h1b='از جذب مشتری، به حفظ رابطه با او.', en='Creating meaningful connections',
      sub='از جذب مشتری، به حفظ رابطه با او.',
      desc='پروژه‌ی «ارتباط‌های معنادار» برای قهوه تلنت: شناخت بهتر مشتری، نقطه‌های تماس تازه و رابطه‌ی بلندمدت با مخاطب.',
      vision='رابطه‌ای معنادارتر و ماندگارتر میان برند و مشتریانش.',
      problem='بازاریابی‌ای که فقط به جذب مشتری تکیه کند، رابطه را بعد از اولین خرید رها می‌کند.',  # DRAFT
      solution='شناخت بهتر مشتری و طراحی نقطه‌های تماس تازه، برای ارتباطی شخصی‌سازی‌شده و بلندمدت.',
      features=['شناخت بهتر مشتریان', 'طراحی نقطه‌های تماس تازه', 'ارتباط شخصی‌سازی‌شده', 'طراحی تجربه‌ی مشتری', 'افزایش تعامل و وفاداری', 'ارتباط بلندمدت با مخاطبان'],
      now='در حال اجرا.', related=['talent', 'sports']),
 dict(slug='captain', n=7, type='project', cat='digital', brand='DOT’s', status='dev', chain={2, 7}, wip={7}, kind='هوش مصنوعی و اتوماسیون',
      title='Captain', h1='<bdi class="latin" translate="no">Captain</bdi>', h1b='عملیات بازاریابی، با هوش مصنوعی.', en='AI-powered marketing operations',
      sub='سیستم عملیات بازاریابی با هوش مصنوعی.',
      desc='Captain: سیستم در حال توسعه‌ی DOT’s برای یکپارچه‌سازی و خودکارسازی فرایندهای بازاریابی با هوش مصنوعی.',
      vision='بهینه‌سازی و یکپارچه‌سازی فرایندهای بازاریابی با هوش مصنوعی و اتوماسیون؛ سیستمی که در آینده برای کسب‌وکارهای دیگر هم به کار بیاید.',
      problem='محتوا، تبلیغات، پایش و گزارش، هر کدام جدا و دستی اجرا می‌شوند و تصویر یکپارچه‌ای از عملکرد نمی‌سازند.',  # DRAFT
      solution='سیستمی که این فرایندها را کنار هم می‌گذارد و کارهای تکراری را خودکار می‌کند. <bdi class="latin">Captain</bdi> در دل همکاری با قهوه تلنت شکل گرفت.',
      features=[('Content', 'برنامه‌ریزی و مدیریت تولید محتوا'), ('Advertising', 'برنامه‌ریزی و مدیریت تبلیغات'), ('Analytics', 'پایش بازدید و شاخص‌های عملکرد'),
                ('Reporting', 'گزارش‌گیری و تحلیل عملکرد'), ('Automation', 'خودکارسازی فرایندهای تکراری'), ('Optimization', 'شناسایی فرصت‌های بهبود')],
      now='در حال توسعه؛ هنوز محصول آماده نیست.', related=['talent']),
]
BY = {p['slug']: p for p in P}

# services ↔ work: which services each piece of work used (the service pages list the same links in reverse)
SVC = {1: ('استراتژی و مشاوره', 'Strategy & Consulting'), 2: ('پرفورمنس و رشد', 'Performance & Growth'),
       3: ('داده و تحلیل', 'Data & Analytics'), 4: ('فناوری و اتوماسیون', 'Technology & Automation')}
USES = {'talent': [1, 2, 3, 4], 'partak': [1, 2, 3], 'coldbrew': [2], 'bfyalda': [2, 3], 'sports': [1], 'connections': [1, 3], 'captain': [4, 3]}
def svc_work(k):
    items = ''.join(f'<a class="wr sw" href="work-{q["slug"]}.html"><span class="t"><span class="mono">{q["n"]:02d} · {TYPES[q["type"]][1]}</span><b>{q["title"]}</b></span><span class="go glass" aria-hidden="true">←</span></a>'
                    for q in P if k in USES[q['slug']])
    return f'<div class="svc-work"><p class="svc-k">نمونه در عمل</p><div class="svc-list">{items}</div></div>'
def svc_used(p):
    return ('<ul class="svc-chips" aria-label="خدمات این کار">' + ''.join(f'<li><a href="capabilities.html#s{k}">{SVC[k][0]}<span class="mono">{SVC[k][1]}</span></a></li>' for k in sorted(USES[p['slug']])) + '</ul>')

# the journey strip: every branch page shows where it sits — branch → how we work → conversation
BRANCH = {'capabilities': ('خدمات', 'capabilities.html'), 'work': ('نمونه‌کار', 'work.html'), 'about': ('درباره', 'about.html')}
def journey(cur):
    if cur == 'approach':
        first = '<li class="jn done"><span class="jn-set">' + ''.join(f'<a href="{h}">{t}</a>' for t, h in BRANCH.values()) + '</span></li>'
        mid = '<li class="jn on"><a href="approach.html" aria-current="page">روش کار</a></li>'
    else:
        t, h = BRANCH[cur]
        first = f'<li class="jn on"><a href="{h}"{" aria-current=\"page\"" if cur != "work-item" else ""}>{t}</a></li>'
        mid = '<li class="jn"><a href="approach.html">روش کار</a></li>'
    return f'<nav class="jr rv" aria-label="مسیر شما در سایت"><p class="jr-k">مسیر شما</p><ol>{first}{mid}<li class="jn"><a href="#contact">گفت‌وگو</a></li></ol></nav>'

# ── small parts
def status(k, cls=''): f, e = STATUS[k]; return f'<span class="st st-{k}{cls}">{f}</span>'
def dots(p):
    li = ''.join(f'<i class="{"w" if i in p["wip"] else ("on" if i in p["chain"] else "")}"></i>' for i in range(1, 8))
    covered = '، '.join(fa(i) for i in sorted(p['chain']))
    return f'<span class="cdots" role="img" aria-label="حلقه‌های زنجیره‌ی رشد: {covered}">{li}</span>'
def num(p): return fa(f'{p["n"]:02d}')
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def row(k, en, body, cls=''): return f'<div class="rv{cls}"><span class="k">{k} <span class="mono">{en}</span></span>{body}</div>'

def card(p):
    flag = p['slug'] == 'talent'
    metrics = ('<span class="wm" aria-label="نتیجه در یک سال، نسبت به سال قبل"><span><b>۲٫۵ <small>برابر</small></b>فروش آنلاین</span>'
               '<span><b>۳۰٪ <small>کمتر</small></b>هزینه‌ی جذب</span><span><b>۲۰٪ <small>بیشتر</small></b>بازده تبلیغات</span></span>') if flag else ''
    return f'''<a class="wcard{' flag' if flag else ''}" href="work-{p['slug']}.html" data-cat="{p['cat']}">
  <span class="wc-top"><span class="mono">{p['n']:02d} · {CAT[p['cat']][1]}</span>{status(p['status'])}</span>
  <span class="wc-brand">{p['brand']}</span>
  <b class="wc-t">{p['title']}</b>
  <span class="wc-sub">{p['sub']}</span>{metrics}
  <span class="wc-foot">{dots(p)}<span class="go glass" aria-hidden="true">←</span></span>
</a>'''

# ── hub
def hub():
    chain = ''.join(f'<li><i>{fa(i)}</i><span>{t}</span></li>' for i, t in enumerate(CHAIN, 1))
    counts = {k: sum(p['cat'] == k for p in P) for k, *_ in CATS}
    btns = f'<button class="glass fbtn" type="button" data-c="all" aria-pressed="true">همه <span class="n">{fa(len(P))}</span></button>' + ''.join(
        f'<button class="glass fbtn" type="button" data-c="{k}" aria-pressed="false">{f} <span class="n">{fa(counts[k])}</span></button>' for k, f, e in CATS)
    groups = ''
    for t, (_, _, gfa, gen) in TYPES.items():
        cards = '\n'.join(card(p) for p in P if p['type'] == t)
        groups += f'''
    <section class="wgroup g-{t}" aria-labelledby="g-{t}">
      <h2 id="g-{t}" class="wg-h">{gfa} <span class="mono">{gen}</span></h2>
      <div class="wgrid">
{cards}
      </div>
    </section>'''
    body = f'''<div class="page" id="p-work">
  <div class="wrap vhead">
    <a class="crumb glass" href="#work"><span class="a" aria-hidden="true">→</span>صفحه‌ی اصلی</a>
    <p class="eyebrow"><b>چه کرده‌ایم</b><span class="mono">What we’ve done</span></p>
    <h1>از شناخت مسئله، <span>تا ساختن سیستم رشد.</span></h1>
    <p class="lede">کار DOT’s فقط اجرای بازاریابی نیست؛ در ساختن سیستم رشد کسب‌وکار نقش دارد. دو مطالعه‌ی موردی جامع، دو کمپین و سه پروژه‌ی در حال توسعه.</p>
  </div>
  <div class="wrap vbody">
    <section class="chain rv" aria-labelledby="ch-h">
      <h2 id="ch-h" class="wg-h">زنجیره‌ی رشد <span class="mono">The growth chain</span></h2>
      <ol class="chain-list">{chain}</ol>
      <p class="chain-note"><span class="cdots demo" aria-hidden="true"><i class="on"></i><i class="w"></i><i></i></span>نقطه‌های هر کارت نشان می‌دهد آن کار کدام حلقه‌ها را پوشش داده است؛ نقطه‌ی توخالی یعنی در جریان است.</p>
    </section>
    <div class="wfilter" role="group" aria-label="دسته‌بندی نمونه‌کارها">{btns}</div>
    <p class="sr-only" id="wcount" aria-live="polite"></p>{groups}
    {journey('work')}
    <div class="vcta on-dark"><p>پروژه‌ی بعدی شاید مال شما باشد. <span>در جلسه‌ی اول بگویید فروشتان کجا گیر کرده است.</span></p><div class="row"><a class="btn btn-primary" href="#contact">شروع گفت‌وگو</a><a class="btn" href="#/approach">نقشه‌ی حل مسئله را ببینید <span class="arr" aria-hidden="true">←</span></a></div></div>
  </div>
</div>'''
    return ('چه کرده‌ایم · نمونه‌کار · DOT’s',
            'نمونه‌کارهای DOT’s: مطالعه‌ی موردی قهوه تلنت و پارتاک استور، کمپین‌های فصلی و پروژه‌های در حال توسعه؛ از شناخت مسئله تا سیستم رشد.', body)

# ── visuals: flat, two lights on night, no small text on the glow (the words sit in the caption)
def visual(kind):
    if kind == 'coldbrew':
        cube = 'M1 0H3V2A1 1 0 0 0 2 3H1A1 1 0 0 0 0 2V1A1 1 0 0 0 1 0Z'
        cubes = ''.join(f'<path d="{cube}" transform="translate({x} {y}) rotate({r} 13.5 13.5) scale(9)" fill="#A9CEC7" opacity=".9"/>' for x, y, r in ((150, 100, -8), (174, 118, 10), (155, 140, 4)))
        return f'''<svg viewBox="0 0 320 200" role="img" aria-label="لیوان کلدبرو با یخ، زیر آفتاب تابستان">
  <circle cx="74" cy="60" r="24" fill="#F9F5EC" opacity=".92"/>
  <path d="M74 22v-8M74 106v-8M36 60h-8M120 60h-8M47 33l-6-6M107 93l-6-6M47 87l-6 6M107 27l-6 6" stroke="#F9F5EC" stroke-width="3" stroke-linecap="round" opacity=".55"/>
  <path d="M190 18 176 150" stroke="#F9F5EC" stroke-width="5" stroke-linecap="round" opacity=".7"/>
  <path d="M134 92H206L202 172Q201 180 193 180H147Q139 180 138 172Z" fill="#F9F5EC" opacity=".16"/>
  {cubes}
  <path d="M130 40H210L202 172Q201 180 193 180H147Q139 180 138 172Z" fill="none" stroke="#F9F5EC" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="186" cy="164" r="3" fill="#F9F5EC" opacity=".5"/><circle cx="196" cy="150" r="2" fill="#F9F5EC" opacity=".5"/><circle cx="150" cy="170" r="2.5" fill="#F9F5EC" opacity=".5"/>
</svg>'''
    n = 24; bars = ''
    for i in range(n):       # right = Black Friday, left = Yalda; each night a little longer
        x = 286 - i * 10.8; h = 34 + i * 4.2; o = .22 + .7 * i / (n - 1)
        bars += f'<rect x="{x:.1f}" y="{170 - h:.1f}" width="6" height="{h:.1f}" rx="3" fill="#F9F5EC" opacity="{o:.2f}"/>'
    x_last = 286 - (n - 1) * 10.8 + 3
    return f'''<svg viewBox="0 0 320 200" role="img" aria-label="ستون‌هایی که هر شب بلندتر می‌شوند، تا بلندترین شب سال">
  {bars}
  <circle cx="{x_last:.1f}" cy="24" r="13" fill="#F9F5EC"/>
  <path d="M28 182H292" stroke="#F9F5EC" stroke-width="1.5" opacity=".35"/>
</svg>'''

# ── one project page
def detail(p):
    tfa, ten = TYPES[p['type']][:2]
    meta = (f'<div><dt>برند</dt><dd>{p["brand"]}</dd></div><div><dt>دسته</dt><dd>{CAT[p["cat"]][0]}</dd></div>'
            f'<div><dt>وضعیت</dt><dd>{status(p["status"])}</dd></div>' + (f'<div><dt>نوع</dt><dd>{p["kind"]}</dd></div>' if p.get('kind') else ''))
    x = ''
    if p['type'] == 'case':
        if p['slug'] == 'talent':
            x += f'''<article class="case" style="margin-top:0;--surface:var(--sand)">
      <div><p class="case-meta"><span class="mono">Results · 1 year vs previous</span></p><h2 class="case-h">اول، نتیجه.</h2><p class="src">به دست علیرضا محرزی، در نقش مدیر تبلیغات و برند قهوه تلنت.</p></div>
      {bars_html}
    </article>'''
        x += '<div class="cs-rows">' + row('چالش', 'Challenge', f'<p>{p["challenge"]}</p>') + row('رویکرد', 'Approach', f'<p>{p["approach"]}</p>') + '</div>'
        ph = ''
        for i, (en, t, st, items) in enumerate(p['phases'], 1):
            pill = '' if st == 'done' else status(st)
            ph += f'''<li><details class="phase"{' open' if i == 1 else ''}><summary><span class="pn">{fa(f"{i:02d}")}</span><span class="pt"><b>{t}</b><span class="mono">{en}</span>{pill}</span><span class="pm" aria-hidden="true"></span></summary>{ul(items)}</details></li>'''
        x += f'''
    <h2 class="wsec-h rv">مسیر پروژه <span class="mono">Strategy & execution · {len(p["phases"])} phases</span></h2>
    <ol class="phases">{ph}</ol>
    <div class="cs-rows">'''
        x += row('نتایج', 'Results', ul(p['results'])) if p['results'] else row('نتایج', 'Results', '<p>نتایج در حال ثبت است؛ این مطالعه‌ی موردی با هر نتیجه‌ی تازه کامل می‌شود.</p>', ' pend')
        if p['insight']: x += row('آموخته', 'Key insight', f'<p>{p["insight"]}</p>')
        x += '</div>'
    elif p['type'] == 'campaign':
        x += f'<figure class="wvis rv">{visual(p["visual"])}<figcaption>{p["cap"]}</figcaption></figure>'
        x += '<div class="cs-rows">' + row('هدف', 'Objective', f'<p>{p["objective"]}</p>') + row('ایده', 'Creative idea', f'<p>{p["idea"]}</p>')
        x += row('اجرا', 'Execution', ul(p['execution'])) if p['execution'] else ''
        if p['result']: x += row('نتایج', 'Results', f'<p>{p["result"]}</p>', ' pend')
        if not p['execution'] and not p['result']: x += row('اجرا و نتایج', 'Execution · Results', '<p>جزئیات اجرا و نتیجه‌ی این کمپین به‌زودی همین‌جا منتشر می‌شود.</p>', ' pend')
        x += '</div>'
    else:
        feats = p['features']
        fbody = ('<ul class="fgrid">' + ''.join(f'<li><span class="mono">{e}</span>{t}</li>' for e, t in feats) + '</ul>') if isinstance(feats[0], tuple) else ul(feats)
        x += ('<div class="cs-rows">' + row('چشم‌انداز', 'Vision', f'<p>{p["vision"]}</p>') + row('مسئله', 'Problem', f'<p>{p["problem"]}</p>')
              + row('راه‌حل', 'Solution', f'<p>{p["solution"]}</p>') + row('قابلیت‌ها', 'Key features', fbody)
              + row('وضعیت فعلی', 'Current status', f'<p class="now">{status(p["status"])}<span>{p["now"]}</span></p>') + '</div>')
    rel = ''.join(f'<a class="wr" href="work-{r}.html"><span class="t"><span class="mono">{BY[r]["n"]:02d} · {TYPES[BY[r]["type"]][1]}</span><b>{BY[r]["title"]}</b></span><span class="go glass" aria-hidden="true">←</span></a>' for r in p['related'])
    body = f'''<div class="page" id="p-work">
  <div class="wrap vhead">
    <a class="crumb glass" href="work.html"><span class="a" aria-hidden="true">→</span>همه‌ی نمونه‌کارها</a>
    <p class="eyebrow"><b>{tfa}</b><span class="mono">{ten} · {p['n']:02d} · {CAT[p['cat']][1]}</span></p>
    <h1>{p['h1']} <span>{p['h1b']}</span></h1>
    <p class="wen mono">{p['en']}</p>
    <dl class="wmeta">{meta}</dl>
    <div class="wchain">{dots(p)}<span>حلقه‌های زنجیره‌ی رشد</span></div>
  </div>
  <div class="wrap vbody">
    {x}
    <h2 class="wsec-h rv">خدمات این کار <span class="mono">Services used</span></h2>
    {svc_used(p)}
    <h2 class="wsec-h rv">پروژه‌های مرتبط <span class="mono">Connected work</span></h2>
    <div class="wrel">{rel}</div>
    {journey('work').replace(' aria-current="page"', '')}
    <div class="vcta on-dark"><p>پروژه‌ای شبیه این دارید؟ <span>ببینید پیش از هر هزینه، مسئله را چطور تعریف می‌کنیم.</span></p><div class="row"><a class="btn btn-primary" href="approach.html">روش کار را ببینید <span class="arr" aria-hidden="true">←</span></a><a class="btn" href="#contact">شروع گفت‌وگو</a></div></div>
  </div>
</div>'''
    return (f'{p["title"]} · {tfa} · DOT’s'.replace('<bdi class="latin" translate="no">', '').replace('</bdi>', ''), p['desc'], body)

WP = {'work': hub()}
for p in P: WP['work-' + p['slug']] = detail(p)

WORK_CSS = r"""
/* ═════════ WHAT WE'VE DONE — hub and project pages ═════════ */
[hidden]{display:none!important}
.wg-h{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;font-size:22px;font-weight:700;line-height:1.5}
.wg-h .mono{color:var(--mute)}
@media (min-width:700px){.wg-h{font-size:26px}}
/* the growth chain: seven links, read in order */
.chain{padding:20px;border-radius:var(--r);background:var(--sand)}
.chain-list{position:relative;display:grid;gap:2px;margin-top:14px;counter-reset:c}
.chain-list li{position:relative;display:grid;grid-template-columns:32px 1fr;align-items:center;gap:12px;min-height:44px}
.chain-list li:not(:last-child)::before{content:"";position:absolute;right:15px;top:30px;bottom:-16px;width:2px;background:var(--line)}
.chain-list i{position:relative;z-index:1;display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:50%;background:var(--cream);box-shadow:inset 0 0 0 2px var(--green);font-style:normal;font-size:15px;font-weight:700;color:var(--green)}
.chain-list span{font-size:16px;font-weight:500;line-height:1.6}
.chain-note{display:flex;align-items:center;gap:12px;margin-top:14px;font-size:16px;line-height:1.8;color:var(--ink2)}
@media (min-width:1024px){
  .chain{padding:32px 36px}
  .chain-list{grid-template-columns:repeat(7,1fr);gap:12px;margin-top:22px}
  .chain-list li{grid-template-columns:1fr;align-content:start;justify-items:start;gap:12px}
  .chain-list li:not(:last-child)::before{right:32px;left:-12px;top:15px;bottom:auto;width:auto;height:2px}
  .chain-list span{font-size:15.5px}
}
/* the filter: one row, scrolls sideways on a phone */
.wfilter{display:flex;gap:8px;margin:28px calc(-1 * max(var(--pad),env(safe-area-inset-right))) 0;padding:6px max(var(--pad),env(safe-area-inset-right)) 10px;overflow-x:auto;scroll-snap-type:x proximity;scrollbar-width:none;overscroll-behavior-x:contain}
.wfilter::-webkit-scrollbar{display:none}
.fbtn{flex:none;display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 18px;border-radius:999px;font-size:15px;font-weight:600;white-space:nowrap;scroll-snap-align:start}
.fbtn .n{font-size:13px;font-weight:500;color:var(--mute)}
.fbtn[aria-pressed="true"] .n{color:inherit}
.fbtn:focus-visible{outline:2px solid rgba(var(--lit-c),.95);outline-offset:3px}
@media (min-width:1024px){.wfilter{flex-wrap:wrap;margin-inline:0;padding-inline:0;overflow:visible}}
/* groups and cards */
.wgroup{margin-top:28px}
.wgrid{display:grid;gap:10px;margin-top:14px}
@media (min-width:700px){.wgrid{grid-template-columns:repeat(2,minmax(0,1fr))}.g-case .wgrid{grid-template-columns:1fr}}
@media (min-width:1024px){.wgrid{grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.g-case .wgrid{grid-template-columns:7fr 5fr}.g-campaign .wgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
.wcard{position:relative;display:flex;flex-direction:column;gap:6px;min-height:200px;padding:20px;border-radius:var(--r);background:var(--sand);transition:background-color .3s,translate .45s var(--spring),box-shadow .4s var(--ease)}
.wcard:focus-visible{outline:2px solid rgba(var(--lit-c),.95);outline-offset:3px}
@media (hover:hover){.wcard:hover{translate:0 -2px;box-shadow:0 14px 30px -18px rgba(122,98,62,.55)}.wcard:hover .go{background-color:var(--s-bg-h)}}
.wcard:active{scale:.99}
.wc-top{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
.wc-top .mono{color:var(--mute)}
.wc-brand{margin-top:6px;font-size:14px;font-weight:600;color:var(--green)}
.wc-t{font-size:21px;font-weight:700;line-height:1.5}
.wc-sub{font-size:16px;line-height:1.75;color:var(--ink2)}
.wc-foot{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:auto;padding-top:14px}
.wcard .go,.wr .go{flex:none;display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:50%;font-family:var(--la);font-size:18px}
.wcard .go::after,.wr .go::after{display:none}
.wcard.flag .wc-t{font-size:24px}
@media (min-width:1024px){.wcard{padding:26px}.wcard.flag{padding:32px}.wcard.flag .wc-t{font-size:32px;line-height:1.35}}
.wm{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:10px}
.wm span{display:flex;flex-direction:column;gap:2px;padding:12px;border-radius:16px;background:var(--cream);font-size:13px;font-weight:500;line-height:1.5;color:var(--ink2)}
.wm b{font-size:24px;font-weight:300;line-height:1.2;color:var(--green);white-space:nowrap}
.wm b small{font-size:13px;font-weight:600}
@media (min-width:1024px){.wm b{font-size:34px}}
/* status: the word always, the dot only repeats it */
.st{display:inline-flex;align-items:center;gap:8px;min-height:28px;padding:2px 12px 2px 10px;border-radius:999px;background:var(--cream);font-size:13px;font-weight:600;line-height:1.4;color:var(--ink);white-space:nowrap}
.st::before{content:"";flex:none;width:8px;height:8px;border-radius:50%;box-sizing:border-box}
.st-done::before{background:var(--green)}
.st-live::before{background:var(--green);box-shadow:0 0 0 0 rgba(0,110,98,.45)}
.st-wip::before{border:2px solid var(--green)}
.st-dev::before{border:2px dashed var(--green)}
@media (prefers-reduced-motion:no-preference){.st-live::before{animation:stp 2.2s var(--ease) infinite}@keyframes stp{0%{box-shadow:0 0 0 0 rgba(0,110,98,.45)}70%,100%{box-shadow:0 0 0 7px rgba(0,110,98,0)}}}
/* the seven chain dots on every card */
.cdots{position:relative;display:inline-flex;align-items:center;gap:8px}
.cdots::before{content:"";position:absolute;right:4px;left:4px;top:50%;height:2px;margin-top:-1px;background:var(--line)}
.cdots i{position:relative;width:9px;height:9px;border-radius:50%;background:var(--cream);box-shadow:inset 0 0 0 1.5px var(--line)}
.cdots i.on{background:var(--green);box-shadow:none}
.cdots i.w{background:var(--cream);box-shadow:inset 0 0 0 2px var(--green)}
.chain-note .cdots{flex:none}
/* project page head */
.wen{margin-top:10px;color:var(--mute)}
.wmeta{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.wmeta div{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:4px 6px 4px 14px;border-radius:999px;background:var(--sand)}
.wmeta div:not(:has(.st)){padding-left:14px}
.wmeta dt{font-size:13px;font-weight:500;color:var(--mute)}
.wmeta dd{font-size:15px;font-weight:600}
.wchain{display:flex;align-items:center;gap:12px;margin-top:14px;font-size:13px;font-weight:500;color:var(--mute)}
.wsec-h{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;margin-top:36px;font-size:22px;font-weight:700;line-height:1.5}
.wsec-h .mono{color:var(--mute)}
@media (min-width:700px){.wsec-h{font-size:26px}}
.case-h{margin-top:8px;font-size:20px;font-weight:700;line-height:1.5}
.cs-rows+.cs-rows,.vbody>.case+.cs-rows{margin-top:10px}
.cs-rows a{color:var(--green);font-weight:600;text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:1px}
.cs-rows .pend{background:transparent;box-shadow:inset 0 0 0 1.5px var(--line)}
.cs-rows .pend p{color:var(--mute)}
.now{display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.now .st{background:var(--cream)}
/* phases: a timeline of disclosures; one open on a phone, all open on a desktop */
.phases{display:grid;gap:10px;margin-top:14px}
.phase{border-radius:var(--r);background:var(--sand)}
.phase summary{display:grid;grid-template-columns:44px 1fr 28px;align-items:center;gap:14px;min-height:72px;padding:14px 18px;list-style:none;cursor:pointer;border-radius:var(--r)}
.phase summary::-webkit-details-marker{display:none}
.phase summary:focus-visible{outline:2px solid rgba(var(--lit-c),.95);outline-offset:3px}
.pn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:50%;background:var(--cream);font-size:15px;font-weight:700;color:var(--green)}
.phase[open] .pn{background:var(--green);color:var(--cream)}
.pt{display:flex;flex-wrap:wrap;align-items:center;gap:2px 10px}
.pt b{flex-basis:100%;font-size:18px;font-weight:600;line-height:1.5}
.pt .mono{color:var(--mute)}
.pm{position:relative;width:28px;height:28px;border-radius:50%;background:var(--cream)}
.pm::before,.pm::after{content:"";position:absolute;top:13px;right:8px;width:12px;height:2px;border-radius:2px;background:var(--ink);transition:rotate .35s var(--spring)}
.pm::after{rotate:90deg}
.phase[open] .pm::after{rotate:0deg}
.phase ul{display:grid;gap:6px;padding:0 18px 20px 18px;margin-right:58px}
.phase li{display:flex;gap:10px;align-items:baseline;font-size:16.5px;line-height:1.8}
.phase li::before{content:"";flex:none;width:6px;height:6px;border-radius:50%;background:var(--green);transform:translateY(-3px)}
.phase li a{display:inline-flex;align-items:center;min-height:44px;margin-block:-8px;color:var(--green);font-weight:600;text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:1px}
@media (hover:hover){.phase summary:hover .pm{background:var(--s-bg-h)}}
@media (max-width:420px){.phase ul{margin-right:0}}
@media (min-width:1024px){.phase summary{padding:18px 26px}.phase ul{grid-template-columns:repeat(2,minmax(0,1fr));gap:6px 28px;padding:0 26px 24px}}
/* campaign visual */
.wvis{border-radius:var(--r);overflow:hidden;background:var(--sand)}
.wvis svg{width:100%;height:auto;aspect-ratio:16/10;background:var(--glow)}
.wvis figcaption{padding:14px 18px 16px;font-size:16px;line-height:1.75;color:var(--ink2)}
.wvis+.cs-rows{margin-top:10px}
@media (min-width:1024px){.wvis svg{aspect-ratio:21/9}}
/* features with an English key */
.fgrid{display:grid;gap:8px;margin-top:6px}
.cs-rows .fgrid li{display:flex;flex-direction:column;align-items:flex-start;gap:2px;padding:12px 14px;border-radius:16px;background:var(--cream);font-size:16px;line-height:1.7}
.cs-rows .fgrid li::before{display:none}
.fgrid .mono{font-size:12px;color:var(--green)}
@media (min-width:560px){.fgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1024px){.fgrid{grid-template-columns:repeat(3,minmax(0,1fr))}}
/* connected work */
.wrel{display:grid;gap:10px;margin-top:14px}
@media (min-width:700px){.wrel{grid-template-columns:repeat(2,minmax(0,1fr))}}
.wr{display:flex;align-items:center;justify-content:space-between;gap:14px;min-height:76px;padding:14px 16px 14px 14px;border-radius:var(--r);background:var(--sand);transition:translate .45s var(--spring)}
.wr .t{display:flex;flex-direction:column}
.wr .mono{font-size:12px;color:var(--mute)}
.wr b{font-size:17px;font-weight:600;line-height:1.5}
.wr:focus-visible{outline:2px solid rgba(var(--lit-c),.95);outline-offset:3px}
@media (hover:hover){.wr:hover{translate:0 -2px}.wr:hover .go{background-color:var(--s-bg-h)}}
.wr:active{scale:.99}
::view-transition-group(*){animation-duration:.32s}
/* services ↔ work */
.svc-work{margin-top:16px}
.svc-k{font-size:13px;font-weight:600;color:var(--mute);margin-bottom:8px}
.svc-list{display:grid;gap:8px}
@media (min-width:700px){.svc-list{grid-template-columns:repeat(2,minmax(0,1fr))}}
.block .wr.sw{background:var(--cream);min-height:64px;padding:10px 14px 10px 10px}
.block .wr.sw b{font-size:16px}
.svc-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.svc-chips a{display:inline-flex;align-items:center;gap:10px;min-height:44px;padding:4px 16px;border-radius:999px;background:var(--sand);font-size:15px;font-weight:600;transition:background-color .25s}
.svc-chips a .mono{font-size:12px;color:var(--mute)}
.svc-chips a:focus-visible{outline:2px solid rgba(var(--lit-c),.95);outline-offset:3px}
@media (hover:hover){.svc-chips a:hover{background:var(--sand2)}}
/* the journey strip: branch → how we work → conversation */
.jr{margin-top:32px;padding:16px 18px;border-radius:var(--r);background:var(--sand)}
.jr-k{font-size:13px;font-weight:600;color:var(--mute);margin-bottom:8px}
.jr ol{display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.jn{display:flex;align-items:center;gap:6px}
.jn+.jn::before{content:"";width:22px;height:2px;border-radius:2px;background:var(--line)}
.jn a{display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 14px;border-radius:999px;background:var(--cream);font-size:15px;font-weight:600;transition:background-color .25s}
.jn a::before{content:"";flex:none;width:8px;height:8px;border-radius:50%;box-shadow:inset 0 0 0 2px var(--green)}
.jn.on>a{background:var(--green);color:var(--cream)}
.jn.on>a::before{background:var(--cream);box-shadow:none}
.jn-set{display:inline-flex;flex-wrap:wrap;gap:4px}
.jn.done a::before{background:var(--green);box-shadow:none}
.jn a:focus-visible{outline:2px solid rgba(var(--lit-c),.95);outline-offset:3px}
@media (hover:hover){.jn:not(.on) a:hover{background:#fff}}
.jr+.vcta{margin-top:12px}
/* about page */
.block .lead-card{display:grid;grid-template-columns:1fr!important;gap:16px;padding:18px}
.block .lead-card figure{align-items:center}
.about-key{margin-top:10px}
.about-key p+p{margin-top:8px}
.who{margin-top:10px}
"""

WORK_JS = r"""
  /* what we've done: filter by category (kept in the address, so a filtered list can be shared) */
  const wf = $('#wfilter') || $('.wfilter');
  if (wf) {
    const btns = $$('button', wf), cards = $$('.wcard'), groups = $$('.wgroup'), live = $('#wcount');
    const apply = (c, user) => {
      const run = () => {
        btns.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.c === c)));
        let n = 0;
        cards.forEach((k) => { const on = c === 'all' || k.dataset.cat === c; k.hidden = !on; if (on) n++; });
        groups.forEach((g) => { g.hidden = !$$('.wcard:not([hidden])', g).length; });
        if (user) live.textContent = n.toLocaleString('fa-IR') + ' مورد نمایش داده می‌شود';
      };
      if (user && document.startViewTransition && !RM) document.startViewTransition(run); else run();
      if (user) { const u = new URL(location.href); if (c === 'all') u.searchParams.delete('c'); else u.searchParams.set('c', c); history.replaceState(null, '', u); }
    };
    btns.forEach((b) => b.addEventListener('click', () => apply(b.dataset.c, true)));
    const q = new URLSearchParams(location.search).get('c');
    apply(btns.some((b) => b.dataset.c === q) ? q : 'all', false);
    const sel = btns.find((b) => b.getAttribute('aria-pressed') === 'true'); if (sel && sel.dataset.c !== 'all') sel.scrollIntoView({ block: 'nearest', inline: 'center' });
  }
  /* project pages: every phase open on a wide screen */
  if (matchMedia('(min-width: 1024px)').matches) $$('details.phase').forEach((d) => { d.open = true; });
"""
