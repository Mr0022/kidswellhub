#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ساخت بخش «مقاله‌های پیشنهادی» پایین هر مقاله.

کارت هر مقاله فقط یک جا نوشته می‌شود — در فهرست articles/index.html — و این اسکریپت از
همان کارت‌ها برای پایین هر مقاله سه کارت کوچک می‌سازد و میان دو نشانه‌ی
«مقاله‌های پیشنهادی» می‌گذارد. از ریشه‌ی مخزن اجرا کنید:

    python3 tools/related-posts.py

بلوک قبلی جایگزین می‌شود، پس اجرای دوباره چیزی را تکرار نمی‌کند.

انتخاب ثابت است، نه تصادفی: هر مقاله مقاله‌ی بعدی، دو تا بعدی و قبلی خودش را در
ترتیب articles/index.html پیشنهاد می‌کند (فهرست دوری است؛ بعد از آخری، اولی می‌آید). دلیلش:
- پیوندها میان دو بار خزیدن موتور جست‌وجو عوض نمی‌شوند؛
- هر مقاله دقیقاً از سه مقاله‌ی دیگر پیوند می‌گیرد و هیچ مقاله‌ای بی‌پیوند نمی‌ماند؛
- کارت‌های articles/index.html بر اساس موضوع کنار هم چیده شده‌اند، پس همسایه‌ها به هم
  مرتبط‌ترند. برای عوض کردن پیشنهادها، ترتیب کارت‌ها را در articles/index.html عوض کنید.

پیوند کارت‌ها نشانی بی‌پسوند مقاله است (‎/articles/<نام>) و فایلش articles/<نام>.html.
"""

import io, re

INDEX = "articles/index.html"
INDEX_URL = "/articles/"
COUNT = 3
START = "<!-- مقاله‌های پیشنهادی -->"
END   = "<!-- پایان مقاله‌های پیشنهادی -->"

GRID_RE = re.compile(r'<ul class="post-grid">(.*?)</ul>', re.S)
CARD_RE = re.compile(r'<li style="([^"]*)">\s*<article class="post-card">(.*?)</article>\s*</li>', re.S)
BLOCK_RE = re.compile(r'[ \t]*' + re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)

def field(pattern, src):
    m = re.search(pattern, src, re.S)
    assert m, pattern
    return m.groups() if len(m.groups()) > 1 else m.group(1)

def read_cards():
    grid = GRID_RE.search(io.open(INDEX, encoding="utf-8").read()).group(1)
    cards = []
    for style, body in CARD_RE.findall(grid):
        href, title = field(r'<h2><a href="([^"]+)">(.*?)</a></h2>', body)
        cards.append(dict(style=style, href=href, title=title,
                          img=field(r'<img class="post-card__img" src="([^"]+)"', body),
                          tag=field(r'<p class="post-card__tag">(.*?)</p>', body),
                          time=field(r'<span>([^<]*مطالعه)</span>', body)))
    return cards

def picks(cards, i):
    """بعدی، دو تا بعدی و قبلی؛ بی‌تکرار و بدون خودِ مقاله."""
    n, out = len(cards), []
    for step in (1, 2, -1):
        k = (i + step) % n
        if k != i and k not in out:
            out.append(k)
    return out[:COUNT]

def render(cards, ks):
    items = "".join(f'''      <li style="{c['style']}">
        <article class="post-card">
          <img class="post-card__img" src="{c['img']}" width="1200" height="630" alt="" loading="lazy" decoding="async" />
          <div class="post-card__body">
            <p class="post-card__tag">{c['tag']}</p>
            <h3><a href="{c['href']}">{c['title']}</a></h3>
            <p class="post-card__meta">
              <span>{c['time']}</span>
              <span class="post-card__go" aria-hidden="true">خواندن <i>←</i></span>
            </p>
          </div>
        </article>
      </li>
''' for c in (cards[k] for k in ks))
    return f'''  {START}
  <section class="post-related" aria-labelledby="related-title">
    <div class="post-related__head">
      <h2 id="related-title">مقاله‌های پیشنهادی</h2>
      <a class="post-related__all" href="{INDEX_URL}">همه‌ی مقاله‌ها <i aria-hidden="true">←</i></a>
    </div>
    <ul class="post-grid post-grid--related">
{items}    </ul>
  </section>
  {END}
'''

cards = read_cards()
assert len(cards) > 1, "در " + INDEX + " کمتر از دو کارت مقاله پیدا شد"
inbound = {c["href"]: 0 for c in cards}

for i, c in enumerate(cards):
    ks = picks(cards, i)
    for k in ks:
        inbound[cards[k]["href"]] += 1
    path = c["href"].lstrip("/") + ".html"
    src = io.open(path, encoding="utf-8").read()
    assert BLOCK_RE.search(src), path + ": نشانه‌های «مقاله‌های پیشنهادی» پیدا نشد"
    src = BLOCK_RE.sub(lambda m: render(cards, ks), src, count=1)
    io.open(path, "w", encoding="utf-8").write(src)
    print("ok", c["href"], "←", "، ".join(cards[k]["href"] for k in ks))

# هر مقاله باید دست‌کم از یک مقاله‌ی دیگر پیوند بگیرد
orphans = [h for h, n in inbound.items() if n == 0]
assert not orphans, "مقاله‌ی بی‌پیوند: " + "، ".join(orphans)
