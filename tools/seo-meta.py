#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تولید بلوک سئوی <head> همه‌ی صفحه‌ها و فایل sitemap.xml.

برای تغییر عنوان یا توضیح یک صفحه، جدول PAGES پایین را ویرایش و این فایل را
از ریشه‌ی مخزن اجرا کنید:

    python3 tools/seo-meta.py

اسکریپت بلوک قبلی را (میان دو نشانه‌ی «سئو») جایگزین می‌کند، پس اجرای دوباره
چیزی را تکرار نمی‌کند. متن پرسش‌های متداول از خودِ HTML خوانده می‌شود تا
اسکیمای FAQPage همیشه با محتوای دیده‌شده یکی باشد.
"""

SITE = "https://kidswellhub.ir"
BRAND = "مرکز مغز و شناخت کودکان"
KW1 = "کاردرمانی ذهنی کودکان"
KW2 = "کاردرمانی ذهنی کودکان آنلاین"
AUTHOR = "مهرناز افشار"
PHONE = "+989011922823"
OG_IMAGE = SITE + "/logo/og-cover.png"

# slug -> dict(title, desc, ogtype, crumb, imgalt)
PAGES = {
"index.html": dict(
  title="کاردرمانی ذهنی کودکان | " + BRAND,
  desc="کاردرمانی ذهنی کودکان به‌صورت آنلاین و در سراسر ایران، زیر نظر مهرناز افشار؛ دست‌ورزی، مهارت‌های شناختی، ادراک بینایی، پردازش شنیداری و رفتاردرمانی.",
  ogtype="website", crumb=None,
  imgalt="مرکز مغز و شناخت کودکان — کاردرمانی ذهنی کودکان آنلاین"),

"online.html": dict(
  title="کاردرمانی ذهنی کودکان آنلاین | جلسه‌ی آنلاین در سراسر ایران",
  desc="کاردرمانی ذهنی کودکان آنلاین در سراسر ایران؛ ارزیابی و جلسه‌ی آنلاین با مهرناز افشار — جلسه چطور برگزار می‌شود، برای چه کودکانی مناسب است و چطور نوبت بگیریم.",
  ogtype="article", crumb="کاردرمانی ذهنی کودکان آنلاین",
  imgalt="کاردرمانی ذهنی کودکان آنلاین در مرکز مغز و شناخت کودکان"),

"about.html": dict(
  title="مهرناز افشار، کاردرمانگر ذهنی کودکان | درباره‌ی ما",
  desc="مهرناز افشار، موسس مرکز مغز و شناخت کودکان و کاردرمانگر ذهنی کودکان با بیش از ۷ سال سابقه‌ی کار با کودکان اوتیسم، ADHD و اختلالات یادگیری.",
  ogtype="profile", crumb="درباره‌ی ما",
  imgalt="مهرناز افشار، کاردرمانگر ذهنی کودکان"),

"reserve.html": dict(
  title="رزرو نوبت کاردرمانی ذهنی کودکان آنلاین",
  desc="رزرو نوبت کاردرمانی ذهنی کودکان آنلاین؛ جلسه‌های ارزیابی، مشاوره و درمان از راه دور در سراسر ایران با کاردرمانگر مهرناز افشار.",
  ogtype="article", crumb="رزرو نوبت",
  imgalt="رزرو نوبت کاردرمانی ذهنی کودکان آنلاین"),

"fine-motor.html": dict(
  title="دست‌ورزی و ترسیم کودکان | کاردرمانی ذهنی کودکان",
  desc="دست‌ورزی و ترسیم در کاردرمانی ذهنی کودکان؛ نشانه‌های نیاز به کمک، مسیر جلسه‌ها و پنج تمرین پلکانی خانگی برای آماده‌کردن دست کودک برای نوشتن.",
  ogtype="article", crumb="دست‌ورزی و ترسیم",
  imgalt="دست‌ورزی و ترسیم در کاردرمانی ذهنی کودکان"),

"cognitive.html": dict(
  title="مهارت‌های شناختی کودک | کاردرمانی ذهنی کودکان",
  desc="توجه، حافظه و حل مسئله در کاردرمانی ذهنی کودکان؛ نشانه‌های نیاز به کمک، مسیر جلسه‌ها و تمرین‌های خانگی برای تقویت کارکردهای اجرایی کودک.",
  ogtype="article", crumb="مهارت‌های شناختی",
  imgalt="مهارت‌های شناختی کودک در کاردرمانی ذهنی کودکان"),

"visual-perception.html": dict(
  title="ادراک بینایی کودکان | کاردرمانی ذهنی کودکان",
  desc="ادراک بینایی در کاردرمانی ذهنی کودکان؛ قرینه‌نویسی، جاافتادن در رونویسی و ضعف حافظه‌ی دیداری — نشانه‌ها، مسیر جلسه‌ها و تمرین‌های خانگی.",
  ogtype="article", crumb="ادراک بینایی",
  imgalt="ادراک بینایی کودکان در کاردرمانی ذهنی کودکان"),

"auditory-processing.html": dict(
  title="پردازش شنیداری کودکان | کاردرمانی ذهنی کودکان",
  desc="پردازش شنیداری در کاردرمانی ذهنی کودکان؛ آگاهی واج‌شناختی، حافظه و توالی شنیداری — نشانه‌ها، مسیر جلسه‌ها و تمرین‌های خانگی برای پایه‌ی خواندن و املا.",
  ogtype="article", crumb="پردازش شنیداری",
  imgalt="پردازش شنیداری کودکان در کاردرمانی ذهنی کودکان"),

"social-skills.html": dict(
  title="مهارت‌های اجتماعی کودکان | کاردرمانی ذهنی کودکان",
  desc="مهارت‌های اجتماعی کودکان؛ دوست‌یابی، نوبت‌گیری، شناخت هیجان و حل تعارض — نشانه‌ها، مسیر جلسه‌ها و تمرین‌های خانگی در کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="مهارت‌های اجتماعی",
  imgalt="مهارت‌های اجتماعی کودکان در کاردرمانی ذهنی کودکان"),

"play-therapy.html": dict(
  title="بازی‌درمانی کودکان | کاردرمانی ذهنی کودکان",
  desc="بازی‌درمانی کودکان؛ تخلیه‌ی هیجانی، کاهش اضطراب و افزایش تحمل شکست — نشانه‌ها، مسیر جلسه‌ها و نکته‌های بازی در خانه.",
  ogtype="article", crumb="بازی‌درمانی",
  imgalt="بازی‌درمانی کودکان در کاردرمانی ذهنی کودکان"),

"perceptual-motor.html": dict(
  title="مهارت درکی‌ـ‌حرکتی کودکان | کاردرمانی ذهنی کودکان",
  desc="مهارت درکی‌ـ‌حرکتی کودکان؛ تعادل، هماهنگی دو طرف بدن، طرح‌ریزی حرکتی و جهت‌یابی — نشانه‌ها، مسیر جلسه‌ها و تمرین‌های خانگی.",
  ogtype="article", crumb="مهارت درکی‌ـ‌حرکتی",
  imgalt="مهارت درکی‌ـ‌حرکتی کودکان در کاردرمانی ذهنی کودکان"),

"school-readiness.html": dict(
  title="سنجش بدو ورود به مدرسه و آمادگی کودک | کاردرمانی ذهنی کودکان",
  desc="سنجش بدو ورود به مدرسه؛ در سنجش چه چیزی بررسی می‌شود، چطور کودک را آماده کنیم و پس از سنجش چه باید کرد — راهنمای کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="سنجش مدرسه",
  imgalt="سنجش بدو ورود به مدرسه و آمادگی کودک"),

"behavioral-therapy.html": dict(
  title="رفتاردرمانی کودکان | کاردرمانی ذهنی کودکان",
  desc="رفتاردرمانی کودکان؛ پیدا کردن علت رفتار، آموزش رفتار جایگزین، جدول ستاره و نظام تشویق در خانه — نشانه‌ها، مسیر جلسه‌ها و نکته‌های والدین.",
  ogtype="article", crumb="رفتاردرمانی",
  imgalt="رفتاردرمانی کودکان در کاردرمانی ذهنی کودکان"),

"fine-motor-game-1.html": dict(
  title="گلوله را به سبد برسان | تمرین ۱ دست‌ورزی",
  desc="بازی تعاملی پله‌ی یک دست‌ورزی؛ کشیدن گلوله‌های کاغذ به داخل سبد برای تمرین قدرت گرفتن و هدف‌گیری — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۱ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),

"fine-motor-game-2.html": dict(
  title="گیره را روی رنگش بگذار | تمرین ۲ دست‌ورزی",
  desc="بازی تعاملی پله‌ی دو دست‌ورزی؛ گذاشتن هر گیره روی نوار هم‌رنگش برای تمرین رها کردن دقیق — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۲ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),

"fine-motor-game-3.html": dict(
  title="مهره‌ها را به ترتیب نخ کن | تمرین ۳ دست‌ورزی",
  desc="بازی تعاملی پله‌ی سه دست‌ورزی؛ گذشتن از مهره‌ها به ترتیب و بدون بلندکردن انگشت — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۳ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),

"fine-motor-game-4.html": dict(
  title="روی خط ببر | تمرین ۴ دست‌ورزی",
  desc="بازی تعاملی پله‌ی چهار دست‌ورزی؛ حرکت روی خط راست، موجی و دایره با اندازه‌گیری دقت — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۴ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),

"fine-motor-game-5.html": dict(
  title="الگو را کپی کن | تمرین ۵ دست‌ورزی",
  desc="بازی تعاملی پله‌ی پنج دست‌ورزی؛ بازساختن الگوی خط‌ها روی شبکه‌ی نقطه‌ها — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۵ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),
}


import io, re, json, html, datetime

ORG_ID    = SITE + "/#organization"
WEBSITE_ID= SITE + "/#website"
PERSON_ID = SITE + "/#mehrnaz"

def url_of(slug):
    """نشانی عمومی هر صفحه.

    کلودفلر پیجز فایل about.html را روی /about سرو می‌کند و درخواستِ
    /about.html را با ۳۰۸ به همان‌جا می‌فرستد؛ پس نشانی بی‌پسوند تنها
    شکلی است که خودش تغییرمسیر نمی‌دهد و باید در canonical، og:url،
    شناسه‌های JSON-LD و نقشه‌ی سایت همان استفاده شود.
    """
    return SITE + "/" if slug == "index.html" else SITE + "/" + slug[:-len(".html")]

def esc(t):
    return html.escape(t, quote=True)

# ---------- FAQ: schema is generated FROM the visible markup so the two can never drift
FAQ_RE = re.compile(
    r'<details class="faq__item">\s*<summary>(.*?)</summary>\s*'
    r'<div class="faq__a">(.*?)</div>\s*</details>', re.S)

def strip_tags(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()

def faq_items(src):
    return [(strip_tags(q), strip_tags(a)) for q, a in FAQ_RE.findall(src)]

# ---------- JSON-LD builders
def org_graph():
    return [
        {"@type": "WebSite", "@id": WEBSITE_ID, "url": SITE + "/", "name": BRAND,
         "alternateName": "kidswellhub", "inLanguage": "fa-IR",
         "publisher": {"@id": ORG_ID}},
        {"@type": ["MedicalBusiness", "ProfessionalService"], "@id": ORG_ID,
         "name": BRAND, "alternateName": "kidswellhub", "url": SITE + "/",
         "description": "مرکز تخصصی " + KW1 + "؛ ارزیابی و درمان آنلاین در سراسر ایران، در حیطه‌های دست‌ورزی، "
                        "مهارت‌های شناختی، ادراک بینایی، پردازش شنیداری، مهارت‌های اجتماعی، بازی‌درمانی، "
                        "درکی‌ـ‌حرکتی، سنجش مدرسه و رفتاردرمانی.",
         "logo": {"@type": "ImageObject", "url": SITE + "/logo/kidswellhub-mark.svg"},
         "image": OG_IMAGE,
         "telephone": PHONE,
         "medicalSpecialty": "Pediatric",
         "priceRange": "$$",
         "availableLanguage": {"@type": "Language", "name": "فارسی", "alternateName": "fa"},
         "areaServed": {"@type": "Country", "name": "ایران"},
         "founder": {"@id": PERSON_ID},
         "employee": {"@id": PERSON_ID},
         "knowsAbout": [KW1, KW2, "کاردرمانی کودکان", "اوتیسم", "ADHD",
                        "اختلالات یادگیری", "ادراک بینایی", "پردازش شنیداری",
                        "دست‌ورزی و ترسیم", "رفتاردرمانی کودکان"],
         "hasOfferCatalog": {
             "@type": "OfferCatalog", "name": "خدمات " + KW1,
             "itemListElement": [
                 {"@type": "Offer", "itemOffered": {
                     "@type": "Service", "name": p["crumb"], "url": url_of(slug),
                     "serviceType": KW1, "provider": {"@id": ORG_ID},
                     "areaServed": {"@type": "Country", "name": "ایران"}}}
                 for slug, p in PAGES.items()
                 if slug not in ("index.html", "about.html", "reserve.html")
                 and not slug.startswith("fine-motor-game-")]}},
        {"@type": "Person", "@id": PERSON_ID, "name": AUTHOR,
         "jobTitle": "کاردرمانگر ذهنی کودکان",
         "description": "موسس " + BRAND + " و کاردرمانگر ذهنی کودکان با بیش از هفت سال سابقه‌ی کار "
                        "با کودکان اوتیسم، ADHD و اختلالات یادگیری.",
         "url": SITE + "/about",
         "image": SITE + "/logo/mehrnaz-afshar-cutout.webp",
         "worksFor": {"@id": ORG_ID},
         "knowsAbout": [KW1, "اوتیسم", "ADHD", "اختلالات یادگیری", "کاردرمانی کودکان"],
         "hasCredential": {"@type": "EducationalOccupationalCredential",
                           "credentialCategory": "کد نظام پزشکی", "identifier": "ک‑د ۳۲۸۹"}},
    ]

def breadcrumb(slug, p):
    items = [{"@type": "ListItem", "position": 1, "name": "خانه", "item": SITE + "/"}]
    if slug.startswith("fine-motor-game-"):
        items.append({"@type": "ListItem", "position": 2, "name": "دست‌ورزی و ترسیم",
                      "item": url_of("fine-motor.html")})
        items.append({"@type": "ListItem", "position": 3, "name": p["crumb"], "item": url_of(slug)})
    else:
        items.append({"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url_of(slug)})
    return {"@type": "BreadcrumbList", "@id": url_of(slug) + "#breadcrumb", "itemListElement": items}

def webpage(slug, p, src):
    page_type = {"about.html": "AboutPage", "reserve.html": "ContactPage"}.get(slug, "WebPage")
    if slug == "index.html":
        page_type = "WebPage"
    node = {"@type": page_type, "@id": url_of(slug) + "#webpage", "url": url_of(slug),
            "name": p["title"], "description": p["desc"], "inLanguage": "fa-IR",
            "isPartOf": {"@id": WEBSITE_ID}, "about": {"@id": ORG_ID},
            "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMAGE}}
    if slug != "index.html":
        node["breadcrumb"] = {"@id": url_of(slug) + "#breadcrumb"}
    return node

def service_node(slug, p):
    if slug == "online.html":
        name, desc = KW2, ("جلسه‌های ارزیابی و درمان " + KW1 + " به‌صورت آنلاین و از راه دور، "
                           "با برنامه‌ی اختصاصی و پیگیری تمرین‌های خانگی.")
        mode = "https://schema.org/OnlineEventAttendanceMode"
    else:
        name, desc, mode = p["crumb"] + " در " + KW1, p["desc"], None
    node = {"@type": "Service", "@id": url_of(slug) + "#service", "name": name,
            "description": desc, "serviceType": KW1, "url": url_of(slug),
            "provider": {"@id": ORG_ID}, "areaServed": {"@type": "Country", "name": "ایران"},
            "audience": {"@type": "PeopleAudience", "suggestedMinAge": 2, "suggestedMaxAge": 12}}
    if mode:
        node["serviceOutput"] = "برنامه‌ی اختصاصی کاردرمانی ذهنی و تمرین‌های خانگی"
        node["availableChannel"] = {"@type": "ServiceChannel",
                                    "serviceUrl": url_of(slug),
                                    "servicePhone": {"@type": "ContactPoint", "telephone": PHONE},
                                    "availableLanguage": {"@type": "Language", "name": "فارسی"}}
    return node

def faq_node(slug, src):
    items = faq_items(src)
    if not items:
        return None
    return {"@type": "FAQPage", "@id": url_of(slug) + "#faq",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def build_jsonld(slug, p, src):
    graph = []
    if slug == "index.html":
        graph += org_graph()
    graph.append(webpage(slug, p, src))
    if slug != "index.html":
        graph.append(breadcrumb(slug, p))
    if slug not in ("index.html", "about.html", "reserve.html") and not slug.startswith("fine-motor-game-"):
        graph.append(service_node(slug, p))
    f = faq_node(slug, src)
    if f:
        graph.append(f)
    return {"@context": "https://schema.org", "@graph": graph}

# ---------- head block
BLOCK_START = "<!-- سئو: آدرس یکتا، اشتراک‌گذاری و داده‌ی ساختاریافته -->"
BLOCK_END   = "<!-- پایان سئو -->"

def head_block(slug, p, src):
    u = url_of(slug)
    ld = json.dumps(build_jsonld(slug, p, src), ensure_ascii=False, indent=2)
    return f"""{BLOCK_START}
<link rel="canonical" href="{u}" />
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
<meta name="author" content="{esc(AUTHOR)}" />
<meta property="og:type" content="{p['ogtype']}" />
<meta property="og:site_name" content="{esc(BRAND)}" />
<meta property="og:locale" content="fa_IR" />
<meta property="og:url" content="{u}" />
<meta property="og:title" content="{esc(p['title'])}" />
<meta property="og:description" content="{esc(p['desc'])}" />
<meta property="og:image" content="{OG_IMAGE}" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="{esc(p['imgalt'])}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{esc(p['title'])}" />
<meta name="twitter:description" content="{esc(p['desc'])}" />
<meta name="twitter:image" content="{OG_IMAGE}" />
<meta name="twitter:image:alt" content="{esc(p['imgalt'])}" />
<link rel="manifest" href="site.webmanifest" />
<script type="application/ld+json">
{ld}
</script>
{BLOCK_END}"""

TITLE_RE = re.compile(r'<title>.*?</title>', re.S)
DESC_RE  = re.compile(r'<meta name="description" content=".*?" />', re.S)
OLD_BLOCK_RE = re.compile(re.escape(BLOCK_START) + r'.*?' + re.escape(BLOCK_END) + r'\n?', re.S)

for slug, p in PAGES.items():
    src = io.open(slug, encoding='utf-8').read()
    src = OLD_BLOCK_RE.sub('', src)                                  # اجرای دوباره، بدون تکرار
    assert TITLE_RE.search(src) and DESC_RE.search(src), slug

    block = head_block(slug, p, src)

    src = TITLE_RE.sub(lambda m: '<title>' + p['title'] + '</title>', src, count=1)
    src = DESC_RE.sub(lambda m: '<meta name="description" content="' + esc(p['desc']) + '" />',
                      src, count=1)
    src = src.replace('</head>', block + '\n</head>', 1)
    src = src.replace('styles.css?v=2', 'styles.css?v=3')
    src = src.replace('app.js?v=2', 'app.js?v=3').replace('games.js?v=2', 'games.js?v=3')

    io.open(slug, 'w', encoding='utf-8').write(src)
    print('ok', slug)

# ---------- نقشه‌ی سایت
today = datetime.date.today().isoformat()
PRIO = {"index.html": ("1.0", "weekly"), "online.html": ("0.9", "monthly"),
        "reserve.html": ("0.8", "monthly"), "about.html": ("0.8", "monthly")}

def prio(slug):
    if slug in PRIO:
        return PRIO[slug]
    if slug.startswith("fine-motor-game-"):
        return ("0.4", "yearly")
    return ("0.7", "monthly")

rows = []
for slug in PAGES:
    pr, cf = prio(slug)
    rows.append(f"""  <url>
    <loc>{url_of(slug)}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{cf}</changefreq>
    <priority>{pr}</priority>
  </url>""")

io.open('sitemap.xml', 'w', encoding='utf-8').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(rows) + "\n</urlset>\n")
print('ok sitemap.xml (%d نشانی)' % len(rows))
