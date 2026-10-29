/* =========================================================
   مرکز مغز و شناخت کودکان — پس‌زمینه‌ی بازی‌گوش صفحه‌ی اصلی

   یک بوم (canvas) پشت محتوای هر بخش که با نشانگر بازی می‌کند. فقط
   index.html این فایل را بار می‌کند. سه صحنه دارد و
   فقط یکی روی سایت است؛ برای عوض کردنش DEFAULT را تغییر دهید:
     meadow  باغ پروانه‌ها: پروانه‌ها کنار نشانگرِ ایستاده جمع می‌شوند، با کلیک گل می‌روید
     shapes  شکل‌های بازیگوش: شکل‌ها از نشانگر فرار می‌کنند، با کلیک شکل تازه می‌آید
     sea     زیر دریا: ماهی‌ها دنبال نشانگر می‌آیند، با کلیک فرار می‌کنند

   برای امتحانِ صحنه‌ی دیگر بدون ویرایش فایل: index.html?bg=sea (یا ?bg=off)
   ========================================================= */
(function () {
  'use strict';

  const DEFAULT = 'meadow';

  const TAU = Math.PI * 2;
  // رنگ‌های شاد ثابت، کنار دو رنگ خودِ هر بخش (--a و --b)
  const FUN = ['#ff6b8b', '#ffb547', '#ffd84d', '#4fd08a', '#45c4f0', '#8b7bff', '#ff8fd1'];
  const rand = (a, b) => a + Math.random() * (b - a);
  const pick = (arr) => arr[(Math.random() * arr.length) | 0];
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));

  function hexA(hex, a) {
    const n = parseInt(hex.slice(1), 16);
    return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`;
  }
  function starPath(c, x, y, r, points, inner) {
    c.beginPath();
    for (let i = 0; i < points * 2; i++) {
      const rr = i % 2 ? r * inner : r;
      const ang = (i / (points * 2)) * TAU - Math.PI / 2;
      c.lineTo(x + Math.cos(ang) * rr, y + Math.sin(ang) * rr);
    }
    c.closePath();
  }
  function heartPath(c, x, y, r) {
    c.beginPath();
    c.moveTo(x, y + r * .7);
    c.bezierCurveTo(x - r * 1.3, y - r * .1, x - r * .6, y - r * 1.1, x, y - r * .45);
    c.bezierCurveTo(x + r * .6, y - r * 1.1, x + r * 1.3, y - r * .1, x, y + r * .7);
    c.closePath();
  }
  /** نشانگر نزدیک است؟ شیء را از آن دور می‌کند */
  function repel(o, p, radius, force, dt) {
    if (!p.on) return;
    const dx = o.x - p.x, dy = o.y - p.y, d = Math.hypot(dx, dy);
    if (d < radius && d > .1) {
      const f = (1 - d / radius) * force * dt;
      o.vx += dx / d * f; o.vy += dy / d * f;
    }
  }

  /* ---------------------------------------------------------
     صحنه‌ها
     هر صحنه برای یک بوم ساخته می‌شود و pal رنگ‌های همان بخش است.
     init(W,H) از نو می‌چیند، resize(W,H) فقط اندازه را به‌روز می‌کند،
     step(dt,t,p) جلو می‌برد (p: نشانگر در مختصات همین بوم)، draw(c) می‌کشد
     و tap(x,y) پاسخ کلیک روی فضای خالی است.
     --------------------------------------------------------- */

  /** ۷. باغ پروانه‌ها */
  function meadow(pal) {
    const cols = [pal.a, pal.b, ...FUN];
    let W = 0, H = 0, bf = [], flowers = [];
    const flower = (x, g) => ({ x, h: rand(.45, 1) * Math.min(H * .18, 140), g, c: pick(cols), sway: rand(0, TAU) });
    const roam = (b) => { b.tx = rand(20, W - 20); b.ty = rand(20, H * .75); };

    return {
      init(w, h) {
        W = w; H = h; bf = []; flowers = [];
        const n = Math.round(W / 220) + 2;
        for (let i = 0; i < n; i++) {
          const b = { x: rand(0, W), y: rand(0, H * .7), vx: 0, vy: 0, ph: rand(0, TAU), c: pick(cols), c2: pick(FUN), s: rand(.85, 1.2) };
          roam(b);
          bf.push(b);
        }
        for (let x = rand(10, 40); x < W; x += rand(60, 130)) flowers.push(flower(x, 1));
      },
      resize(w, h) { W = w; H = h; },
      tap(x) {
        flowers.push(flower(x, 0));
        if (flowers.length > 40) flowers.shift();
      },
      step(dt, t, p) {
        // نشانگری که لحظه‌ای ایستاده (یا انگشتی که تازه لمس کرده) پروانه‌ها را صدا می‌زند
        const still = p.on && t - p.at > 350 && t - p.at < 8000;
        for (const b of bf) {
          b.ph += .35 * dt;
          let tx = b.tx, ty = b.ty;
          if (still) { tx = p.x + Math.cos(b.ph * .02) * 55; ty = p.y + Math.sin(b.ph * .025) * 40; }
          else if (Math.hypot(b.x - b.tx, b.y - b.ty) < 40) roam(b);
          const dx = tx - b.x, dy = ty - b.y, d = Math.hypot(dx, dy) || 1;
          b.vx += dx / d * .04 * dt; b.vy += dy / d * .04 * dt + Math.sin(b.ph * .3) * .05;
          if (!still) repel(b, p, 90, .6, dt);
          b.vx *= .96; b.vy *= .96;
          b.x += b.vx * dt; b.y += b.vy * dt;
        }
        for (const f of flowers) { f.g = Math.min(1, f.g + .015 * dt); f.sway += .02 * dt; }
      },
      draw(c) {
        c.fillStyle = hexA('#4fd08a', .35);
        c.beginPath(); c.moveTo(0, H);
        for (let x = 0; x <= W + 24; x += 24) c.lineTo(x, H - 26 - Math.sin(x * .015) * 10);
        c.lineTo(W, H); c.fill();
        for (const f of flowers) {
          const h = f.h * f.g, tipx = f.x + Math.sin(f.sway) * 6, tipy = H - 20 - h;
          c.strokeStyle = '#2fb37a'; c.lineWidth = 3;
          c.beginPath(); c.moveTo(f.x, H); c.quadraticCurveTo(f.x, H - h * .5, tipx, tipy); c.stroke();
          const pr = 9 * f.g;
          c.fillStyle = f.c;
          for (let i = 0; i < 6; i++) {
            const a = i / 6 * TAU + f.sway * .2;
            c.beginPath(); c.arc(tipx + Math.cos(a) * pr, tipy + Math.sin(a) * pr, pr * .75, 0, TAU); c.fill();
          }
          c.fillStyle = '#ffd84d'; c.beginPath(); c.arc(tipx, tipy, pr * .65, 0, TAU); c.fill();
        }
        for (const b of bf) {
          const flap = Math.abs(Math.sin(b.ph)) * .8 + .2, s = 13 * b.s;
          c.save(); c.translate(b.x, b.y); c.rotate(clamp(b.vx * .2, -.6, .6));
          for (const side of [-1, 1]) {
            c.save(); c.scale(side * flap, 1);
            c.fillStyle = b.c; c.beginPath(); c.ellipse(s * .75, -s * .45, s * .8, s * .62, -.4, 0, TAU); c.fill();
            c.fillStyle = b.c2; c.beginPath(); c.ellipse(s * .6, s * .45, s * .52, s * .42, .4, 0, TAU); c.fill();
            c.fillStyle = 'rgba(255,255,255,.55)'; c.beginPath(); c.arc(s * .8, -s * .5, s * .18, 0, TAU); c.fill();
            c.restore();
          }
          c.fillStyle = '#3a2e5c'; c.beginPath(); c.ellipse(0, 0, s * .14, s * .8, 0, 0, TAU); c.fill();
          c.strokeStyle = '#3a2e5c'; c.lineWidth = 1.2;
          c.beginPath(); c.moveTo(0, -s * .7); c.lineTo(-s * .3, -s * 1.2); c.moveTo(0, -s * .7); c.lineTo(s * .3, -s * 1.2); c.stroke();
          c.restore();
        }
      }
    };
  }

  /** ۵. شکل‌های بازیگوش */
  function shapes(pal) {
    const cols = [pal.a, pal.b, ...FUN];
    const kinds = ['circle', 'tri', 'square', 'star', 'heart'];
    let W = 0, H = 0, list = [];
    function make(x, y) {
      const a = rand(0, TAU), s = rand(.2, .6);
      return { x, y, vx: Math.cos(a) * s, vy: Math.sin(a) * s, r: rand(14, 28), rot: rand(0, TAU), vr: rand(-.02, .02), k: pick(kinds), c: pick(cols), pop: 0 };
    }

    return {
      init(w, h) {
        W = w; H = h; list = [];
        const n = Math.round(W * H / 60000) + 4;
        for (let i = 0; i < n; i++) list.push(make(rand(40, W - 40), rand(40, H - 40)));
      },
      resize(w, h) { W = w; H = h; },
      tap(x, y) {
        const s = make(x, y); s.pop = 1; list.push(s);
        if (list.length > 50) list.shift();
      },
      step(dt, t, p) {
        for (const s of list) {
          repel(s, p, 130, .7, dt);
          if (Math.hypot(s.vx, s.vy) > .6) { s.vx *= .97; s.vy *= .97; }
          s.x += s.vx * dt; s.y += s.vy * dt; s.rot += (s.vr + s.vx * .01) * dt;
          if (s.x < s.r) { s.x = s.r; s.vx = Math.abs(s.vx); }
          if (s.x > W - s.r) { s.x = W - s.r; s.vx = -Math.abs(s.vx); }
          if (s.y < s.r) { s.y = s.r; s.vy = Math.abs(s.vy); }
          if (s.y > H - s.r) { s.y = H - s.r; s.vy = -Math.abs(s.vy); }
          if (s.pop > 0) s.pop = Math.max(0, s.pop - .035 * dt);
        }
      },
      draw(c) {
        for (const s of list) {
          const r = s.r * Math.max(.2, 1 + Math.sin(s.pop * Math.PI) * .6 - s.pop * .8);
          c.save(); c.translate(s.x, s.y); c.rotate(s.rot);
          c.fillStyle = hexA(s.c, .45); c.strokeStyle = s.c; c.lineWidth = 3;
          c.beginPath();
          if (s.k === 'circle') c.arc(0, 0, r, 0, TAU);
          else if (s.k === 'square') c.roundRect(-r * .85, -r * .85, r * 1.7, r * 1.7, r * .3);
          else if (s.k === 'tri') { c.moveTo(0, -r); c.lineTo(r * .95, r * .7); c.lineTo(-r * .95, r * .7); c.closePath(); }
          else if (s.k === 'star') starPath(c, 0, 0, r * 1.1, 5, .5);
          else heartPath(c, 0, 0, r);
          c.fill(); c.stroke();
          c.restore();
        }
      }
    };
  }

  /** ۶. زیر دریا */
  function sea(pal) {
    const cols = [pal.a, pal.b, ...FUN];
    let W = 0, H = 0, fish = [], bub = [], weeds = [], scare = 0, t0 = 0;
    const wander = (f) => { f.wx = rand(30, W - 30); f.wy = rand(H * .08, H * .78); };

    return {
      init(w, h) {
        W = w; H = h; fish = []; bub = []; weeds = []; scare = 0;
        const n = Math.round(W / 160) + 3;
        for (let i = 0; i < n; i++) {
          const f = { x: rand(0, W), y: rand(H * .1, H * .8), vx: rand(-1, 1), vy: rand(-.3, .3), s: rand(.7, 1.3), c: pick(cols), ph: rand(0, TAU) };
          wander(f);
          fish.push(f);
        }
        for (let x = 10; x < W; x += rand(44, 80)) weeds.push({ x, h: rand(.1, .22) * Math.min(H, 900), ph: rand(0, TAU), c: Math.random() < .5 ? '#4fd08a' : '#2fb37a' });
        for (let i = 0; i < 18; i++) bub.push({ x: rand(0, W), y: rand(0, H), r: rand(2, 6), v: rand(.3, .9) });
      },
      resize(w, h) { W = w; H = h; },
      tap(x, y) {
        scare = 1;
        for (const f of fish) {
          const dx = f.x - x, dy = f.y - y, d = Math.hypot(dx, dy) || 1;
          f.vx += dx / d * 6; f.vy += dy / d * 4;
        }
        for (let i = 0; i < 10; i++) bub.push({ x: x + rand(-14, 14), y: y + rand(-10, 10), r: rand(3, 8), v: rand(.8, 1.8) });
      },
      step(dt, t, p) {
        t0 = t;
        scare = Math.max(0, scare - .01 * dt);
        // ماهی‌ها فقط دنبال نشانگرِ در حال حرکت می‌آیند؛ نشانگرِ بی‌حرکت را رها می‌کنند
        const follow = p.on && t - p.at < 2500 && scare < .3;
        for (const f of fish) {
          f.ph += .2 * dt;
          let tx = f.wx, ty = f.wy;
          if (follow) { tx = p.x + Math.cos(f.ph * .05) * 40; ty = p.y + Math.sin(f.ph * .04) * 30; }
          else if (Math.hypot(f.x - f.wx, f.y - f.wy) < 30) wander(f);
          const dx = tx - f.x, dy = ty - f.y, d = Math.hypot(dx, dy) || 1;
          f.vx += dx / d * .05 * dt; f.vy += dy / d * .04 * dt;
          f.vx *= .975; f.vy *= .96;
          const sp = Math.hypot(f.vx, f.vy);
          if (sp > 3.4 && scare < .2) { f.vx *= 3.4 / sp; f.vy *= 3.4 / sp; }
          f.x += f.vx * dt; f.y += f.vy * dt;
          if (f.x < -40) f.x = W + 30;
          if (f.x > W + 40) f.x = -30;
          f.y = clamp(f.y, 10, H * .86);
        }
        for (const b of bub) {
          b.y -= b.v * dt; b.x += Math.sin((b.y + b.r * 20) * .03) * .3;
          if (b.y < -10) { b.y = H + 10; b.x = rand(0, W); }
        }
        if (bub.length > 60) bub.splice(18, bub.length - 60);
        for (const w of weeds) w.ph += .02 * dt;
      },
      draw(c) {
        // نوارهای نور از سطح آب
        c.fillStyle = hexA(pal.b, .12);
        for (let i = 0; i < 4; i++) {
          const x = (i / 4) * W + Math.sin(t0 * .0004 + i) * 40;
          c.beginPath(); c.moveTo(x, 0); c.lineTo(x + 70, 0); c.lineTo(x + 170, H); c.lineTo(x + 100, H); c.fill();
        }
        c.lineCap = 'round';
        for (const w of weeds) {
          c.strokeStyle = w.c; c.lineWidth = 7;
          c.beginPath(); c.moveTo(w.x, H + 4);
          for (let k = 1; k <= 6; k++) c.lineTo(w.x + Math.sin(w.ph + k * .7) * k * 3, H - (w.h * k / 6));
          c.stroke();
        }
        c.fillStyle = hexA(pal.a, .12);
        c.beginPath(); c.moveTo(0, H);
        for (let x = 0; x <= W + 20; x += 20) c.lineTo(x, H - 18 - Math.sin(x * .02) * 8);
        c.lineTo(W, H); c.fill();
        for (const f of fish) {
          const dir = f.vx < 0 ? -1 : 1, s = 14 * f.s, wag = Math.sin(f.ph) * .35;
          c.save(); c.translate(f.x, f.y); c.scale(dir, 1); c.rotate(clamp(f.vy * .15, -.5, .5));
          c.fillStyle = f.c;
          c.beginPath(); c.moveTo(-s * .9, 0); c.lineTo(-s * 1.7, -s * .6 + wag * s); c.lineTo(-s * 1.7, s * .6 + wag * s); c.closePath(); c.fill();
          c.beginPath(); c.ellipse(0, 0, s * 1.1, s * .72, 0, 0, TAU); c.fill();
          c.fillStyle = 'rgba(255,255,255,.35)';
          c.beginPath(); c.ellipse(-s * .1, s * .2, s * .7, s * .3, 0, 0, TAU); c.fill();
          c.fillStyle = '#fff'; c.beginPath(); c.arc(s * .5, -s * .15, s * .24, 0, TAU); c.fill();
          c.fillStyle = '#1d1b2e'; c.beginPath(); c.arc(s * .56, -s * .15, s * .12, 0, TAU); c.fill();
          c.restore();
        }
        c.strokeStyle = 'rgba(255,255,255,.85)'; c.lineWidth = 1.4; c.fillStyle = 'rgba(255,255,255,.25)';
        for (const b of bub) { c.beginPath(); c.arc(b.x, b.y, b.r, 0, TAU); c.fill(); c.stroke(); }
      }
    };
  }

  const SCENES = { meadow, shapes, sea };

  /* ---------------------------------------------------------
     انتخاب صحنه
     --------------------------------------------------------- */

  let choice = DEFAULT;
  try { choice = new URLSearchParams(location.search).get('bg') || DEFAULT; } catch (_) { /* نشانی نامعتبر */ }
  if (choice === 'off') return;
  const make = SCENES[choice] || SCENES[DEFAULT];
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------
     میزبان‌ها: یک بوم در هر بخش، کنار لکه‌های تزئینی (z-index: -1 درون
     بخش، پس روی رنگ پس‌زمینه‌ی بخش و زیر محتوایش) با رنگ‌های همان بخش؛
     فقط بخش‌های دیده‌شده بوم واقعی دارند و جلو می‌روند.
     --------------------------------------------------------- */

  const scroller = document.getElementById('scroller');
  if (!scroller) return;
  const sections = Array.from(scroller.querySelectorAll('.sec'));

  function color(cs, name, fallback) {
    const v = cs.getPropertyValue(name).trim();
    return /^#[0-9a-f]{6}$/i.test(v) ? v : fallback;
  }

  const hosts = sections.map((el) => {
    const cv = document.createElement('canvas');
    cv.className = 'playground';
    cv.setAttribute('aria-hidden', 'true');
    cv.width = cv.height = 0;
    const blobs = el.querySelector(':scope > .blobs');
    if (blobs) blobs.after(cv); else el.prepend(cv);
    const cs = getComputedStyle(el);
    const pal = { a: color(cs, '--a', '#7c5cff'), b: color(cs, '--b', '#ff7ab6') };
    return { el, cv, ctx: cv.getContext('2d'), scene: make(pal), W: 0, H: 0, visible: false, ready: false, settled: false };
  });

  /** اندازه‌ی بوم با جعبه‌ی خودش؛ صحنه فقط وقتی پهنا محسوس عوض شود از نو چیده می‌شود
      (نوار آدرس گوشی که ارتفاع را کم و زیاد می‌کند، باغ را از نو نمی‌کارد) */
  function fit(h) {
    const r = h.cv.getBoundingClientRect();
    const W = Math.round(r.width), H = Math.round(r.height);
    if (!W || !H) return;
    const dpr = Math.min(1.5, window.devicePixelRatio || 1);
    h.cv.width = Math.round(W * dpr);
    h.cv.height = Math.round(H * dpr);
    h.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    if (!h.ready || Math.abs(W - h.W) > h.W * .25) { h.scene.init(W, H); h.ready = true; h.settled = false; }
    else h.scene.resize(W, H);
    h.W = W; h.H = H;
    if (reduceMotion) still(h);
    else wake();
  }
  /** بوم بخشی که دیده نمی‌شود حافظه نگیرد؛ وضعیت صحنه‌اش می‌ماند */
  function free(h) { h.cv.width = 0; h.cv.height = 0; }

  const byCanvas = new Map(hosts.map((h) => [h.cv, h]));
  const byEl = new Map(hosts.map((h) => [h.el, h]));
  const ro = new ResizeObserver((entries) => entries.forEach((en) => {
    const h = byCanvas.get(en.target);
    if (h.visible) fit(h);
  }));
  hosts.forEach((h) => ro.observe(h.cv));

  // حاشیه‌ی منفی: بخشی که فقط لبه‌به‌لبه‌ی صفحه است، دیده‌شده حساب نشود
  const io = new IntersectionObserver((entries) => entries.forEach((en) => {
    const h = byEl.get(en.target);
    h.visible = en.isIntersecting;
    if (h.visible) fit(h); else free(h);
  }), { root: scroller, rootMargin: '-1px 0px' });
  hosts.forEach((h) => io.observe(h.el));

  /* ---------------------------------------------------------
     نشانگر: در کل صفحه دنبال می‌شود، حتی روی محتوا
     --------------------------------------------------------- */

  const ptr = { x: -1e4, y: -1e4, on: false, at: -1e4 };
  const track = (e) => { ptr.x = e.clientX; ptr.y = e.clientY; ptr.on = true; ptr.at = performance.now(); };
  window.addEventListener('pointermove', track, { passive: true });
  window.addEventListener('pointerdown', track, { passive: true });
  document.addEventListener('mouseout', (e) => { if (!e.relatedTarget) ptr.on = false; });

  /** نشانگر در مختصات بوم h */
  function local(h) {
    const r = h.cv.getBoundingClientRect();
    return {
      x: ptr.x - r.left, y: ptr.y - r.top, at: ptr.at,
      on: ptr.on && ptr.x >= r.left && ptr.x <= r.right && ptr.y >= r.top && ptr.y <= r.bottom
    };
  }

  /* ---------------------------------------------------------
     کلیک روی فضای خالی (نه دکمه، نه متن، نه کارت) صحنه را بازی می‌دهد
     --------------------------------------------------------- */

  const BUSY = 'a, button, input, select, textarea, label, summary, details, canvas, svg, img, video, ' +
               'header, nav, footer, p, h1, h2, h3, h4, li, blockquote, figure, table, pre, ' +
               '[role], [tabindex], [contenteditable]';

  /** هدف کلیک خودِ زمینه‌ی صفحه است: نه درون عنصری کاربردی و نه روی سطحی رنگی (کارت، چیپ) */
  function bare(el) {
    for (let n = el; n instanceof Element; n = n.parentElement) {
      if (byEl.has(n)) return true;
      if (n.matches(BUSY)) return false;
      const s = getComputedStyle(n);
      if (s.backgroundImage !== 'none' || s.backgroundColor !== 'rgba(0, 0, 0, 0)') return false;
    }
    return false;
  }

  document.addEventListener('click', (e) => {
    if (e.button !== 0 || !bare(e.target) || String(window.getSelection())) return;
    const h = hosts.find((k) => {
      if (!k.visible || !k.cv.width) return false;
      const r = k.cv.getBoundingClientRect();
      return e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;
    });
    if (!h) return;
    const r = h.cv.getBoundingClientRect();
    h.scene.tap(e.clientX - r.left, e.clientY - r.top);
    if (reduceMotion) still(h, true);
  });

  /* ---------------------------------------------------------
     حلقه‌ی انیمیشن: فقط تا وقتی بومی دیده می‌شود
     --------------------------------------------------------- */

  let raf = 0, last = 0;
  function frame(t) {
    raf = 0;
    const dt = Math.min(3, (t - last) / 16.67 || 1);
    last = t;
    let any = false;
    hosts.forEach((h) => {
      if (!h.visible || !h.cv.width) return;
      any = true;
      h.scene.step(dt, t, local(h));
      h.ctx.clearRect(0, 0, h.W, h.H);
      h.scene.draw(h.ctx);
    });
    if (any) raf = requestAnimationFrame(frame);
  }
  function wake() {
    if (raf) return;
    last = performance.now();
    raf = requestAnimationFrame(frame);
  }

  /** «کاهش حرکت»: صحنه یک بار جا می‌افتد و تصویری ثابت می‌ماند؛ کلیک فقط همان تصویر را به‌روز می‌کند */
  function still(h, grow) {
    const idle = { x: -1e4, y: -1e4, on: false, at: -1e4 };
    const n = !h.settled ? 120 : (grow ? 80 : 0);
    for (let i = 0; i < n; i++) h.scene.step(1, i * 16.67, idle);
    h.settled = true;
    h.ctx.clearRect(0, 0, h.W, h.H);
    h.scene.draw(h.ctx);
  }
})();
