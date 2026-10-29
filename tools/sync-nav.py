#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
هدر و نوار ناوبری صفحه‌ی اصلی را به همه‌ی صفحه‌های دیگر می‌برد.

سایت ابزار ساخت ندارد و هدر در هر فایل HTML تکرار شده است. فقط در index.html
ویرایشش کنید و سپس از ریشه‌ی مخزن اجرا کنید:

    python3 tools/sync-nav.py

- هدر: از <header class="site-head"> تا منوی تمام‌صفحه (<nav class="menu-panel">).
  همه‌ی نشانی‌های سایت از ریشه‌ی دامنه و بی‌پسوندند (/reserve، /services/cognitive،
  /articles/)، پس هدر در هر پوشه‌ای همان است. فقط پیوندهای درون‌صفحه‌ای صفحه‌ی اصلی
  (href="#tamas" data-goto="tamas") به /#tamas تبدیل می‌شوند و #hero به خود /.
- صفحه‌ها: همه‌ی HTMLهای ریشه، articles/ و services/ (404.html هم، که Cloudflare Pages
  در هر نشانی ناموجودی نشانش می‌دهد).
- در reserve.html دکمه‌ی «رزرو نوبت» هدر aria-current="page" می‌گیرد.
- assets/site.js اگر در صفحه‌ای بار نشده باشد، پیش از نخستین اسکریپت پایان صفحه
  (یا پیش از </body>) اضافه می‌شود، و نشانه‌ی نسخه‌ی styles.css و site.js همه‌ی
  صفحه‌ها با index.html یکی می‌شود (فایل‌های assets طولانی کش می‌شوند).

اینکه کدام پیوند ناوبری در هر صفحه «جاری» است، از صفت data-page یا data-section
روی <body> همان صفحه می‌آید (site.js)، و این اسکریپت به آن دست نمی‌زند.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

HEAD = re.compile(
    r'<header class="site-head">.*?</header>'
    r'(?:\n\n<!-- منوی تمام‌صفحه[^\n]*-->\n<nav class="menu-panel"[^>]*></nav>)?', re.S)
ASSET = re.compile(r'(/?assets/(?:styles\.css|site\.js))\?v=\d+')
FOLDERS = ('articles', 'services')


def page_head(head):
    """هدر صفحه‌ی اصلی، برای صفحه‌های دیگر"""
    head = re.sub(r'href="#hero" data-goto="hero"', 'href="/"', head)
    return re.sub(r'href="#([\w-]+)" data-goto="\1"', r'href="/#\1"', head)


def main():
    index = io.open('index.html', encoding='utf-8').read()
    head = page_head(HEAD.search(index).group(0))
    versions = {m.group(1).lstrip('/'): m.group(0).lstrip('/') for m in ASSET.finditer(index)}
    if set(versions) != {'assets/styles.css', 'assets/site.js'}:
        sys.exit('index.html باید styles.css و site.js را با نشانه‌ی نسخه (?v=N) بار کند')

    names = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
    names += [os.path.join(d, f) for d in FOLDERS for f in os.listdir(d) if f.endswith('.html')]
    for name in sorted(names):
        src = io.open(name, encoding='utf-8').read()
        mine = head
        if name == 'reserve.html':
            mine = mine.replace('class="btn head-cta" href="/reserve"',
                                'class="btn head-cta" href="/reserve" aria-current="page"')
        if not HEAD.search(src):
            sys.exit(name + ': هدر <header class="site-head"> پیدا نشد')
        out = HEAD.sub(lambda m: mine, src, count=1)

        if 'assets/site.js' not in out:
            tag = '<script src="/assets/site.js?v=0"></script>\n'
            k = out.find('<script src=', out.find('</main>'))
            k = k if k >= 0 else out.find('</body>')
            out = out[:k] + tag + out[k:]
        out = ASSET.sub(lambda m: m.group(1).rsplit('assets/', 1)[0] + versions[m.group(1).lstrip('/')], out)

        if out != src:
            io.open(name, 'w', encoding='utf-8').write(out)
            print('به‌روز شد:', name)


if __name__ == '__main__':
    main()
