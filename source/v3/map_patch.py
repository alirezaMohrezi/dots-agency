
MAP_PATCHES=[
 ("(function loop(now) { dtG = Math.max(0, Math.min(0.05, (now - last) / 1000)); last = now; requestAnimationFrame(loop); if (visible.get(cv) === false) return; t += dtG; draw(); })(last);",
  "let mPaused = false; const mpb = document.getElementById('mPause');\n      if (mpb) mpb.addEventListener('click', () => { mPaused = !mPaused; mpb.setAttribute('aria-pressed', mPaused); mpb.setAttribute('aria-label', mPaused ? 'ادامه‌ی حرکت نقشه' : 'توقف حرکت نقشه'); mpb.querySelector('path').setAttribute('d', mPaused ? 'M3 2l9 5-9 5z' : 'M3 2h3v10H3zM8 2h3v10H8z'); });\n      (function loop(now) { dtG = Math.max(0, Math.min(0.05, (now - last) / 1000)); last = now; requestAnimationFrame(loop); if (visible.get(cv) === false) return; if (!mPaused) t += dtG; draw(); })(last);"),
 ("setInterval(() => { if (inView && !user && document.visibilityState === 'visible') step(1, false); }, 3200);",
  "setInterval(() => { if (inView && !user && !mPaused && document.visibilityState === 'visible') step(1, false); }, 3200);"),
 ("const r = cv.getBoundingClientRect(), dpr = Math.min(2, devicePixelRatio || 1);","const r = cv.getBoundingClientRect(), dpr = Math.min(innerWidth < 860 ? 1.5 : 2, devicePixelRatio || 1);"),
]
def patch_map(js):
    for a,b in MAP_PATCHES:
        assert a in js, a[:50]; js=js.replace(a,b)
    return js
