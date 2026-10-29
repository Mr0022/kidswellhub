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
AUTHOR = BRAND
PHONE = "+989011922823"
# ?v=N: پس از ساختن دوباره‌ی تصویر یکی بالا ببرید تا شبکه‌های اجتماعی نسخه‌ی تازه را بگیرند
OG_IMAGE = SITE + "/logo/og-cover.png?v=2"

# مسیر فایل -> dict(title, desc, ogtype, crumb, imgalt)
# نشانی عمومی هر فایل بی‌پسوند است (Cloudflare Pages ‎/about.html را به ‎/about می‌برد): url_of پایین
PAGES = {
"index.html": dict(
  title="کاردرمانی ذهنی کودکان آنلاین | " + BRAND,
  desc="کاردرمانی ذهنی کودکان آنلاین در سراسر ایران؛ دست‌ورزی، مهارت‌های شناختی، ادراک بینایی، پردازش شنیداری، بازی‌درمانی و رفتاردرمانی. رزرو نوبت.",
  ogtype="website", crumb=None,
  imgalt="مرکز مغز و شناخت کودکان — کاردرمانی ذهنی کودکان آنلاین در سراسر ایران"),

"online.html": dict(
  title="کاردرمانی ذهنی کودکان آنلاین | جلسه‌ی آنلاین در سراسر ایران",
  desc="کاردرمانی ذهنی کودکان آنلاین در سراسر ایران؛ جلسه چطور برگزار می‌شود، برای چه کودکانی مناسب است، چه وسایلی لازم است و چطور نوبت بگیریم.",
  ogtype="article", crumb="کاردرمانی ذهنی کودکان آنلاین",
  imgalt="کاردرمانی ذهنی کودکان آنلاین در مرکز مغز و شناخت کودکان"),

"about.html": dict(
  title="درباره‌ی ما | تیم " + BRAND,
  desc="تیم " + BRAND + "؛ کاردرمانگران ذهنی کودکان با ارزیابی دقیق، برنامه‌ی بازی‌محور و همراهی خانواده، در جلسه‌های آنلاین در سراسر ایران.",
  ogtype="website", crumb="درباره‌ی ما",
  imgalt="تیم " + BRAND + " — کاردرمانی ذهنی کودکان"),

"faq.html": dict(
  title="سوالات متداول رشد کودک و کاردرمانی ذهنی کودکان",
  desc="پاسخ پرسش‌های رایج والدین درباره‌ی کاردرمانی ذهنی کودکان، رشد و تکامل، صفحه‌نمایش و خواب، مدرسه و تکالیف، رفتار و احساسات کودک و نحوه‌ی رزرو نوبت.",
  ogtype="article", crumb="سوالات متداول",
  imgalt="سوالات متداول درباره‌ی رشد کودک و کاردرمانی ذهنی کودکان"),

"reserve.html": dict(
  title="رزرو نوبت کاردرمانی ذهنی کودکان آنلاین و تماس با ما",
  desc="رزرو نوبت کاردرمانی ذهنی کودکان آنلاین در سراسر ایران؛ ارزیابی، درمان و مشاوره‌ی والدین از خانه. برای رزرو یا هر پرسشی با ۰۹۰۱ ۱۹۲ ۲۸ ۲۳ تماس بگیرید.",
  ogtype="article", crumb="رزرو نوبت",
  imgalt="رزرو نوبت کاردرمانی ذهنی کودکان آنلاین"),

"services/fine-motor.html": dict(
  title="دست‌ورزی و ترسیم کودکان | کاردرمانی ذهنی کودکان آنلاین",
  desc="دست‌ورزی و ترسیم در کاردرمانی ذهنی کودکان آنلاین؛ نشانه‌های نیاز به کمک، مسیر جلسه‌ها و پنج تمرین پلکانی خانگی برای آماده‌کردن دست کودک برای نوشتن.",
  ogtype="article", crumb="دست‌ورزی و ترسیم",
  imgalt="دست‌ورزی و ترسیم در کاردرمانی ذهنی کودکان"),

"services/cognitive.html": dict(
  title="مهارت‌های شناختی کودک | کاردرمانی ذهنی کودکان آنلاین",
  desc="توجه، حافظه و حل مسئله در کاردرمانی ذهنی کودکان آنلاین؛ نشانه‌های نیاز به کمک، مسیر جلسه‌ها و تمرین‌های خانگی برای تقویت کارکردهای اجرایی کودک.",
  ogtype="article", crumb="مهارت‌های شناختی",
  imgalt="مهارت‌های شناختی کودک در کاردرمانی ذهنی کودکان"),

"services/visual-perception.html": dict(
  title="ادراک بینایی کودکان | کاردرمانی ذهنی کودکان آنلاین",
  desc="ادراک بینایی در کاردرمانی ذهنی کودکان آنلاین؛ قرینه‌نویسی، جاافتادن در رونویسی و ضعف حافظه‌ی دیداری — نشانه‌ها، مسیر جلسه‌ها و تمرین‌های خانگی.",
  ogtype="article", crumb="ادراک بینایی",
  imgalt="ادراک بینایی کودکان در کاردرمانی ذهنی کودکان"),

"services/auditory-processing.html": dict(
  title="پردازش شنیداری کودکان | کاردرمانی ذهنی کودکان آنلاین",
  desc="پردازش شنیداری در کاردرمانی ذهنی کودکان آنلاین؛ آگاهی واج‌شناختی، حافظه و توالی شنیداری — نشانه‌ها، مسیر جلسه‌ها و تمرین‌های خانگی برای خواندن و املا.",
  ogtype="article", crumb="پردازش شنیداری",
  imgalt="پردازش شنیداری کودکان در کاردرمانی ذهنی کودکان"),

"services/social-skills.html": dict(
  title="مهارت‌های اجتماعی کودکان | کاردرمانی ذهنی کودکان آنلاین",
  desc="مهارت‌های اجتماعی کودکان؛ دوست‌یابی، نوبت‌گیری، شناخت هیجان و حل تعارض — نشانه‌ها، مسیر جلسه‌ها و تمرین‌های خانگی در کاردرمانی ذهنی کودکان آنلاین.",
  ogtype="article", crumb="مهارت‌های اجتماعی",
  imgalt="مهارت‌های اجتماعی کودکان در کاردرمانی ذهنی کودکان"),

"services/play-therapy.html": dict(
  title="بازی‌درمانی کودکان | کاردرمانی ذهنی کودکان آنلاین",
  desc="بازی‌درمانی در کاردرمانی ذهنی کودکان آنلاین؛ تخلیه‌ی هیجانی، کاهش اضطراب و افزایش تحمل شکست — نشانه‌ها، مسیر جلسه‌ها و نکته‌های بازی در خانه.",
  ogtype="article", crumb="بازی‌درمانی",
  imgalt="بازی‌درمانی کودکان در کاردرمانی ذهنی کودکان"),

"services/perceptual-motor.html": dict(
  title="مهارت درکی‌ـ‌حرکتی کودکان | کاردرمانی ذهنی کودکان آنلاین",
  desc="مهارت درکی‌ـ‌حرکتی کودکان؛ تعادل، هماهنگی دو طرف بدن، طرح‌ریزی حرکتی و جهت‌یابی — نشانه‌ها، مسیر جلسه‌ها و تمرین‌های خانگی در کاردرمانی ذهنی کودکان آنلاین.",
  ogtype="article", crumb="مهارت درکی‌ـ‌حرکتی",
  imgalt="مهارت درکی‌ـ‌حرکتی کودکان در کاردرمانی ذهنی کودکان"),

"services/school-readiness.html": dict(
  title="سنجش بدو ورود به مدرسه | کاردرمانی ذهنی کودکان آنلاین",
  desc="سنجش بدو ورود به مدرسه؛ چه چیزی بررسی می‌شود، چطور کودک را آماده کنیم و پس از سنجش چه باید کرد — راهنمای کاردرمانی ذهنی کودکان آنلاین.",
  ogtype="article", crumb="سنجش مدرسه",
  imgalt="سنجش بدو ورود به مدرسه و آمادگی کودک"),

"services/behavioral-therapy.html": dict(
  title="رفتاردرمانی کودکان | کاردرمانی ذهنی کودکان آنلاین",
  desc="رفتاردرمانی کودکان؛ پیدا کردن علت رفتار، رفتار جایگزین، جدول ستاره و تشویق در خانه — نشانه‌ها، مسیر جلسه‌ها و نکته‌های والدین در کاردرمانی ذهنی کودکان آنلاین.",
  ogtype="article", crumb="رفتاردرمانی",
  imgalt="رفتاردرمانی کودکان در کاردرمانی ذهنی کودکان"),

"services/fine-motor-game-1.html": dict(
  title="گلوله را به سبد برسان | تمرین ۱ دست‌ورزی",
  desc="بازی تعاملی پله‌ی یک دست‌ورزی؛ کشیدن گلوله‌های کاغذ به داخل سبد برای تمرین قدرت گرفتن و هدف‌گیری — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۱ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),

"services/fine-motor-game-2.html": dict(
  title="گیره را روی رنگش بگذار | تمرین ۲ دست‌ورزی",
  desc="بازی تعاملی پله‌ی دو دست‌ورزی؛ گذاشتن هر گیره روی نوار هم‌رنگش برای تمرین رها کردن دقیق — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۲ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),

"services/fine-motor-game-3.html": dict(
  title="مهره‌ها را به ترتیب نخ کن | تمرین ۳ دست‌ورزی",
  desc="بازی تعاملی پله‌ی سه دست‌ورزی؛ گذشتن از مهره‌ها به ترتیب و بدون بلندکردن انگشت — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۳ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),

"services/fine-motor-game-4.html": dict(
  title="روی خط ببر | تمرین ۴ دست‌ورزی",
  desc="بازی تعاملی پله‌ی چهار دست‌ورزی؛ حرکت روی خط راست، موجی و دایره با اندازه‌گیری دقت — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۴ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),

"services/fine-motor-game-5.html": dict(
  title="الگو را کپی کن | تمرین ۵ دست‌ورزی",
  desc="بازی تعاملی پله‌ی پنج دست‌ورزی؛ بازساختن الگوی خط‌ها روی شبکه‌ی نقطه‌ها — تمرین خانگی کاردرمانی ذهنی کودکان.",
  ogtype="article", crumb="تمرین ۵ دست‌ورزی",
  imgalt="تمرین تعاملی دست‌ورزی کودکان"),

"articles/index.html": dict(
  title="مقالات کاردرمانی ذهنی کودکان | راهنمای والدین",
  desc="مقاله‌های آموزشی مرکز مغز و شناخت کودکان برای والدین: کاردرمانی کودکان و نشانه‌های نیاز به آن، دست‌ورزی و دست‌خط، لباس پوشیدن، غذا خوردن و برنامه‌ی تصویری روزانه.",
  ogtype="website", crumb="مقالات",
  imgalt="مقاله‌های آموزشی کاردرمانی ذهنی کودکان برای والدین"),

# مقاله‌ها: published تاریخ انتشار است و image تصویر اشتراک‌گذاری خودِ مقاله
# (همان تصویر شاخص، به PNG؛ چون شبکه‌های اجتماعی SVG را نشان نمی‌دهند).
# ترتیب مقاله‌ها همان ترتیب کارت‌ها در articles.html است (فهرست ItemList صفحه‌ی مقالات)
"articles/pediatric-occupational-therapy.html": dict(
  title="کاردرمانی کودکان چیست؟ راهنمای کامل برای والدین",
  desc="کاردرمانی کودکان چیست، برای چه کودکانی لازم است و جلسه‌ها چطور پیش می‌رود؟ راهنمای کامل والدین: حیطه‌های درمان، نشانه‌های هر سن، ارزیابی و تمرین در خانه.",
  ogtype="article", crumb="کاردرمانی کودکان چیست؟", parent="articles/index.html", published="2026-10-29",
  image="images/articles/pediatric-ot-cover.png",
  imgalt="وسایل اتاق کاردرمانی کودکان: توپ درمانی، مکعب، پازل و مهره"),

"articles/occupational-therapy-signs.html": dict(
  title="آیا کودکم به کاردرمانی نیاز دارد؟ نشانه‌هایی که ارزش بررسی دارند",
  desc="نشانه‌هایی که ممکن است کودک از کاردرمانی سود ببرد: دشواری در لباس پوشیدن، دست‌خط، غذا خوردن، بازی، هماهنگی حرکتی و روال روزانه؛ و چرا یک نشانه به‌تنهایی تشخیص نیست.",
  ogtype="article", crumb="آیا کودکم به کاردرمانی نیاز دارد؟", parent="articles/index.html", published="2026-10-29",
  image="images/articles/ot-signs-cover.png",
  imgalt="وسایل کارهای روزمره‌ی کودک — لباس، مداد، قاشق، توپ و مکعب — زیر ذره‌بین"),

"articles/fine-motor-activities.html": dict(
  title="۱۵ فعالیت کاردرمانی برای تقویت مهارت‌های حرکتی ظریف کودک",
  desc="۱۵ فعالیت ساده‌ی کاردرمانی با وسایل خانه برای تقویت قدرت دست، گرفتن دقیق و آمادگی نوشتن کودک؛ از خمیربازی و گیره‌ی لباس تا قیچی‌کاری و سینی نمک.",
  ogtype="article", crumb="۱۵ فعالیت برای مهارت‌های حرکتی ظریف", parent="articles/index.html", published="2026-10-29",
  image="images/articles/fine-motor-cover.png",
  imgalt="وسایل تمرین دست‌ورزی کودک: گیره‌ی لباس، خمیر بازی، قیچی و انبرک"),

"articles/pencil-grip-handwriting.html": dict(
  title="چگونه گرفتن مداد و دست‌خط کودک را بهتر کنیم؟",
  desc="مراحل رشد گرفتن مداد، نشانه‌های مشکل و راه‌های عملی کاردرمانی برای بهتر شدن دست‌خط کودک: ابزار کوتاه، ترفند نیشگون و چرخش، نشستن ۹۰-۹۰-۹۰ و سطح شیب‌دار.",
  ogtype="article", crumb="گرفتن مداد و دست‌خط کودک", parent="articles/index.html", published="2026-10-29",
  image="images/articles/pencil-grip-cover.png",
  imgalt="دفتر باز با دست‌خط و مداد با رابط مثلثی"),

"articles/dressing-skills.html": dict(
  title="چگونه به کودک یاد بدهیم خودش لباس بپوشد؟ راهنمای کاردرمانی",
  desc="آموزش لباس پوشیدن به کودک با روش‌های کاردرمانی: انتظار هر سن، یاد دادن از قدم آخر، ترفند تی‌شرت و کاپشن، تمرین دکمه، زیپ و بند کفش و نکته‌های صبح‌های شلوغ.",
  ogtype="article", crumb="آموزش لباس پوشیدن به کودک", parent="articles/index.html", published="2026-10-29",
  image="images/articles/dressing-cover.png",
  imgalt="لباس‌های کودک روی بند رخت و یک جفت کفش بنددار"),

"articles/feeding-skills.html": dict(
  title="مهارت‌های غذا خوردن در کودکان: کاردرمانی چطور می‌تواند کمک کند؟",
  desc="کاردرمانی تغذیه‌ی کودکان: رشد مهارت خودخوری در هر سن، کار با قاشق و چنگال و لیوان، نشستن درست سر سفره، حساسیت به غذا و اینکه چه وقت باید سراغ پزشک یا کاردرمانگر رفت.",
  ogtype="article", crumb="مهارت‌های غذا خوردن کودک", parent="articles/index.html", published="2026-10-29",
  image="images/articles/feeding-cover.png",
  imgalt="سفره‌ی کودک با بشقاب سه‌قسمتی، قاشق و چنگال دسته‌کلفت و لیوان دودسته"),

"articles/visual-schedule.html": dict(
  title="برنامه‌ی تصویری برای کودکان: چطور کارهای روزانه را آسان‌تر کنیم؟",
  desc="برنامه‌ی تصویری روزانه برای کودک: انواع و روش ساخت، تخته‌ی «اول‌ـ‌بعد»، زمان‌سنج دیداری و روال‌های قابل‌پیش‌بینی برای همکاری بیشتر و جابه‌جایی‌های آرام‌تر میان کارها.",
  ogtype="article", crumb="برنامه‌ی تصویری برای کودکان", parent="articles/index.html", published="2026-10-29",
  image="images/articles/visual-schedule-cover.png",
  imgalt="تخته‌ی برنامه‌ی تصویری روزانه‌ی کودک با کارت‌های بیدار شدن، مسواک، لباس، صبحانه و مدرسه"),
}


import io, re, json, html, datetime, subprocess

ORG_ID    = SITE + "/#organization"
# نام‌های دیگری که مردم برند را با آن جست‌وجو می‌کنند (نام سایت در نتیجه‌ی گوگل از این‌ها انتخاب می‌شود)
ALT_NAMES = ["مرکز مغز و شناخت", "kidswellhub"]
WEBSITE_ID= SITE + "/#website"

# صفحه‌هایی که خدمت درمانی نیستند (بازی‌های دست‌ورزی و مقاله‌ها هم جداگانه کنار گذاشته می‌شوند)
NOT_SERVICE = ("index.html", "about.html", "reserve.html", "faq.html", "articles/index.html")

ARTICLES = [slug for slug, p in PAGES.items() if p.get("published")]

def is_service(slug):
    return (slug not in NOT_SERVICE and slug not in ARTICLES
            and not slug.startswith("services/fine-motor-game-"))

def url_of(slug):
    """index.html → نشانی پوشه با / پایانی؛ بقیه بدون ‎.html (services/cognitive.html → /services/cognitive)"""
    if slug.endswith("index.html"):
        return SITE + "/" + slug[:-len("index.html")]
    return SITE + "/" + slug[:-len(".html")]

def image_of(p):
    return SITE + "/" + p["image"] if p.get("image") else OG_IMAGE

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
         "alternateName": ALT_NAMES, "inLanguage": "fa-IR",
         "publisher": {"@id": ORG_ID}},
        {"@type": ["MedicalBusiness", "ProfessionalService"], "@id": ORG_ID,
         "name": BRAND, "alternateName": ALT_NAMES, "url": SITE + "/",
         "slogan": KW2 + " در سراسر ایران",
         "description": "مرکز تخصصی " + KW1 + "؛ ارزیابی و درمان آنلاین در سراسر ایران در حیطه‌های دست‌ورزی، "
                        "مهارت‌های شناختی، ادراک بینایی، پردازش شنیداری، مهارت‌های اجتماعی، بازی‌درمانی، "
                        "درکی‌ـ‌حرکتی، سنجش مدرسه و رفتاردرمانی.",
         "logo": {"@type": "ImageObject", "url": SITE + "/logo/kidswellhub-mark.svg"},
         "image": OG_IMAGE,
         "telephone": PHONE,
         "medicalSpecialty": "Pediatric",
         "priceRange": "$$",
         "availableLanguage": {"@type": "Language", "name": "فارسی", "alternateName": "fa"},
         "areaServed": {"@type": "Country", "name": "ایران"},
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
                 if is_service(slug)]}},
    ]

def breadcrumb(slug, p):
    items = [{"@type": "ListItem", "position": 1, "name": "خانه", "item": SITE + "/"}]
    if slug.startswith("services/fine-motor-game-"):
        items.append({"@type": "ListItem", "position": 2, "name": "دست‌ورزی و ترسیم",
                      "item": url_of("services/fine-motor.html")})
        items.append({"@type": "ListItem", "position": 3, "name": p["crumb"], "item": url_of(slug)})
    elif p.get("parent"):
        items.append({"@type": "ListItem", "position": 2, "name": PAGES[p["parent"]]["crumb"],
                      "item": url_of(p["parent"])})
        items.append({"@type": "ListItem", "position": 3, "name": p["crumb"], "item": url_of(slug)})
    else:
        items.append({"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url_of(slug)})
    return {"@type": "BreadcrumbList", "@id": url_of(slug) + "#breadcrumb", "itemListElement": items}

def webpage(slug, p, src):
    page_type = {"about.html": "AboutPage", "reserve.html": "ContactPage",
                 "articles/index.html": "CollectionPage"}.get(slug, "WebPage")
    if slug == "index.html":
        page_type = "WebPage"
    node = {"@type": page_type, "@id": url_of(slug) + "#webpage", "url": url_of(slug),
            "name": p["title"], "description": p["desc"], "inLanguage": "fa-IR",
            "isPartOf": {"@id": WEBSITE_ID}, "about": {"@id": ORG_ID},
            "primaryImageOfPage": {"@type": "ImageObject", "url": image_of(p)}}
    if slug != "index.html":
        node["breadcrumb"] = {"@id": url_of(slug) + "#breadcrumb"}
    if slug == "articles/index.html":
        node["mainEntity"] = {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": k, "url": url_of(a), "name": PAGES[a]["title"]}
            for k, a in enumerate(ARTICLES, 1)]}
    return node

def article_node(slug, p):
    return {"@type": "BlogPosting", "@id": url_of(slug) + "#article",
            "headline": p["title"], "description": p["desc"], "inLanguage": "fa-IR",
            "image": image_of(p), "datePublished": p["published"],
            "dateModified": p.get("modified", p["published"]),
            "author": {"@type": "Organization", "@id": ORG_ID, "name": BRAND, "url": SITE + "/"},
            "publisher": {"@id": ORG_ID},
            "mainEntityOfPage": {"@id": url_of(slug) + "#webpage"},
            "isPartOf": {"@id": url_of(p["parent"]) + "#webpage"}}

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
    if is_service(slug):
        graph.append(service_node(slug, p))
    if slug in ARTICLES:
        graph.append(article_node(slug, p))
    f = faq_node(slug, src)
    if f:
        graph.append(f)
    return {"@context": "https://schema.org", "@graph": graph}

# ---------- head block
BLOCK_START = "<!-- سئو: آدرس یکتا، اشتراک‌گذاری و داده‌ی ساختاریافته -->"
BLOCK_END   = "<!-- پایان سئو -->"

def head_block(slug, p, src):
    u = url_of(slug)
    img = image_of(p)
    ld = json.dumps(build_jsonld(slug, p, src), ensure_ascii=False, indent=2)
    published = (f'\n<meta property="article:published_time" content="{p["published"]}" />'
                 if p.get("published") else "")
    return f"""{BLOCK_START}
<link rel="canonical" href="{u}" />
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
<meta name="author" content="{esc(AUTHOR)}" />
<meta property="og:type" content="{p['ogtype']}" />
<meta property="og:site_name" content="{esc(BRAND)}" />
<meta property="og:locale" content="fa_IR" />
<meta property="og:url" content="{u}" />
<meta property="og:title" content="{esc(p['title'])}" />
<meta property="og:description" content="{esc(p['desc'])}" />{published}
<meta property="og:image" content="{img}" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="{esc(p['imgalt'])}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{esc(p['title'])}" />
<meta name="twitter:description" content="{esc(p['desc'])}" />
<meta name="twitter:image" content="{img}" />
<meta name="twitter:image:alt" content="{esc(p['imgalt'])}" />
<link rel="manifest" href="/site.webmanifest" />
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
    if slug.startswith("services/fine-motor-game-"):
        return ("0.4", "yearly")
    return ("0.7", "monthly")

def lastmod(slug):
    """تاریخ آخرین تغییر واقعی هر صفحه، تا گوگل به lastmod اعتماد کند: اگر فایل تغییر
    ثبت‌نشده دارد امروز، وگرنه تاریخ آخرین commit همان فایل"""
    try:
        git = lambda *a: subprocess.run(("git",) + a, capture_output=True, text=True).stdout.strip()
        if not git("status", "--porcelain", "--", slug):
            return git("log", "-1", "--format=%cs", "--", slug) or today
    except OSError:
        pass
    return today

rows = []
for slug, p in PAGES.items():
    pr, cf = prio(slug)
    img = (f"""
    <image:image>
      <image:loc>{image_of(p)}</image:loc>
    </image:image>""" if p.get("image") else "")
    rows.append(f"""  <url>
    <loc>{url_of(slug)}</loc>
    <lastmod>{lastmod(slug)}</lastmod>
    <changefreq>{cf}</changefreq>
    <priority>{pr}</priority>{img}
  </url>""")

io.open('sitemap.xml', 'w', encoding='utf-8').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    + "\n".join(rows) + "\n</urlset>\n")
print('ok sitemap.xml (%d نشانی)' % len(rows))
