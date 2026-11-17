"""Read the change list (#dx-edits) out of pages the owner edited and saved, into edits/<page>.json.
usage: python3 -I import_edits.py <edited.html> [more.html ...]"""
import sys, json, re, os, html
for f in sys.argv[1:]:
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<script type="application/json" id="dx-edits">(.*?)</script>', s, re.S)
    if not m: print(f, '— no change list in this file'); continue
    log = json.loads(m.group(1).replace('\\u003c', '<'))
    by = {}
    for e in log: by.setdefault(e['page'], []).append(e)
    for page, entries in by.items():
        out = f'/home/claude/v3/edits/{page[:-5]}.json'
        old = json.load(open(out, encoding='utf-8')) if os.path.exists(out) else []
        keyed = {(e['field'], e['from']): e for e in old}
        for e in entries: keyed[(e['field'], e['from'])] = e
        json.dump(list(keyed.values()), open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f, '→', out, len(entries), 'changes')
        for e in entries: print('   ', e['field'], ':', html.unescape(re.sub('<[^>]+>', '', e['from']))[:50], '→', html.unescape(re.sub('<[^>]+>', '', e['to']))[:50])
