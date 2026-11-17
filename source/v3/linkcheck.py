"""Every link on every page goes somewhere real. usage: python3 -I linkcheck.py <siteDir>"""
import sys, os, re, collections
S = sys.argv[1]; pages = sorted(f for f in os.listdir(S) if f.endswith('.html'))
ids = {p: set(re.findall(r'\sid="([^"]+)"', open(f'{S}/{p}', encoding='utf-8').read())) for p in pages}
bad, inbound, out = [], collections.Counter(), {}
for p in pages:
    h = open(f'{S}/{p}', encoding='utf-8').read()
    h = re.sub(r'<script.*?</script>', '', h, flags=re.S)
    hrefs = re.findall(r'<a\b[^>]*\shref="([^"]+)"', h); out[p] = set()
    for u in hrefs:
        if u.startswith(('tel:', 'mailto:', 'http')): continue
        f, _, frag = u.partition('#'); f = f or p
        if f not in ids: bad.append((p, u, 'no such page')); continue
        if frag and frag not in ids[f]: bad.append((p, u, 'no such section')); continue
        if f != p: inbound[f] += 1; out[p].add(f)
print('pages:', len(pages)); print('broken:', bad or 'none')
for p in pages: print(f'  {p:22s} links in from {inbound[p]:3d} places · links out to: {", ".join(sorted(x[:-5] for x in out[p]))}')
