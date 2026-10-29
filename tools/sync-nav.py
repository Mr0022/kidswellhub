#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
هدر و نوار ناوبری صفحه‌ی اصلی را به همه‌ی صفحه‌های دیگر می‌برد.

سایت ابزار ساخت ندارد و هدر در هر فایل HTML تکرار شده است. فقط در index.html
ویرایشش کنید و سپس از ریشه‌ی مخزن اجرا کنید:

    python3 tools/sync-nav.py

- هدر: از <header class="site-head"> تا منوی تمام‌صفحه (<nav class="menu-panel">).
  پیوندهای درون‌صفحه‌ای صفحه‌ی اصلی (href="#tamas" data-goto="tamas") به
  index.html#tamas تبدیل می‌شوند و #hero به خود index.html.
- 404.html را Cloudflare Pages در هر نشانی ناموجودی نشان می‌دهد، پس همه‌ی
  نشانی‌های هدرش از ریشه‌ی دامنه‌اند (/reserve.html، و / برای صفحه‌ی اصلی).
- در reserve.html دکمه‌ی «رزرو نوبت» هدر aria-current="page" می‌گیرد.
- assets/site.js اگر در صفحه‌ای بار نشده باشد، پیش از نخستین اسکریپت پایان صفحه
  (یا پیش از </body>) اضافه می‌شود و assets/playground.js (پس‌زمینه‌ی بازی‌گوش)
  درست پس از آن؛ نشانه‌ی نسخه‌ی styles.css، site.js و playground.js همه‌ی
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
ASSET = re.compile(r'(/?assets/(?:styles\.css|site\.js|playground\.js))\?v=\d+')
# نشانی نسبی: نه طرح‌دار (https:، tel:)، نه #…، نه از ریشه‌ی دامنه (/…)
LOCAL = re.compile(r'((?:href|src)=")(?![a-z][a-z0-9+.-]*:|#|/)([^"]+)(")')


def page_head(head):
    """هدر صفحه‌ی اصلی، برای صفحه‌های دیگر"""
    head = re.sub(r'href="#hero" data-goto="hero"', 'href="index.html"', head)
    return re.sub(r'href="#([\w-]+)" data-goto="\1"', r'href="index.html#\1"', head)


def from_root(head):
    """همه‌ی نشانی‌های نسبی از ریشه‌ی دامنه (برای 404.html)"""
    def fix(m):
        url = m.group(2)
        url = '/' + url[len('index.html'):] if url.startswith('index.html') else '/' + url
        return m.group(1) + url + m.group(3)
    return LOCAL.sub(fix, head)


def main():
    index = io.open('index.html', encoding='utf-8').read()
    head = page_head(HEAD.search(index).group(0))
    versions = {m.group(1).lstrip('/'): m.group(0).lstrip('/') for m in ASSET.finditer(index)}
    if set(versions) != {'assets/styles.css', 'assets/site.js', 'assets/playground.js'}:
        sys.exit('index.html باید styles.css، site.js و playground.js را با نشانه‌ی نسخه (?v=N) بار کند')

    for name in sorted(f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html'):
        src = io.open(name, encoding='utf-8').read()
        root = '/' if name == '404.html' else ''
        mine = from_root(head) if root else head
        if name == 'reserve.html':
            mine = mine.replace('class="btn head-cta" href="reserve.html"',
                                'class="btn head-cta" href="reserve.html" aria-current="page"')
        if not HEAD.search(src):
            sys.exit(name + ': هدر <header class="site-head"> پیدا نشد')
        out = HEAD.sub(lambda m: mine, src, count=1)

        if 'assets/site.js' not in out:
            tag = '<script src="' + root + 'assets/site.js?v=0"></script>\n'
            k = out.find('<script src=', out.find('</main>'))
            k = k if k >= 0 else out.find('</body>')
            out = out[:k] + tag + out[k:]
        if 'assets/playground.js' not in out:
            site = re.search(r'<script src="/?assets/site\.js\?v=\d+"></script>\n', out)
            tag = '<script src="' + root + 'assets/playground.js?v=0"></script>\n'
            out = out[:site.end()] + tag + out[site.end():]
        out = ASSET.sub(lambda m: m.group(1).rsplit('assets/', 1)[0] + versions[m.group(1).lstrip('/')], out)

        if out != src:
            io.open(name, 'w', encoding='utf-8').write(out)
            print('به‌روز شد:', name)


if __name__ == '__main__':
    main()
