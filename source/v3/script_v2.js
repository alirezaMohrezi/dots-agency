
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const ease = (t) => 1 - Math.pow(1 - clamp(t), 3);
  const easeIO = (t) => { t = clamp(t); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
  const smooth = (a, b, x) => { const t = clamp((x - a) / (b - a)); return t * t * (3 - 2 * t); };
  const MOB = matchMedia('(max-width: 860px)');

  {{INTRO_JS}}

  /* ───── hero: Milky Way + construction grid + two hands; scroll closes the gap, the meeting point becomes a sun ─────
     Art direction: the hands are never cropped. Each size computes the largest scale at which both hands (wrists included)
     fit in the band between the header and the copy; forearms may run off the frame, fingers and palms never do.
     The copy sits on a solid night band below that, so no line, label or star runs under text. */
  const hero = $('#hero'), cv = $('#sky'), ctx = cv.getContext('2d'), gapRead = $('#gapRead'), cue = $('#cue'), stageEl = $('.stage'), copyEl = $('#heroCopy');
  const human = new Image(), ai = new Image();
  {{HAND_SRC}}
  const FW = 1600, FH = 914, P = [832, 446], TIP_AI = [796, 437], TIP_HU = [868, 455];
  const BOX = { l: 262, r: 1380, t: 270, b: 722 };           // both hands, wrists included (frame units)
  let W, H, DPR, S, O, U, cx, cy, startGap, galaxy = null;
  function size() {
    if (!cv.clientWidth || !cv.clientHeight) return;
    DPR = Math.min(innerWidth < 860 ? 1.5 : 2, devicePixelRatio || 1); W = cv.clientWidth; H = cv.clientHeight;
    cv.width = Math.round(W * DPR); cv.height = Math.round(H * DPR);
    const narrow = W < 860;
    startGap = narrow ? 44 : 108;
    const sr = stageEl.getBoundingClientRect(), hb = $('#top').getBoundingClientRect().bottom;
    const copyTop = copyEl.getBoundingClientRect().top - sr.top;
    const top = Math.max(0, hb - Math.max(0, sr.top)) + (narrow ? 58 : 24), bot = copyTop - (narrow ? 12 : 20), side = narrow ? 8 : 48;
    // vertical room the drawing needs around the meeting point at scale s: the hands, the labels above, the gap ruler below
    const up = (s) => Math.max((P[1] - BOX.t) * s, 144 * s + 46), down = (s) => Math.max((BOX.b - P[1]) * s, 187 * s + 22);
    const wide = (s) => (BOX.r - BOX.l + 2 * startGap) * s;
    let lo = .08, hi = narrow ? .6 : .8;
    for (let i = 0; i < 28; i++) { const m = (lo + hi) / 2; if (wide(m) <= W - 2 * side && up(m) + down(m) <= bot - top) lo = m; else hi = m; }
    S = lo; U = (TIP_HU[0] - TIP_AI[0]) * S;
    const L = (P[0] - BOX.l + startGap) * S, R = (BOX.r - P[0] + startGap) * S;
    cx = (W - (L + R)) / 2 + L;
    cy = top + Math.max(0, (bot - top) - (up(S) + down(S))) / 2 + up(S);
    O = [cx - P[0] * S, cy - P[1] * S];
    stageEl.style.setProperty('--scrimH', Math.max(0, H - copyTop + 10) + 'px');
    galaxy = buildGalaxy();
  }

  // the Milky Way: a tilted band of dense stars, soft gas and dark dust lanes — drawn once per size
  function buildGalaxy() {
    const c = document.createElement('canvas'); c.width = cv.width; c.height = cv.height;
    const g = c.getContext('2d'); g.scale(DPR, DPR);
    let seed = 42; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    const gauss = () => { let u = 0; for (let i = 0; i < 4; i++) u += rnd(); return (u - 2) / 2; };
    const ang = -.32, ca = Math.cos(ang), sa = Math.sin(ang);
    const L = Math.hypot(W, H) * .65, bw = Math.max(W, H) * (W < 860 ? .2 : .13);
    const at = (u, v) => [cx + u * ca - v * sa, cy + u * sa + v * ca];
    g.globalCompositeOperation = 'lighter';
    for (let i = 0; i < 220; i++) {
      const u = (rnd() * 2 - 1) * L, v = gauss() * bw * .7, [x, y] = at(u, v), core = 1 - Math.min(1, Math.abs(u) / L);
      const r = bw * (.35 + rnd() * .9), a = (.012 + .03 * core) * (1 - Math.min(1, Math.abs(v) / (bw * 1.6)));
      const pick = rnd(); const col = pick < .55 ? `255,226,170` : pick < .78 ? `212,175,55` : pick < .9 ? `0,110,98` : `121,30,35`;
      const gr = g.createRadialGradient(x, y, 0, x, y, r); gr.addColorStop(0, `rgba(${col},${a})`); gr.addColorStop(1, `rgba(${col},0)`);
      g.fillStyle = gr; g.beginPath(); g.arc(x, y, r, 0, 6.2832); g.fill();
    }
    const n = Math.round((W * H) / 260);
    for (let i = 0; i < n; i++) {
      const inBand = rnd() < .72, u = (rnd() * 2 - 1) * L * 1.1, v = inBand ? gauss() * bw * .55 : (rnd() * 2 - 1) * Math.max(W, H);
      const [x, y] = at(u, v); if (x < 0 || y < 0 || x > W || y > H) continue;
      const m = rnd(), r = m > .985 ? 1.3 + rnd() * .8 : m > .9 ? .8 : .45;
      const tone = rnd(); g.fillStyle = tone < .7 ? `rgba(249,245,236,${.25 + rnd() * .6})` : tone < .9 ? `rgba(255,226,170,${.3 + rnd() * .5})` : `rgba(159,245,232,${.25 + rnd() * .4})`;
      g.beginPath(); g.arc(x, y, r, 0, 6.2832); g.fill();
    }
    g.globalCompositeOperation = 'source-over';
    for (let i = 0; i < 70; i++) {
      const u = (rnd() * 2 - 1) * L * .9, v = gauss() * bw * .18, [x, y] = at(u, v), r = bw * (.12 + rnd() * .3);
      const gr = g.createRadialGradient(x, y, 0, x, y, r); gr.addColorStop(0, 'rgba(8,9,9,.32)'); gr.addColorStop(1, 'rgba(8,9,9,0)');
      g.save(); g.translate(x, y); g.rotate(ang); g.scale(2.6, .6); g.translate(-x, -y); g.fillStyle = gr; g.beginPath(); g.arc(x, y, r, 0, 6.2832); g.fill(); g.restore();
    }
    return c;
  }
  const TW = []; { let s = 9; const r = () => (s = (s * 16807) % 2147483647) / 2147483647; for (let i = 0; i < 70; i++) TW.push([r(), r(), r() * 6.28, .6 + r()]); }
  const line = (x0, y0, x1, y1) => { ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke(); };
  const mono = (txt, x, y, a, align) => { ctx.font = `500 11px "DM Mono", monospace`; ctx.textAlign = align; ctx.fillStyle = `rgba(249,245,236,${a})`; ctx.fillText(txt, x, y); };
  const faTxt = (txt, x, y, a, align) => { ctx.font = `500 14px Estedad, Tahoma, sans-serif`; ctx.textAlign = align; ctx.direction = 'rtl'; ctx.fillStyle = `rgba(249,245,236,${a})`; ctx.fillText(txt, x, y); ctx.direction = 'ltr'; };

  let p = 0, pShown = 0, paused = RM, t0 = performance.now(), tStop = 0, mx = 0, my = 0, tmx = 0, tmy = 0, heroOn = true, lastGap = '';
  addEventListener('pointermove', (e) => { if (e.pointerType === 'mouse') { tmx = e.clientX / innerWidth - .5; tmy = e.clientY / innerHeight - .5; } }, { passive: true });
  function readScroll() {
    const r = hero.getBoundingClientRect(), span = r.height - innerHeight;
    p = RM ? .6 : clamp(-r.top / Math.max(1, span));
    cue.style.opacity = String(1 - smooth(.02, .15, p));
  }
  /* scroll phases: 0–.42 the hands close the gap · .2–.62 the meeting point swells into a sun · .62–1 the camera flies into it */
  function render(t) {
    pShown += (p - pShown) * (RM ? 1 : .14);
    mx += (tmx - mx) * .05; my += (tmy - my) * .05;
    const q = pShown, close = easeIO(q / .42), sun = smooth(.2, .62, q), dive = smooth(.62, .86, q), intro = RM ? 1 : ease(t / 1.6);
    const Z = Math.exp(Math.pow(dive, 1.6) * Math.log(60));
    const white = smooth(.78, .9, q) * .82 + smooth(.95, .995, q) * .18;
    const ui = 1 - smooth(.55, .68, q);
    stageEl.style.setProperty('--ui', ui.toFixed(3)); stageEl.style.setProperty('--uivis', ui < .02 ? 'hidden' : 'visible');
    const wel = RM ? 0 : smooth(.8, .86, q) * (1 - smooth(.95, .995, q)); stageEl.style.setProperty('--wel', wel.toFixed(3));
    const breathe = RM || paused ? 0 : (Math.sin(t * .8) * .5 + .5) * (1 - close * .6);
    const gap = startGap * (1 - close) + breathe * 4;
    const cam = () => ctx.setTransform(DPR * Z, 0, 0, DPR * Z, DPR * cx * (1 - Z), DPR * cy * (1 - Z));
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = '#0B0C0C'; ctx.fillRect(0, 0, cv.width, cv.height);
    cam();
    ctx.globalAlpha = intro; ctx.drawImage(galaxy, 0, 0, W, H); ctx.globalAlpha = 1;
    if (!RM) for (const [u, v, ph, sz] of TW) { const a = .25 + .55 * (Math.sin(t * 1.3 + ph * 4) * .5 + .5); ctx.fillStyle = `rgba(249,245,236,${a * intro})`; ctx.beginPath(); ctx.arc(u * W, v * H, sz / Z, 0, 6.2832); ctx.fill(); }
    ctx.globalCompositeOperation = 'lighter';
    let g = ctx.createRadialGradient(cx, cy, 0, cx, cy, Math.max(W, H) * (.25 + .6 * sun));
    g.addColorStop(0, `rgba(255,214,140,${.08 + .4 * sun})`); g.addColorStop(.3, `rgba(212,175,55,${.04 + .16 * sun})`); g.addColorStop(1, 'rgba(212,175,55,0)');
    ctx.fillStyle = g; ctx.fillRect(cx - W * 2, cy - H * 2, W * 4, H * 4);
    ctx.globalCompositeOperation = 'source-over';
    const cons = 1 - dive;
    ctx.lineWidth = 1 / Z; ctx.strokeStyle = `rgba(249,245,236,${.045 * cons})`;
    for (let x = cx - Math.ceil(cx / U) * U; x < W; x += U) line(x, 0, x, H);
    for (let y = cy - Math.ceil(cy / U) * U; y < H; y += U) line(0, y, W, y);
    ctx.strokeStyle = `rgba(249,245,236,${.16 * cons})`; line(0, cy, W, cy); line(cx, 0, cx, H);
    ctx.globalAlpha = intro; ctx.globalCompositeOperation = 'screen';
    ctx.drawImage(ai, O[0] - gap * S - mx * 8, O[1] - my * 5, FW * S, FH * S);
    ctx.drawImage(human, O[0] + gap * S + mx * 8, O[1] + my * 5, FW * S, FH * S);
    ctx.globalCompositeOperation = 'source-over'; ctx.globalAlpha = 1;
    const a0 = [O[0] + TIP_AI[0] * S - gap * S - mx * 8, O[1] + TIP_AI[1] * S - my * 5];
    const h0 = [O[0] + TIP_HU[0] * S + gap * S + mx * 8, O[1] + TIP_HU[1] * S + my * 5];
    const R2 = 2 * U, gu = (h0[0] - a0[0]) / U, sheet = ui;
    if (sheet > .01) {
      ctx.globalAlpha = sheet;
      ctx.strokeStyle = 'rgba(249,245,236,.4)';
      for (const pt of [a0, h0]) { ctx.beginPath(); ctx.arc(pt[0], pt[1], R2, 0, 6.2832); ctx.stroke(); }
      ctx.save(); ctx.setLineDash([3, 6]); ctx.strokeStyle = `rgba(249,245,236,${.15 + .35 * close})`; ctx.beginPath(); ctx.arc(cx, cy, R2 * 1.5, 0, 6.2832); ctx.stroke(); ctx.restore();
      const dy = cy + R2 + U * .6; ctx.strokeStyle = 'rgba(249,245,236,.5)';
      line(a0[0], dy, h0[0], dy); line(a0[0], dy - 5, a0[0], dy + 5); line(h0[0], dy - 5, h0[0], dy + 5);
      const gtxt = 'GAP ' + (gu < 1.05 ? '1u' : gu.toFixed(1) + 'u');
      mono(gtxt, cx, dy + 17, .75, 'center');
      if (gtxt !== lastGap) { lastGap = gtxt; gapRead.textContent = gtxt; }
      const lx = R2 * .15, ly = Math.min(a0[1], h0[1]) - R2 - 14;
      mono('AI · AUTOMATION', a0[0] - lx, ly, .7, 'right'); faTxt('هوش مصنوعی', a0[0] - lx, ly - 19, .92, 'right');
      mono('HUMAN · EXPERIENCE', h0[0] + lx, ly, .7, 'left'); faTxt('تجربه‌ی انسانی', h0[0] + lx, ly - 19, .92, 'left');
      for (const pt of [a0, h0]) { ctx.fillStyle = '#0B0C0C'; ctx.strokeStyle = 'rgba(249,245,236,.9)'; ctx.beginPath(); ctx.arc(pt[0], pt[1], 3.5, 0, 6.2832); ctx.fill(); ctx.stroke(); }
      ctx.globalAlpha = 1;
    }
    const pulse = RM || paused ? 1 : 1 + .04 * Math.sin(t * 2.2);
    const core = U * (.12 + .55 * sun) * pulse;
    ctx.globalCompositeOperation = 'lighter';
    g = ctx.createRadialGradient(cx, cy, 0, cx, cy, core * 6);
    g.addColorStop(0, `rgba(255,240,190,${.5 + .4 * sun})`); g.addColorStop(.18, `rgba(255,206,110,${.25 + .35 * sun})`); g.addColorStop(.5, `rgba(212,175,55,${.08 + .12 * sun})`); g.addColorStop(1, 'rgba(212,175,55,0)');
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, core * 6, 0, 6.2832); ctx.fill();
    const rot = RM ? 0 : t * .08; ctx.strokeStyle = `rgba(255,226,150,${(.12 + .4 * sun) * (1 - dive * .7)})`;
    for (let i = 0; i < 24; i++) { const a = rot + i * Math.PI / 12, r0 = core * 1.25, r1 = core * (i % 2 ? 2.1 : 3.2) * (1 + .3 * sun); line(cx + Math.cos(a) * r0, cy + Math.sin(a) * r0, cx + Math.cos(a) * r1, cy + Math.sin(a) * r1); }
    ctx.globalCompositeOperation = 'source-over';
    g = ctx.createRadialGradient(cx - core * .25, cy - core * .25, 0, cx, cy, core);
    g.addColorStop(0, '#FFF8E2'); g.addColorStop(.6, '#FFE29A'); g.addColorStop(1, '#E8BE4A');
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, core, 0, 6.2832); ctx.fill();
    if (white > 0) { ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.fillStyle = `rgba(249,245,236,${white})`; ctx.fillRect(0, 0, cv.width, cv.height); }
  }
  let raf = 0, ready = false;
  function loop(now) { raf = 0; if (!heroOn) return; const t = paused ? tStop : (now - t0) / 1000; render(t); if (!paused || Math.abs(p - pShown) > .001) raf = requestAnimationFrame(loop); }
  const kick = () => { if (ready && !raf && heroOn) raf = requestAnimationFrame(loop); };
  addEventListener('scroll', () => { readScroll(); kick(); }, { passive: true });
  let rw = innerWidth, rh = innerHeight;
  addEventListener('resize', () => { if (!ready) return;
    const urlBar = innerWidth === rw && Math.abs(innerHeight - rh) < 160 && innerWidth < 860;   // phones resize when the address bar slides
    if (!urlBar) { rw = innerWidth; rh = innerHeight; size(); } readScroll(); kick(); });
  new IntersectionObserver(([e]) => { heroOn = e.isIntersecting; kick(); }).observe(hero);
  const pb = $('#pause'), pi = $('#pauseIcon');
  const setIcon = () => { pi.setAttribute('d', paused ? 'M3 2l9 5-9 5z' : 'M3 2h3v10H3zM8 2h3v10H8z'); pb.setAttribute('aria-pressed', paused); pb.setAttribute('aria-label', paused ? 'ادامه‌ی حرکت' : 'توقف حرکت'); };
  pb.addEventListener('click', () => { if (paused) { t0 = performance.now() - tStop * 1000; paused = false; } else { tStop = (performance.now() - t0) / 1000; paused = true; } setIcon(); kick(); });
  window.__hero = (pp, t) => { if (!ready) return; p = pp; pShown = pp; render(t); };
  Promise.all([human.decode().catch(() => {}), ai.decode().catch(() => {}), document.fonts ? document.fonts.ready : 0]).then(() => {
    size(); ready = true; readScroll(); pShown = p; tStop = 10; setIcon(); t0 = performance.now(); kick();
  });
  if (document.fonts) document.fonts.addEventListener('loadingdone', () => { if (ready) { size(); kick(); } });

  /* ───── blocks & steps chart, approach diamonds ───── */
  const NS = 'http://www.w3.org/2000/svg';
  function diamonds(box) {
    // three phases, each wider than the last; each opens (diverge) then closes (converge); outputs are wine dots at the joints
    const PH = [['شناخت مسئله', 'UNDERSTAND', 'بیان مسئله'], ['ساختاربندی', 'STRUCTURE', 'مسئله‌ی اصلی'], ['توسعه‌ی راه‌حل', 'SOLVE', 'راهکار']];
    const len = [150, 210, 290], half = [44, 60, 80];
    // horizontal (RTL: the flow starts on the right)
    let x = 1000 - 30, h = `<svg class="h" viewBox="0 0 1000 250" role="img" aria-label="سه مرحله پشت سر هم، از راست به چپ؛ هر مرحله یک بار باز و یک بار جمع می‌شود و در پایان هر مرحله یک خروجی هست">`;
    const cyH = 120; h += `<line class="flow" x1="20" y1="${cyH}" x2="980" y2="${cyH}" stroke-dasharray="2 5"/>`;
    PH.forEach((ph, i) => { const x0 = x, x1 = x - len[i], xm = (x0 + x1) / 2, hh = half[i];
      h += `<polygon class="shape${i === 2 ? ' on' : ''}" points="${x0},${cyH} ${xm},${cyH - hh} ${x1},${cyH} ${xm},${cyH + hh}"/><line class="mid" x1="${xm}" y1="${cyH - hh}" x2="${xm}" y2="${cyH + hh}"/>`;
      h += `<text class="tm" x="${xm}" y="${cyH - hh - 34}" text-anchor="middle" direction="ltr">0${i + 1} · ${ph[1]}</text><text class="t" x="${xm}" y="${cyH - hh - 12}" text-anchor="middle" direction="rtl">${ph[0]}</text>`;
      h += `<circle class="out" cx="${x1}" cy="${cyH}" r="7"/><text class="ts" x="${x1}" y="${cyH + 30 + (i === 2 ? 0 : 0)}" text-anchor="middle" direction="rtl">${ph[2]}</text>`;
      x = x1 - 40; });
    h += `<text class="ts" x="${1000 - 24}" y="${cyH + 30}" text-anchor="start" direction="rtl">شروع</text></svg>`;
    // phones: the same flow, simplified into one compact row; the phase names live in the numbered list below
    const sc = .33, gp = 14, lens = len.map((l) => l * sc), tot = lens.reduce((a, b) => a + b, 0) + gp * 2 + 36, vb = Math.ceil(tot + 24);
    let xv = vb - 12, cyV = 64, v = `<svg class="v" viewBox="0 0 ${vb} 132" role="img" aria-label="سه مرحله پشت سر هم، از راست به چپ؛ هر مرحله یک بار باز و یک بار جمع می‌شود و در پایان هر مرحله یک خروجی هست">`;
    v += `<line class="flow" x1="4" y1="${cyV}" x2="${vb - 4}" y2="${cyV}" stroke-dasharray="2 5"/><circle cx="${xv}" cy="${cyV}" r="3.5" fill="#141615"/>`;
    xv -= 18;
    PH.forEach((ph, i) => { const x0 = xv, x1 = xv - lens[i], xm = (x0 + x1) / 2, hh = half[i] * .55;
      v += `<polygon class="shape${i === 2 ? ' on' : ''}" points="${x0},${cyV} ${xm},${cyV - hh} ${x1},${cyV} ${xm},${cyV + hh}"/><line class="mid" x1="${xm}" y1="${cyV - hh}" x2="${xm}" y2="${cyV + hh}"/>`;
      v += `<text class="tm" x="${xm}" y="${cyV - hh - 10}" text-anchor="middle" direction="ltr">0${i + 1}</text><circle class="out" cx="${x1}" cy="${cyV}" r="5"/>`;
      xv = x1 - gp; });
    v += `<text class="ts" x="${vb - 6}" y="${cyV + 46}" text-anchor="start" direction="rtl">شروع</text><text class="ts" x="${xv + gp - 2}" y="${cyV + 58}" text-anchor="middle" direction="rtl">راهکار</text></svg>`;
    box.innerHTML = h + v;
  }
  $$('[data-dia]').forEach(diamonds);
  // vertical labels are anchored "end" in an RTL svg; fix anchors for LTR mono text by direction attribute above

  /* reveal once, < 500ms; the bars grow the first time they are seen */
  const rvObs = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); rvObs.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  const watchReveals = (root) => $$('.rv, .reveal-bars', root).forEach((el) => rvObs.observe(el));
  watchReveals(document);

  /* ───── views: the visitor chooses a path (#/capabilities · #/work · #/approach); home anchors still work ───── */
  const views = { '': $('#v-home'), capabilities: $('#v-capabilities'), work: $('#v-work'), approach: $('#v-approach') };
  let current = '';
  function route(first) {
    const h = location.hash, m = h.match(/^#\/(\w+)/), name = m && views[m[1]] ? m[1] : '';
    if (name !== current || first) {
      Object.entries(views).forEach(([k, el]) => el.classList.toggle('on', k === name));
      current = name; document.title = views[name].dataset.title;
      if (name) { scrollTo(0, 0); const h1 = $('h1', views[name]); h1 && h1.focus({ preventScroll: true }); watchReveals(views[name]); }
      if (!name && ready) { size(); kick(); }
      navState(); solid(); bar();
    }
    if (!name && h && h.length > 1 && !first) { const t = document.getElementById(h.slice(1)); if (t) t.scrollIntoView({ behavior: RM ? 'auto' : 'smooth' }); }
  }
  addEventListener('hashchange', () => route(false));
  // a home anchor while a path view is open returns home first, then scrolls
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="#"]'); if (!a) return;
    const href = a.getAttribute('href');
    const t = href.length > 1 && !href.startsWith('#/') ? document.getElementById(href.slice(1)) : null;
    if (t && current && views[''].contains(t)) { e.preventDefault(); history.pushState(null, '', href); route(true); requestAnimationFrame(() => t.scrollIntoView()); }
  });

  /* ───── header, menu, bottom bar ───── */
  const top = $('#top'), mb = $('#menuBtn'), sheet = $('#sheetMenu'), scrim = $('#scrim'), mbar = $('#mbar'), contactSec = $('#contact'), theme = $('meta[name=theme-color]');
  const solid = () => { const on = !!current || hero.getBoundingClientRect().bottom < 80 || (!RM && p > (MOB.matches ? .5 : .8));
    top.classList.toggle('solid', on); const c = on ? '#F9F5EC' : '#0B0C0C'; if (theme.content !== c) theme.content = c; };
  addEventListener('scroll', solid, { passive: true });
  const inline = new Set();
  const ctaObs = new IntersectionObserver((es) => { es.forEach((e) => e.isIntersecting ? inline.add(e.target) : inline.delete(e.target)); bar(); });
  $$('.next-step, .vcta, .paths').forEach((el) => ctaObs.observe(el));
  function bar() {
    const past = !!current || hero.getBoundingClientRect().bottom < innerHeight * .5, atContact = contactSec.getBoundingClientRect().top < innerHeight * .75;
    const vis = [...inline].some((el) => el.offsetParent !== null);
    const on = past && !atContact && !vis && !document.body.classList.contains('menu-on'); mbar.classList.toggle('show', on); mbar.inert = !on;
  }
  addEventListener('scroll', bar, { passive: true });
  const setMenu = (o) => { sheet.hidden = !o; scrim.hidden = !o; document.body.classList.toggle('menu-on', o);
    mb.setAttribute('aria-expanded', o); mb.setAttribute('aria-label', o ? 'بستن منو' : 'باز کردن منو'); $('#menuIcon').setAttribute('d', o ? 'M6 6l12 12M18 6L6 18' : 'M4 8h16M4 16h16');
    if (o) { top.classList.add('solid'); $('a', sheet).focus({ preventScroll: true }); } else solid(); bar(); };
  mb.addEventListener('click', () => setMenu(sheet.hidden));
  scrim.addEventListener('click', () => setMenu(false));
  sheet.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && !sheet.hidden) { setMenu(false); mb.focus(); } });
  function navState() {
    $$('.nav a, .sheet-menu a.row').forEach((a) => { const h = a.getAttribute('href'); if (h === '#/' + current && current) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
  }

  /* ───── contact form: short, checked in place; on phones send by SMS or email ───── */
  const f = $('#form'), nm = $('#f-name'), ct = $('#f-ct'), co = $('#f-co'), msg = $('#f-msg'), st = $('#status');
  const err = (inp, m) => { $('#' + inp.id + '-err').textContent = m; inp.setAttribute('aria-invalid', m ? 'true' : 'false'); };
  [nm, ct].forEach((inp) => inp.addEventListener('input', () => { if (inp.getAttribute('aria-invalid') === 'true') err(inp, ''); }));
  const PHONE = matchMedia('(max-width: 860px), (pointer: coarse)').matches;
  const toEn = (v) => v.replace(/[۰-۹]/g, (d) => '۰۱۲۳۴۵۶۷۸۹'.indexOf(d)).replace(/[٠-٩]/g, (d) => '٠١٢٣٤٥٦٧٨٩'.indexOf(d));
  if (PHONE) {
    ct.type = 'tel'; ct.inputMode = 'tel'; ct.dir = 'ltr'; ct.placeholder = '۰۹۱۲ ۳۴۵ ۶۷۸۹';
    $('#f-ct-l').textContent = 'شماره موبایل *';
    $('.form-note').textContent = 'بعد از «ارسال درخواست» انتخاب می‌کنید با پیامک بفرستید یا ایمیل؛ متن آماده است.';
  }
  const checkCt = (c) => PHONE ? toEn(c).replace(/\D/g, '').length >= 10 : (/^\S+@\S+\.\S+$/.test(c) || toEn(c).replace(/\D/g, '').length >= 10);
  const ctMsg = PHONE ? 'شماره موبایل را کامل بنویسید؛ مثلاً ⁦۰۹۱۲ ۳۴۵ ۶۷۸۹⁩.' : 'یک شماره تماس (دست‌کم ۱۰ رقم) یا ایمیل معتبر بنویسید.';
  ct.addEventListener('blur', () => { const c = ct.value.trim(); if (c && !checkCt(c)) err(ct, ctMsg); });
  f.addEventListener('submit', (e) => {
    e.preventDefault();
    const n = nm.value.trim(), c = ct.value.trim(), okC = checkCt(c);
    err(nm, n ? '' : 'لطفاً نامتان را بنویسید.'); err(ct, okC ? '' : ctMsg);
    if (!n) return nm.focus(); if (!okC) return ct.focus();
    const body = ['درخواست جلسه‌ی مشاوره از سایت DOT’s', '', 'نام: ' + n, 'راه تماس: ' + c, 'کسب‌وکار و حوزه: ' + (co.value.trim() || '—'), '', 'چالش اصلی:', msg.value.trim() || '—'].join('\n');
    const mail = 'mailto:alireza.mohrezi1991@gmail.com?subject=' + encodeURIComponent('درخواست جلسه‌ی مشاوره · ' + n) + '&body=' + encodeURIComponent(body);
    if (PHONE) {
      const sms = ['درخواست جلسه‌ی DOT’s', n + (co.value.trim() ? ' · ' + co.value.trim() : ''), 'تماس: ' + toEn(c), msg.value.trim()].filter(Boolean).join('\n');
      const sep = /iP(hone|ad|od)/.test(navigator.userAgent) ? '&' : '?';
      let box = $('#send'); if (!box) { box = document.createElement('div'); box.id = 'send'; box.className = 'send'; box.tabIndex = -1; st.before(box); }
      box.innerHTML = '<p>درخواست آماده است. از کدام راه بفرستیم؟</p><div class="row2"><a class="btn btn-primary" id="sendSms">ارسال با پیامک</a><a class="btn btn-line" id="sendMail">ارسال با ایمیل</a></div><small>یا همین حالا تماس بگیرید: <a href="tel:+989132289608" dir="ltr">۰۹۱۳ ۲۲۸ ۹۶۰۸</a></small>';
      $('#sendSms').href = 'sms:+989132289608' + sep + 'body=' + encodeURIComponent(sms); $('#sendMail').href = mail;
      st.classList.add('sr-only'); st.textContent = 'درخواست آماده شد. یکی از دو راه ارسال را انتخاب کنید.'; box.focus();
      return;
    }
    location.href = mail;
    st.textContent = 'متن درخواست در برنامه‌ی ایمیل شما آماده شد؛ فقط «ارسال» را بزنید. اگر برنامه‌ای باز نشد، با ۰۹۱۳ ۲۲۸ ۹۶۰۸ تماس بگیرید.';
  });

  route(true); solid(); bar();
})();
