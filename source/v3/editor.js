/* DOT’s · edit mode: change the page's words in the browser and save the page as a new file.
   Shows on its own when the file is opened from the computer; on the live site, add ?edit to the address.
   The saved file is the original page with only the edited words changed (nothing the scripts did at runtime),
   and it keeps a running list of every change (#dx-edits), so the people building the site can carry the same
   wording into the source and nothing is lost on the next build. */
(() => {
  'use strict';
  const me = document.currentScript;
  const SKIP = 'script,style,noscript,svg,canvas,textarea,input,select,option,.intro,#intro,.dx-bar';
  // mark every element that holds words of its own, outermost only, before any other script touches the page
  let n = 0;
  for (const el of document.body.querySelectorAll('*')) {
    if (el.closest(SKIP) || (el.parentElement && el.parentElement.closest('[data-k]'))) continue;
    if ([...el.childNodes].some((c) => c.nodeType === 3 && c.textContent.trim())) el.setAttribute('data-k', String(++n));
  }
  const snap = document.documentElement.cloneNode(true);   // the page as written, up to this script
  const show = location.protocol === 'file:' || /[?&#]edit\b/.test(location.href);
  if (!show) return;

  const edited = new Set(); let on = false, headDirty = false;
  const css = document.createElement('style');
  css.textContent = `
.dx-bar{position:fixed;z-index:300;pointer-events:none;left:max(16px,env(safe-area-inset-left));bottom:calc(16px + env(safe-area-inset-bottom));display:flex;flex-direction:column;align-items:flex-start;gap:8px;font-family:Estedad,Tahoma,sans-serif;direction:rtl}
.dx-bar.dx-right{left:auto;right:max(16px,env(safe-area-inset-right));align-items:flex-end}
.dx-row,.dx-panel{pointer-events:auto}
.dx-row{display:flex;flex-wrap:wrap;gap:6px;padding:6px;border-radius:999px;background:rgba(20,22,21,.92);box-shadow:0 10px 30px -10px rgba(0,0,0,.5)}
.dx-bar button{min-height:44px;padding:0 16px;border:0;border-radius:999px;background:rgba(255,255,255,.1);color:#F9F5EC;font:600 15px/1 Estedad,Tahoma,sans-serif;cursor:pointer}
.dx-bar button:hover{background:rgba(255,255,255,.18)}
.dx-bar button[aria-pressed="true"],.dx-bar .dx-save{background:#006E62}
.dx-bar button:focus-visible{outline:2px solid #9FF5E8;outline-offset:2px}
.dx-bar [hidden]{display:none!important}
body.intro-on .dx-bar{display:none}
.dx-panel{width:min(360px,calc(100vw - 32px));padding:14px;border-radius:20px;background:#F9F5EC;color:#141615;box-shadow:0 14px 40px -12px rgba(0,0,0,.45)}
.dx-panel label{display:block;margin:0 0 4px;font-size:13px;font-weight:600;color:#3E4340}
.dx-panel input,.dx-panel textarea{display:block;width:100%;box-sizing:border-box;margin-bottom:10px;padding:10px 12px;border:1px solid #D9D1C1;border-radius:12px;background:#fff;font:400 16px/1.6 Estedad,Tahoma,sans-serif;direction:rtl}
.dx-hint,.dx-msg{max-width:min(360px,calc(100vw - 32px));margin:0;padding:6px 12px;border-radius:12px;background:rgba(20,22,21,.88);color:#F9F5EC;font-size:13px;line-height:1.7}
.dx-msg:empty{display:none}
html.dx-on [data-k]{outline:1px dashed rgba(0,110,98,.55);outline-offset:3px;cursor:text}
html.dx-on [data-k]:hover{outline-style:solid}
html.dx-on [data-k]:focus{outline:2px solid #006E62;outline-offset:3px;background-color:rgba(159,245,232,.18)}
html.dx-on [data-k].dx-changed{outline-color:#791E23}`;
  document.head.appendChild(css);
  const bar = document.createElement('div'); bar.className = 'dx-bar'; bar.setAttribute('translate', 'no');
  bar.innerHTML = `
<div class="dx-panel" id="dx-panel" hidden>
  <label for="dx-title">عنوان صفحه (در تب مرورگر و نتیجه‌ی گوگل)</label><input id="dx-title" type="text">
  <label for="dx-desc">توضیح صفحه (زیر عنوان در نتیجه‌ی گوگل)</label><textarea id="dx-desc" rows="3"></textarea>
</div>
<p class="dx-hint" id="dx-hint" hidden>روی هر متن کلیک کنید و تایپ کنید. متن‌های تغییرکرده قاب قرمز می‌گیرند.</p>
<p class="dx-msg" id="dx-msg" role="status" aria-live="polite"></p>
<div class="dx-row">
  <button type="button" id="dx-toggle" aria-pressed="false">ویرایش متن‌ها</button>
  <button type="button" id="dx-meta" aria-expanded="false" aria-controls="dx-panel" hidden>عنوان و توضیح</button>
  <button type="button" class="dx-save" id="dx-save" hidden>ذخیره‌ی صفحه</button>
  <button type="button" id="dx-side" aria-label="بردن نوار به گوشه‌ی دیگر" title="بردن نوار به گوشه‌ی دیگر">⇆</button>
</div>`;
  document.body.appendChild(bar);
  const $ = (id) => document.getElementById(id), boxes = () => document.querySelectorAll('[data-k]');
  const meta = document.querySelector('meta[name="description"]');
  $('dx-title').value = document.title; $('dx-desc').value = meta ? meta.content : '';
  $('dx-title').addEventListener('input', (e) => { document.title = e.target.value; headDirty = true; });
  $('dx-desc').addEventListener('input', (e) => { if (meta) meta.content = e.target.value; headDirty = true; });
  const plain = (() => { const t = document.createElement('div'); t.contentEditable = 'plaintext-only'; return t.contentEditable === 'plaintext-only'; })();

  function setOn(v) {
    on = v; document.documentElement.classList.toggle('dx-on', on);
    boxes().forEach((el) => { if (on) el.setAttribute('contenteditable', plain ? 'plaintext-only' : 'true'); else el.removeAttribute('contenteditable'); });
    $('dx-toggle').setAttribute('aria-pressed', String(on)); $('dx-toggle').textContent = on ? 'پایان ویرایش' : 'ویرایش متن‌ها';
    $('dx-save').hidden = $('dx-meta').hidden = $('dx-hint').hidden = !on;
    clearTimeout(setOn.t); if (on) setOn.t = setTimeout(() => { $('dx-hint').hidden = true; }, 6000);   // the hint steps aside so it does not cover the page if (!on) { $('dx-panel').hidden = true; $('dx-meta').setAttribute('aria-expanded', 'false'); }
  }
  $('dx-toggle').addEventListener('click', () => setOn(!on));
  $('dx-side').addEventListener('click', () => bar.classList.toggle('dx-right'));
  $('dx-meta').addEventListener('click', () => { const o = $('dx-panel').hidden; $('dx-panel').hidden = !o; $('dx-meta').setAttribute('aria-expanded', String(o)); });
  // while editing: links do not navigate, Enter does not break a line into a new block, pasted text arrives plain
  document.addEventListener('click', (e) => { if (on && e.target.closest('a') && !e.target.closest('.dx-bar')) { e.preventDefault(); e.stopPropagation(); } }, true);
  document.addEventListener('submit', (e) => { if (on) { e.preventDefault(); e.stopPropagation(); } }, true);
  document.addEventListener('keydown', (e) => { if (on && e.key === 'Enter' && e.target.closest && e.target.closest('[data-k]')) e.preventDefault(); }, true);
  document.addEventListener('paste', (e) => { const k = on && e.target.closest && e.target.closest('[data-k]'); if (!k || plain) return; e.preventDefault(); document.execCommand('insertText', false, (e.clipboardData || window.clipboardData).getData('text')); }, true);
  document.addEventListener('input', (e) => { const k = e.target.closest && e.target.closest('[data-k]'); if (on && k) { edited.add(k.getAttribute('data-k')); k.classList.add('dx-changed'); } }, true);
  // the closing "welcome" words only take clicks while they are on screen
  const wel = document.getElementById('welcome'), stage = document.querySelector('.stage');
  if (wel && stage) addEventListener('scroll', () => { wel.style.pointerEvents = on && parseFloat(getComputedStyle(stage).getPropertyValue('--wel') || 0) > .5 ? 'auto' : ''; }, { passive: true });

  $('dx-save').addEventListener('click', () => {
    const out = snap.cloneNode(true);
    // the scripts that come after this one in the page
    const mine = out.querySelector('#dx-editor'); let s = me.nextElementSibling, at = mine;
    while (s) { if (s.tagName === 'SCRIPT') { const c = s.cloneNode(true); at.after(c); at = c; } s = s.nextElementSibling; }
    // the change list: earlier sessions' entries come with the page; a change to a changed text extends its entry
    const logEl = out.querySelector('#dx-edits'); let log = []; try { log = JSON.parse(logEl ? logEl.textContent : '[]') || []; } catch (err) { log = []; }
    const page = decodeURIComponent(location.pathname.split('/').pop() || 'index.html') || 'index.html', when = new Date().toISOString();
    const note = (field, from, to) => { if (from === to) return; const prev = log.find((e) => e.page === page && e.field === field && e.to === from);
      if (prev) { prev.to = to; prev.at = when; } else log.push({ page, field, from, to, at: when }); };
    for (const id of edited) {
      const live = document.querySelector(`[data-k="${id}"]`), dst = out.querySelector(`[data-k="${id}"]`);
      if (!live || !dst) continue;
      const tmp = live.cloneNode(true); tmp.removeAttribute('contenteditable'); tmp.classList.remove('dx-changed');
      tmp.querySelectorAll('br').forEach((b) => b.replaceWith(' '));
      note('text', dst.innerHTML, tmp.innerHTML);
      dst.innerHTML = tmp.innerHTML;
    }
    if (headDirty) {
      const t = out.querySelector('title'); if (t) { note('title', t.textContent, $('dx-title').value); t.textContent = $('dx-title').value; }
      const d = out.querySelector('meta[name="description"]'); if (d) { note('description', d.getAttribute('content'), $('dx-desc').value); d.setAttribute('content', $('dx-desc').value); }
    }
    log = log.filter((e) => e.from !== e.to);
    if (logEl) logEl.textContent = JSON.stringify(log, null, 1).replace(/</g, '\\u003c');
    out.querySelectorAll('[data-k]').forEach((el) => el.removeAttribute('data-k'));
    const html = '<!DOCTYPE html>\n' + out.outerHTML;
    const name = decodeURIComponent(location.pathname.split('/').pop() || 'index.html') || 'index.html';
    const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([html], { type: 'text/html' })); a.download = name;
    bar.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 2000);
    $('dx-msg').textContent = `«${name}» ذخیره شد؛ آن را جای فایل قبلی بگذارید.`;
  });
})();
