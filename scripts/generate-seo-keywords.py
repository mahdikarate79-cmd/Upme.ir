#!/usr/bin/env python3
"""Generate expanded SEO keyword list for UpMe."""
import json
from itertools import product

TARGET = 8000
SITE = "upmee.site"

brands = [
    "UpMe", "upme", "UPMe", "UpME", "upME", "UPME", "Up Me", "up me", "UP ME",
    "apme", "ApMe", "APMe", "apMe", "APME", "Ap Me", "ap me", "Ap Me",
    "upmee", "UpMee", "UPMEE", "UpMeee", "upmee.site", "upme.ir", "upme app",
    "UpMe App", "upmeapp", "UpMeApp", "اپمی", "اپ می", "اپ‌می", "اپمي",
    "اپلیکیشن اپمی", "اپلیکیشن upme", "دانلود upme", "دانلود اپمی",
    "اپ upme", "اپ UpMe", "برنامه upme", "برنامه اپمی", "upme2025",
    "rubika upme", "روبیکا upme", "upme روبیکا",
]

persian_core = [
    "خودشناسی", "توسعه فردی", "مسیریابی شغلی", "مسیریابی تحصیلی", "تست شخصیت",
    "استعدادیابی", "انتخاب رشته", "تغییر شغل", "رشد فردی", "موفقیت شغلی",
    "مشاوره شغلی", "مشاوره تحصیلی", "تست MBTI", "تست هالند", "تیپ شخصیتی",
    "کشف استعداد", "مسیر شغلی", "مسیر تحصیلی", "هدف گذاری", "خودآگاهی",
    "برنامه ریزی تحصیلی", "انتخاب رشته دانشگاه", "تغییر مسیر شغلی",
    "مهارت سخت", "مهارت نرم", "رزومه نویسی", "مصاحبه شغلی", "استخدام",
    "کارآفرینی", "فریلنسری", "دورکاری", "پیشرفت شغلی", "موفقیت تحصیلی",
    "کنکور", "انتخاب رشته کنکور", "مشاغل پرطرفدار", "بازار کار ایران",
    "هوش مصنوعی", "دستیار هوش مصنوعی", "کوچینگ", "منتورینگ", "انگیزه",
    "سلامت روان", "اعتماد به نفس", "تمرکز", "مدیریت زمان", "برنامه ریزی درسی",
    "یادگیری", "مهارت آموزی", "شبکه سازی", "لینکدین", "برند شخصی",
    "دانلود اپلیکیشن", "دانلود رایگان", "اپلیکیشن موفقیت", "اپلیکیشن خودشناسی",
    "بهترین اپلیکیشن خودشناسی", "مسیریاب هوشمند", "مسیریاب شغلی", "مسیریاب تحصیلی",
    "تست خودشناسی", "آزمون شخصیت", "شخصیت شناسی", "تحلیل شخصیت", "ارزش های شغلی",
    "شغل رویایی", "شغل مناسب", "مشاغل مناسب", "پیدا کردن مسیر زندگی",
    "راهنمای مسیر شغلی", "مشاوره شغلی آنلاین", "مشاوره شغلی رایگان",
    "توسعه مهارت", "رشد شخصی", "موفقیت در زندگی", "هدف زندگی", "رسالت فردی",
    "انتخاب شغل", "شغل آینده", "آینده شغلی", "بازار کار", "ارتقای شغلی",
    "تغییر شغل در 30 سالگی", "تغییر شغل در 40 سالگی", "سردرگمی شغلی",
    "سردرگمی تحصیلی", "دانشجوی سرگردان", "انتخاب رشته دبیرستان",
    "گوگل پلی", "اپ استور", "کافه بازار", "بازار", "دانلود apk", "روبیکا",
    "اینستاگرام", "تلگرام", "شبکه اجتماعی", "اپ ایرانی", "اپلیکیشن ایرانی",
]

cities = [
    "تهران", "اصفهان", "مشهد", "شیراز", "تبریز", "کرج", "اهواز", "قم", "کرمانشاه",
    "رشت", "یزد", "اراک", "زاهدان", "همدان", "کرمان", "اردبیل", "بندرعباس", "قزوین",
    "ایران", "سراسر ایران", "کل کشور",
]

jobs = [
    "برنامه نویس", "طراح گرافیک", "مدیر محصول", "تحلیلگر داده", "دیجیتال مارکتر",
    "روانشناس", "مشاور", "معلم", "پرستار", "پزشک", "مهندس", "حسابدار", "وکیل",
    "معمار", "فیلمبردار", "تدوینگر", "نویسنده", "مترجم", "فروشنده", "مدیر فروش",
    "مدیر منابع انسانی", "طراح UI", "طراح UX", "توسعه دهنده", "بک اند", "فرانت اند",
    "علم داده", "امنیت سایبری", "مدیریت پروژه", "کارشناس SEO", "کپی رایتر",
]

english = [
    "self discovery", "career path", "career guidance", "personality test", "MBTI test",
    "Holland test", "career counseling", "life coaching", "personal development",
    "self awareness", "job search", "resume", "interview skills", "freelance",
    "remote work", "startup", "download app", "free app", "best career app",
    "Iran app", "Persian app", "self help app", "motivation app", "success app",
]

questions = [
    "چطور خودم رو بشناسم", "چطور مسیر شغلی پیدا کنم", "چه رشته ای بخونم",
    "کدوم شغل برام مناسبه", "چطور استعدادم رو پیدا کنم", "بهترین تست شخصیت",
    "تست شخصیت رایگان", "مشاوره شغلی رایگان", "اپ انتخاب رشته",
    "دانلود اپ خودشناسی", "اپلیکیشن موفقیت ایرانی", "بهترین اپ ایرانی",
    "چطور شغل عوض کنم", "چطور اعتماد به نفس بالا ببرم", "چطور هدف گذاری کنم",
]

modifiers = [
    "رایگان", "بهترین", "معتبر", "علمی", "حرفه ای", "آنلاین", "ایرانی",
    "فارسی", "جدید", "2025", "2026", "پیشنهاد", "راهنمای", "آموزش",
    "دانلود", "نصب", "معرفی", "بررسی", "نقد و بررسی", "امتیاز",
]

keywords = set()

for item in brands + persian_core + cities + jobs + english + questions:
    keywords.add(item)

for b in brands:
    for k in persian_core:
        keywords.add(f"{b} {k}")
        keywords.add(f"{k} {b}")

for city in cities:
    for k in persian_core[:40]:
        keywords.add(f"{k} {city}")
        keywords.add(f"UpMe {city}")
        keywords.add(f"اپمی {city}")

for job in jobs:
    keywords.add(f"شغل {job}")
    keywords.add(f"مسیر شغلی {job}")
    keywords.add(f"UpMe {job}")
    for b in ["upme", "اپمی", "apme"]:
        keywords.add(f"{b} {job}")

for q in questions:
    keywords.add(q)
    for b in brands[:12]:
        keywords.add(f"{b} {q}")

for k in persian_core:
    for m in modifiers:
        keywords.add(f"{k} {m}")
        keywords.add(f"{m} {k}")

for site in [SITE, "upme.ir", "upmee", "rubika.ir/upme2025"]:
    for k in persian_core[:35]:
        keywords.add(f"{k} {site}")

extras = [
    "اپلیکیشن", "برنامه", "نرم افزار", "سایت", "وب اپ", "اندروید", "ios",
    "موبایل", "هوشمند", "آنلاین", "فارسی", "ایرانی", "اپ", "نصب", "رایگان",
]
i = 0
while len(keywords) < TARGET:
    for b in brands:
        for e in extras:
            keywords.add(f"{b} {e}")
            keywords.add(f"{e} {b}")
        if len(keywords) >= TARGET:
            break
    for a, c in product(persian_core[:30], modifiers[:10]):
        keywords.add(f"{a} {c}")
    i += 1
    if i > 80:
        break

keywords = sorted(keywords)[:TARGET]

with open("/workspace/seo-keywords.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(keywords))

with open("/workspace/seo-keywords.json", "w", encoding="utf-8") as f:
    json.dump({"keywords": keywords, "count": len(keywords), "site": SITE}, f, ensure_ascii=False, indent=2)

# SEO content HTML
lines = [
    '<div class="seo-content" aria-hidden="true">',
    '<h1>UpMe upme apme اپمی — اپلیکیشن خودشناسی و مسیریاب شغلی ایران | rubika.ir/upme2025</h1>',
    '<section><h2>شبکه‌های اجتماعی UpMe</h2><ul>',
    '<li>روبیکا UpMe: https://rubika.ir/upme2025</li>',
    '<li>تلگرام UpMe: https://t.me/UpMeee</li>',
    '<li>اینستاگرام UpMe</li>',
    '</ul></section>',
]

chunk = max(1, len(keywords) // 16)
titles = [
    "خودشناسی و توسعه فردی", "مسیریابی شغلی", "مسیریابی تحصیلی و کنکور",
    "تست شخصیت MBTI هالند", "دانلود اپلیکیشن", "مهارت و موفقیت شغلی",
    "هوش مصنوعی و فناوری", "شهرهای ایران", "مشاغل و حرفه‌ها",
    "برند UpMe upme apme", "کلیدواژه انگلیسی", "سوالات پرتکرار",
    "روبیکا و شبکه اجتماعی", "مارکت اندروید ios بازار", "کنکور و دانشگاه",
    "کلیدواژه‌های تکمیلی",
]
for idx, title in enumerate(titles):
    start = idx * chunk
    end = min(start + chunk, len(keywords))
    if start >= len(keywords):
        break
    lines.append(f'<section><h2>{title}</h2><ul>')
    for kw in keywords[start:end]:
        lines.append(f'<li>{kw}</li>')
    lines.append('</ul></section>')
lines.append('</div>')

with open("/workspace/seo-content-snippet.html", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

meta = ",".join(keywords)
with open("/workspace/seo-meta-keywords.txt", "w", encoding="utf-8") as f:
    f.write(meta)

print("keywords:", len(keywords))
print("meta chars:", len(meta))
print("seo content lines:", len(lines))
