"""Measure every page of the multi-page site against the mobile checklist. usage: python3 -I audit.py <siteDir> [W H]"""
import pathlib, json, sys
from playwright.sync_api import sync_playwright
SITE=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 390; H=int(sys.argv[3]) if len(sys.argv)>3 else 844
FD='/home/claude/fonts/node_modules/@fontsource'; CSS=pathlib.Path('/home/claude/review/fonts.css').read_text()
M=r"""() => {
  const vis=(el)=>{const r=el.getBoundingClientRect(),s=getComputedStyle(el);return r.width>0&&r.height>0&&s.visibility!=='hidden'&&s.display!=='none'&&!el.closest('[hidden]')&&!el.closest('#intro');};
  const out={overflow:document.documentElement.scrollWidth-innerWidth,small:[],tiny:{},body15:{},blur:0,inputs:[]};
  document.querySelectorAll('a,button,input,textarea,select,summary').forEach(el=>{if(!vis(el))return;const r=el.getBoundingClientRect();if(r.height<44||r.width<44)out.small.push([el.tagName.toLowerCase()+'.'+String(el.className).split(' ')[0],(el.getAttribute('aria-label')||el.textContent).trim().slice(0,24),Math.round(r.width),Math.round(r.height)]);});
  document.querySelectorAll('body *').forEach(el=>{if(!vis(el)||el.closest('svg'))return;if(![...el.childNodes].some(n=>n.nodeType===3&&n.textContent.trim().length>1))return;const s=getComputedStyle(el),fs=parseFloat(s.fontSize);const k=el.tagName.toLowerCase()+'.'+String(el.className).split(' ')[0]+' '+fs;
    if(fs<12)out.tiny[k]=el.textContent.trim().slice(0,24); else if(fs<16&&el.textContent.trim().length>48&&!/mono/.test(el.className))out.body15[k]=el.textContent.trim().slice(0,24);});
  document.querySelectorAll('*').forEach(el=>{const b=getComputedStyle(el).backdropFilter;if(b&&b!=='none'&&vis(el))out.blur++;});
  document.querySelectorAll('input,textarea').forEach(el=>{if(vis(el))out.inputs.push([el.id||el.className,el.type,el.inputMode,parseFloat(getComputedStyle(el).fontSize),el.autocomplete]);});
  return out;}"""
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    c=b.new_context(viewport={'width':W,'height':H},device_scale_factor=2,is_mobile=True,has_touch=True)
    c.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=CSS)); c.route('https://fonts.gstatic.com/**',lambda r:r.abort())
    c.route('https://local.fonts/**',lambda r:r.fulfill(status=200,content_type='font/woff2',body=pathlib.Path(FD+'/'+r.request.url.split('local.fonts/')[1]).read_bytes()))
    c.add_init_script("try{localStorage.setItem('dots-intro-v4','1')}catch(e){}")
    for pgname in sorted(f[:-5] for f in __import__('os').listdir(SITE) if f.endswith('.html')):
        pg=c.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto(f'file://{SITE}/{pgname}.html'); pg.wait_for_timeout(1500)
        r=pg.evaluate(M); r['errors']=errs
        print('=== ',pgname, W,'x',H); print(json.dumps(r,ensure_ascii=False,indent=0)[:2200])
        pg.close()
    b.close()
