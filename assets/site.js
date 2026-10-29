/* =========================================================
   مرکز مغز و شناخت کودکان — بخش‌های مشترک همه‌ی صفحه‌ها
   نوار ناوبری بالا و منوی تمام‌صفحه.
   صفحه‌ی اصلی (app.js) از راه window.kidsSite به این‌ها دسترسی دارد.
   ========================================================= */
(function () {
  'use strict';

  const $  = (sel, el = document) => el.querySelector(sel);
  const $$ = (sel, el = document) => Array.from(el.querySelectorAll(sel));

  /* ---------------------------------------------------------
     ناوبری بالا: پیوند جاری، نشانگر لغزان زیر آن، و زیرمنوی خدمات
     --------------------------------------------------------- */

  const topnav  = $('#topnav');
  // پیوندهای سطح اول (نشانگر لغزان زیر این‌ها می‌رود) و پیوندهای زیرمنوی خدمات
  const navEls  = $$('.topnav__list > li > [data-sections]', topnav);
  const subNavEls = $$('.topnav__sub [data-sections]', topnav);
  const navInd  = $('.topnav__ind', topnav);
  const subItem = $('.topnav__has-sub', topnav);
  const subBtn  = $('button', subItem);
  const subLinks = $$('.topnav__sub a', subItem);
  let subOpenedAt = 0, subHoverTimer = 0;

  /** نشانگر به اندازه و جای پیوند جاری درمی‌آید؛ اگر پیوند پنهان است، نشانگر هم */
  function placeIndicator() {
    const el = navEls.find((n) => n.classList.contains('is-active'));
    if (!el || !el.offsetWidth) { navInd.style.opacity = '0'; return; }
    const box = topnav.getBoundingClientRect();
    const r = el.getBoundingClientRect();
    navInd.style.setProperty('--x', (r.left - box.left - topnav.clientLeft) + 'px');
    navInd.style.setProperty('--y', (r.top - box.top - topnav.clientTop) + 'px');
    navInd.style.setProperty('--w', r.width + 'px');
    navInd.style.setProperty('--h', r.height + 'px');
    navInd.style.opacity = '';
    // نخستین بار بدون لغزش، از آن پس با لغزش
    if (!navInd.classList.contains('is-ready')) requestAnimationFrame(() => navInd.classList.add('is-ready'));
  }
  window.addEventListener('resize', placeIndicator);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(placeIndicator);

  const subOpen = () => subItem.classList.contains('is-open');
  function setSub(open) {
    subItem.classList.toggle('is-open', open);
    subBtn.setAttribute('aria-expanded', String(open));
    if (open) subOpenedAt = performance.now();
  }
  // کلیک باز و بسته می‌کند؛ اما کلیکی که بلافاصله پس از باز شدن با نشانگر برسد، آن را نمی‌بندد
  subBtn.addEventListener('click', () => setSub(!subOpen() || performance.now() - subOpenedAt < 400));
  subItem.addEventListener('pointerenter', (e) => {
    if (e.pointerType !== 'mouse') return;
    clearTimeout(subHoverTimer);
    if (!subOpen()) setSub(true);
  });
  subItem.addEventListener('pointerleave', (e) => {
    if (e.pointerType !== 'mouse') return;
    subHoverTimer = setTimeout(() => setSub(false), 220);
  });
  document.addEventListener('pointerdown', (e) => { if (subOpen() && !subItem.contains(e.target)) setSub(false); });
  subItem.addEventListener('focusout', (e) => { if (!subItem.contains(e.relatedTarget)) setSub(false); });
  // کلیدهای جهت درون زیرمنو میان گزینه‌ها می‌چرخند، نه میان بخش‌ها
  subItem.addEventListener('keydown', (e) => {
    const step = { ArrowDown: 1, ArrowUp: -1 }[e.key];
    if (!step) return;
    e.preventDefault();
    if (!subOpen()) setSub(true);
    const n = subLinks.length;
    const k = subLinks.indexOf(document.activeElement);
    subLinks[k < 0 ? (step > 0 ? 0 : n - 1) : (k + step + n) % n].focus();
  });

  /** پیوندهایی که data-sections آن‌ها id را دارد «جاری» می‌شوند */
  const markCurrent = (els, id, current) => els.forEach((n) => {
    const on = n.dataset.sections.split(' ').includes(id);
    n.classList.toggle('is-active', on);
    if (on && n.tagName === 'A') n.setAttribute('aria-current', current);
    else n.removeAttribute('aria-current');
  });

  /** پیوند جاری در نوار ناوبری (نشانگر به زیرش می‌لغزد)، در زیرمنوی خدمات و در منوی تمام‌صفحه */
  function setActive(id, current = 'true') {
    markCurrent(navEls, id, current);
    markCurrent(subNavEls, id, current);
    markCurrent(menuEls, id, current);
    setSub(false);
    placeIndicator();
  }

  /* ---------------------------------------------------------
     منوی تمام‌صفحه (گوشی و تبلت، جایی که کپسول ناوبری جا نمی‌شود)

     فهرستش از روی همان نوار ناوبری بالا ساخته می‌شود تا این دو هیچ‌گاه از هم
     جدا نشوند: همان پیوندها به همان ترتیب، «خدمات» به‌صورت گروهی که باز و
     بسته می‌شود، و دکمه‌ی رزرو نوبت هدر در پایان.
     --------------------------------------------------------- */

  const menuBtn   = $('#menuBtn');
  const menuPanel = $('#menuPanel');

  /** پیوندی تازه به همان مقصد (در صفحه‌ی اصلی، با همان data-goto که app.js به آن گوش می‌دهد) */
  const copyLink = (src, className) => {
    const a = document.createElement('a');
    a.setAttribute('href', src.getAttribute('href'));
    if (src.dataset.goto) a.dataset.goto = src.dataset.goto;
    a.className = className;
    return a;
  };

  /** گروه «خدمات» را باز یا بسته می‌کند؛ گزینه‌های گروه بسته با Tab هم در دسترس نیستند */
  function setGroup(toggle, open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.nextElementSibling.inert = !open;
  }

  const menuInner = document.createElement('div');
  menuInner.className = 'menu-panel__inner';
  const menuList = document.createElement('ul');
  menuList.className = 'menu-panel__list';
  $$('.topnav__list > li', topnav).forEach((li, k) => {
    const item = document.createElement('li');
    item.style.setProperty('--k', String(k));
    const src = li.firstElementChild;
    if (li !== subItem) {
      const a = copyLink(src, 'menu-panel__link');
      a.dataset.sections = src.dataset.sections;
      a.textContent = src.textContent.trim();
      item.appendChild(a);
    } else {
      const toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'menu-panel__link menu-panel__toggle';
      toggle.dataset.sections = src.dataset.sections;
      toggle.setAttribute('aria-controls', 'menuServices');
      const label = document.createElement('span');
      label.textContent = src.textContent.trim();
      toggle.append(label, $('.topnav__caret', src).cloneNode(true));
      // زیرمجموعه‌ها همان گزینه‌های زیرمنوی خدمات‌اند، با آیکون، رنگ و عنوان (کارت رزرو نوبتش پایین منو دکمه است)
      const group = document.createElement('div');
      group.className = 'menu-panel__group';
      group.id = 'menuServices';
      const ul = document.createElement('ul');
      subLinks.filter((s) => !s.classList.contains('topnav__sub-cta')).forEach((s) => {
        const a = copyLink(s, 'menu-panel__sublink');
        a.dataset.sections = s.dataset.sections;
        if (s.getAttribute('style')) a.setAttribute('style', s.getAttribute('style'));
        a.append($('.topnav__sub-ico', s).cloneNode(true), $('b', s).textContent);
        const sl = document.createElement('li');
        sl.appendChild(a);
        ul.appendChild(sl);
      });
      group.appendChild(ul);
      toggle.addEventListener('click', () => setGroup(toggle, toggle.getAttribute('aria-expanded') !== 'true'));
      item.append(toggle, group);
      setGroup(toggle, false);
    }
    menuList.appendChild(item);
  });
  const headCta = $('.head-cta');
  const menuCta = copyLink(headCta, 'btn btn--big menu-panel__cta');
  menuCta.textContent = headCta.textContent.trim();
  if (headCta.hasAttribute('aria-current')) menuCta.setAttribute('aria-current', 'page');
  menuCta.style.setProperty('--k', String(menuList.children.length));
  menuInner.append(menuList, menuCta);
  menuPanel.appendChild(menuInner);
  const menuEls = $$('[data-sections]', menuPanel);

  const menuOpen = () => menuPanel.classList.contains('is-open');
  // هر چه پشت منوست، تا وقتی منو باز است در دسترس نیست
  const behindMenu = $$('main, footer, #dots, #topnav');

  function openMenu() {
    // گروهی که بخش جاری در آن است باز است، بقیه بسته
    $$('.menu-panel__toggle', menuPanel).forEach((t) => setGroup(t, t.classList.contains('is-active')));
    menuPanel.classList.add('is-open');
    menuBtn.setAttribute('aria-expanded', 'true');
    behindMenu.forEach((el) => { el.inert = true; });
    ($('[aria-current]', menuPanel) || $('a, button', menuPanel)).focus({ preventScroll: true });
  }
  function closeMenu() {
    if (!menuOpen()) return;
    menuPanel.classList.remove('is-open');
    menuBtn.setAttribute('aria-expanded', 'false');
    behindMenu.forEach((el) => { el.inert = false; });
  }
  menuBtn.addEventListener('click', () => (menuOpen() ? closeMenu() : openMenu()));
  menuPanel.addEventListener('click', (e) => {
    if (e.target === menuPanel || e.target === menuInner) { closeMenu(); return; }
    const a = e.target.closest('a');
    if (!a) return;
    // پیوند همین صفحه فقط منو را می‌بندد؛ بقیه هم منو را می‌بندند تا بخشی از همین صفحه
    // (مثل about.html#faq روی صفحه‌ی درباره‌ی ما) زیر منوی باز پنهان نماند
    if (a.getAttribute('aria-current') === 'page') e.preventDefault();
    closeMenu();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    if (menuOpen()) { closeMenu(); menuBtn.focus(); }
    else if (subOpen()) { setSub(false); subBtn.focus(); }
  });

  // صفحه‌ای که خودش یکی از پیوندهای ناوبری است (<body data-page="about">)، یا صفحه‌ای درون
  // بخشی از آن (<body data-section="fine-motor">، مثل بازی‌های دست‌ورزی؛ پیوند بخش جاری است ولی همچنان به صفحه‌ی بخش می‌رود)
  const { page, section } = document.body.dataset;
  if (page) setActive(page, 'page');
  else if (section) setActive(section, 'true');

  window.kidsSite = { setActive, closeSub: () => setSub(false), menuOpen, closeMenu };
})();
