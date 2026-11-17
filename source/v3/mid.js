  /* ───── the approach teaser: one phase lights after another; a comet runs the trajectory (SMIL, no JS per frame) ───── */
  const faN = (n) => String(n).replace(/\d/g, (d) => '۰۱۲۳۴۵۶۷۸۹'[d]);
  const mini = $('#mini'), mph = $$('#miniPh li'), mdm = $$('#mini .dm'), mst = $('#miniStatus');
  let mk = 0, miniOn = false;
  const miniSet = (k) => { mk = k; mph.forEach((li, i) => li.classList.toggle('on', i === k)); mdm.forEach((d, i) => d.classList.toggle('on', i === k)); mst.textContent = `مرحله‌ی ${faN(k + 1)} از ۳`; };
  new IntersectionObserver(([e]) => { miniOn = e.isIntersecting; }, { threshold: .3 }).observe(mini);
  // moving content gets a stop control (WCAG 2.2.2); reduced motion starts it stopped
  const msvg = $('#mini svg'), mpb = $('#miniPause'); let miniPaused = RM;
  const miniPause = (on) => { miniPaused = on; mpb.setAttribute('aria-pressed', on); mpb.setAttribute('aria-label', on ? 'ادامه‌ی حرکت نقشه' : 'توقف حرکت نقشه');
    mpb.firstElementChild.firstElementChild.setAttribute('d', on ? 'M3 2l9 5-9 5z' : 'M3 2h3v10H3zM8 2h3v10H8z'); if (msvg.pauseAnimations) on ? msvg.pauseAnimations() : msvg.unpauseAnimations(); };
  mpb.addEventListener('click', () => miniPause(!miniPaused));
  miniPause(miniPaused);
  setInterval(() => { if (miniOn && !miniPaused && document.visibilityState === 'visible') miniSet((mk + 1) % 3); }, 2600);

  /* ───── reveal once, under 500 ms; the bars grow the first time they are seen ───── */
  const rvObs = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); rvObs.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  const watchReveals = (root) => $$('.rv, .reveal-bars', root).forEach((el) => rvObs.observe(el));
  watchReveals(document);

  /* ───── paths: the visitor chooses where to go (#/capabilities · #/work · #/approach); pages cross-fade ───── */
  const views = { '': $('#v-home'), capabilities: $('#v-capabilities'), work: $('#v-work'), approach: $('#v-approach') };
  let current = '';
  function show(name, anchor) {
    Object.entries(views).forEach(([k, el]) => el.classList.toggle('on', k === name));
    current = name; document.title = views[name].dataset.title;
    if (name) { scrollTo(0, 0); const h1 = $('h1', views[name]); if (h1) h1.focus({ preventScroll: true }); watchReveals(views[name]); }
    dispatchEvent(new Event('resize'));          // canvases measure themselves once their page is visible
    if (!name && ready) { size(); kick(); }
    if (anchor) { const t = document.getElementById(anchor); if (t) t.scrollIntoView(); }
    navState(); tone(); bar();
  }
  function route(first, anchor) {
    const h = location.hash, m = h.match(/^#\/(\w+)/), name = m && views[m[1]] ? m[1] : '';
    if (name !== current || first) {
      const go = () => show(name, anchor);
      if (!first && document.startViewTransition && !RM) document.startViewTransition(go); else go();
      return;
    }
    if (!name && h && h.length > 1) { const t = document.getElementById(h.slice(1)); if (t) t.scrollIntoView({ behavior: RM ? 'auto' : 'smooth' }); }
  }
  addEventListener('hashchange', () => route(false));
  // a link to a home section while another page is open: go home first, then to the section; the shared contact block just scrolls
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="#"]'); if (!a) return;
    const href = a.getAttribute('href');
    const t = href.length > 1 && !href.startsWith('#/') ? document.getElementById(href.slice(1)) : null;
    if (t && current && views[''].contains(t)) { e.preventDefault(); history.pushState(null, '', href); route(false, href.slice(1)); if (!document.startViewTransition || RM) { /* handled */ } }
  });

  /* ───── header pills, bottom-sheet menu, floating action bar ───── */
  const mb = $('#menuBtn'), sheet = $('#bsheet'), scrim = $('#scrim'), mbar = $('#mbar'), contactSec = $('#contact'), theme = $('meta[name=theme-color]');
  function tone() {
    const dark = current === 'approach' ? scrollY < innerHeight * .8 : (!current && hero.getBoundingClientRect().bottom > 80 && !(p > (MOB.matches ? .5 : .8)));
    const c = dark ? '#0B0C0C' : '#F9F5EC'; if (theme.content !== c) theme.content = c;
  }
  addEventListener('scroll', tone, { passive: true });
  const inline = new Set();
  const ctaObs = new IntersectionObserver((es) => { es.forEach((e) => e.isIntersecting ? inline.add(e.target) : inline.delete(e.target)); bar(); });
  $$('.next-step, .vcta, .paths, .gp-foot').forEach((el) => ctaObs.observe(el));
  function bar() {
    const past = !!current || hero.getBoundingClientRect().bottom < innerHeight * .5, atContact = contactSec.getBoundingClientRect().top < innerHeight * .75;
    const vis = [...inline].some((el) => el.offsetParent !== null);
    const on = past && !atContact && !vis && !document.body.classList.contains('menu-on'); mbar.classList.toggle('show', on); mbar.inert = !on;
  }
  addEventListener('scroll', bar, { passive: true });
  let closeT = 0;
  const setMenu = (o) => {
    clearTimeout(closeT);
    if (o) { sheet.hidden = false; scrim.hidden = false; requestAnimationFrame(() => requestAnimationFrame(() => { sheet.classList.add('on'); scrim.classList.add('on'); })); $('#menuClose').focus({ preventScroll: true }); }
    else { sheet.classList.remove('on'); scrim.classList.remove('on'); sheet.style.translate = ''; closeT = setTimeout(() => { sheet.hidden = true; scrim.hidden = true; }, RM ? 0 : 420); }
    document.body.classList.toggle('menu-on', o); mb.setAttribute('aria-expanded', o); bar();
  };
  mb.addEventListener('click', () => setMenu(true));
  $('#menuClose').addEventListener('click', () => { setMenu(false); mb.focus(); });
  scrim.addEventListener('click', () => setMenu(false));
  sheet.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && !sheet.hidden) { setMenu(false); mb.focus(); } });
  // swipe the sheet down to dismiss (the close button stays as the visible alternative)
  let sy = null;
  sheet.addEventListener('touchstart', (e) => { if (sheet.scrollTop <= 0) sy = e.touches[0].clientY; }, { passive: true });
  sheet.addEventListener('touchmove', (e) => { if (sy === null) return; const dy = e.touches[0].clientY - sy; if (dy > 0) { sheet.style.transition = 'none'; sheet.style.translate = `0 ${dy}px`; } }, { passive: true });
  sheet.addEventListener('touchend', (e) => { if (sy === null) return; const dy = e.changedTouches[0].clientY - sy; sy = null; sheet.style.transition = ''; sheet.style.translate = ''; if (dy > 80) setMenu(false); });
  function navState() {
    $$('.navlink, .bsheet .row').forEach((a) => { if (current && a.getAttribute('href') === '#/' + current) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
  }

