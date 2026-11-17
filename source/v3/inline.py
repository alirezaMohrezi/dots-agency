"""Make every page self-contained: CSS, JS and images inside the HTML. usage: python3 -I inline.py <siteDir> <outDir>"""
import sys, os, re, base64
S, O = sys.argv[1], sys.argv[2]; os.makedirs(O, exist_ok=True)
rd = lambda p: open(f'{S}/assets/{p}', encoding='utf-8').read()
uri = lambda p, m: f'data:{m};base64,' + base64.b64encode(open(f'{S}/assets/{p}', 'rb').read()).decode()
css = rd('site.css')
IMG = {'hand-human.webp': uri('hand-human.webp', 'image/webp'), 'hand-ai.webp': uri('hand-ai.webp', 'image/webp'), 'alireza.jpg': uri('alireza.jpg', 'image/jpeg')}
JS = {}
for j in ('site.js', 'home.js', 'map.js'):
    t = rd(j)
    for k, v in IMG.items(): t = t.replace(f'assets/{k}', v)
    assert '</script' not in t.lower(), j
    JS[j] = t
MISS = []
for fn in sorted(f for f in os.listdir(S) if f.endswith('.html')):
    h = open(f'{S}/{fn}', encoding='utf-8').read()
    h = re.sub(r'\n<link rel="preload" as="image" href="assets/[^"]+">', '', h)
    h = h.replace('<link rel="stylesheet" href="assets/site.css">', '<style>\n' + css + '\n</style>')
    for j, t in JS.items(): h = h.replace(f'<script src="assets/{j}" defer></script>', '<script>\n' + t + '\n</script>')
    for k, v in IMG.items(): h = h.replace(f'assets/{k}', v)
    ED = open('/home/claude/v3/editor.js', encoding='utf-8').read(); assert '</script' not in ED.lower()
    mark = '<script>\n/* DOT’s · shared by every page'
    assert h.count(mark) == 1, fn
    # wording the owner changed in the browser (edits/*.json, imported with import_edits.py) is applied on every build
    import json, glob, html as _h
    log = []
    for f in sorted(glob.glob('/home/claude/v3/edits/*.json')):
        log += [e for e in json.load(open(f, encoding='utf-8')) if e.get('page') == fn]
    for e in log:
        if e['field'] == 'text':
            # inside the body only, never inside scripts: the visible text as it appears in the markup
            body_i = h.index('<body'); pre, body = h[:body_i], h[body_i:]
            if e['from'] in body: body = body.replace(e['from'], e['to'], 1); h = pre + body
            else: MISS.append((fn, e['from'][:60]))
        elif e['field'] == 'title':
            h, n = re.subn(r'<title>.*?</title>', '<title>' + _h.escape(e['to'], quote=False) + '</title>', h, count=1, flags=re.S)
        elif e['field'] == 'description':
            h, n = re.subn(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + _h.escape(e['to']) + m.group(2), h, count=1)
    logjs = json.dumps(log, ensure_ascii=False, indent=1).replace('<', '\\u003c')
    h = h.replace(mark, '<script type="application/json" id="dx-edits">' + logjs + '</script>\n<script id="dx-editor">\n' + ED + '\n</script>\n' + mark)
    assert 'assets/' not in h, (fn, re.findall(r'assets/[\w.-]+', h))
    open(f'{O}/{fn}', 'w', encoding='utf-8').write(h)
    print(fn, round(len(h) / 1024), 'KB')
if MISS:
    print('EDITS THAT NO LONGER MATCH THE SOURCE (the text was changed since):')
    for m in MISS: print('  ', m)
