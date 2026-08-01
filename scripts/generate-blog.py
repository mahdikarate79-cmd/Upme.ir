#!/usr/bin/env python3
"""Generate blog HTML pages for UpMe."""
from pathlib import Path

SITE = "https://upmee.site"

NAV = """
    <a href="#main-content" class="skip-link">پرش به محتوای اصلی</a>
    <header>
        <nav aria-label="ناوبری اصلی">
            <div class="logo">
                <a href="/" class="logo-link" aria-label="UpMe - صفحه اصلی">
                    <span class="logo-text">Me</span>
                    <span class="logo-dot" aria-hidden="true"></span>
                    <span class="logo-text logo-thin">Up</span>
                    <span class="logo-underline"></span>
                </a>
            </div>
            <button type="button" id="nav-toggle" class="nav-toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="منو">☰</button>
            <div class="nav-right" id="nav-menu">
                <div class="nav-links">
                    <a href="/#features">امکانات</a>
                    <a href="/blog/">بلاگ</a>
                    <a href="/#cta">دانلود</a>
                </div>
                <a href="https://upmee.site/app/upme.apk" target="_blank" class="nav-btn" onclick="trackDownload()" rel="noopener noreferrer">دانلود</a>
            </div>
        </nav>
    </header>
"""

FOOTER = """
    <footer role="contentinfo">
        <div class="footer-social">
            <a href="https://www.instagram.com/p/DZf5ZcBxWxy/?igsh=MTNkdXNwcTZ1dzI5bQ==" target="_blank" class="social-link" rel="noopener noreferrer">اینستاگرام</a>
            <a href="https://t.me/UpMeee" target="_blank" class="social-link" rel="noopener noreferrer">تلگرام</a>
            <a href="https://rubika.ir/upme2025" target="_blank" class="social-link" rel="noopener noreferrer">روبیکا</a>
        </div>
        <p>© 2025 <a href="/">UpMe</a>. | <a href="/blog/">بلاگ</a> | <a href="/#cta">دانلود رایگان</a></p>
    </footer>
    <button id="back-to-top" class="back-to-top" title="بازگشت به بالا" aria-label="بازگشت به بالا"><span aria-hidden="true">↑</span></button>
    <script src="/assets/js/site.js" defer></script>
"""

HEAD_EXTRA = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700;900&display=swap">
    <link rel="stylesheet" href="/assets/css/site.css">
    <link rel="icon" type="image/png" href="/logo.png">
"""


def page(title, description, canonical_path, body, schema_extra="", og_title=None):
    og_title = og_title or title
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE}{canonical_path}">
{HEAD_EXTRA}
    <meta property="og:type" content="article">
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{SITE}{canonical_path}">
    <meta property="og:image" content="{SITE}/logo.png">
{schema_extra}
</head>
<body>
{NAV}
<main id="main-content" class="page-main">
{body}
</main>
{FOOTER}
</body>
</html>
"""


def related_block(items):
    links = "\n".join(f'<li><a href="{url}">{title}</a></li>' for url, title in items)
    return f'<section class="related-posts"><h2>مطالب مرتبط</h2><ul class="related-list">{links}</ul></section>'


ARTICLES = []

# Article definitions with full Persian content
articles_data = [
    {
        "file": "career-path.html",
        "title": "چطور بهترین مسیر شغلی را پیدا کنیم؟ راهنمای کامل خودشناسی و مسیریابی | UpMe",
        "desc": "راهنمای گام‌به‌گام پیدا کردن مسیر شغلی مناسب با تست شخصیت، کشف استعداد و اپلیکیشن UpMe.",
        "h1": "چطور بهترین مسیر شغلی را پیدا کنیم؟",
        "tag": "مسیریابی شغلی",
        "date": "۱ آگوست ۲۰۲۶",
        "time": "۸ دقیقه",
        "body": """
<p>سردرگمی شغلی یکی از شایع‌ترین چالش‌های نسل جوان ایران است. شاید شما هم بارها از خودتان پرسیده باشید: «چه شغلی برای من مناسب است؟» یا «آیا مسیر فعلی‌ام درست است؟» پاسخ این سوالات بدون خودشناسی عمیق، معمولاً تصادفی و پرریسک می‌شود.</p>
<h2>چرا بسیاری مسیر شغلی اشتباه انتخاب می‌کنند؟</h2>
<p>انتخاب شغل صرفاً بر اساس بازار کار، فشار خانواده یا رویاهای دیگران، بدون شناخت تیپ شخصیتی و ارزش‌های درونی، منجر به فرسودگی شغلی، اضطراب و حس پوچی می‌شود. تحقیقات نشان می‌دهد بخش قابل توجهی از شاغلان ایرانی احساس می‌کنند شغلشان با شخصیتشان هم‌خوانی ندارد.</p>
<h2>گام اول: خودشناسی واقعی</h2>
<p>قبل از جستجوی شغل، باید بفهمید شما کی هستید. تست‌های معتبر مثل <strong>MBTI</strong> (تیپ شخصیتی) و <strong>هالند</strong> (استعدادیابی شغلی) نقشه اولیه‌ای از علایق، مهارت‌ها و محیط کار ایده‌آل شما ارائه می‌دهند. اپلیکیشن <a href="/">UpMe</a> این تست‌ها را با زبان فارسی و تفسیر هوشمند ترکیب کرده است.</p>
<h2>گام دوم: تحلیل استعداد و ارزش‌ها</h2>
<p>استعداد فقط «چیزهایی که خوب انجام می‌دهید» نیست؛ شامل انرژی‌بخش بودن و حس معنا هم می‌شود. ارزش‌های شغلی مثل ثبات، خلاقیت، درآمد، تأثیر اجتماعی یا استقلال، فیلتر مهمی برای انتخاب مسیر هستند. UpMe با هوش مصنوعی این لایه‌ها را کنار هم تحلیل می‌کند.</p>
<h2>گام سوم: اکتشاف مسیرهای شغلی</h2>
<p>پس از خودشناسی، فهرست مشاغل مرتبط را بررسی کنید: مسیر ورود، مهارت‌های مورد نیاز، بازار کار ایران و پتانسیل رشد. مسیریاب شغلی UpMe بر اساس داده‌های واقعی، مسیرهای شغلی و تحصیلی پیشنهاد می‌دهد.</p>
<h2>گام چهارم: آزمایش و بازخورد</h2>
<p>مسیر شغلی یک‌باره انتخاب نمی‌شود؛ با تجربه، کارآموزی، پروژه‌های کوچک و گفتگو با افراد حرفه‌ای تکامل می‌یابد. هر قدم کوچک، تصویر واضح‌تری می‌سازد.</p>
<h2>چرا UpMe؟</h2>
<p>UpMe (upme، اپمی) بهترین اپلیکیشن خودشناسی و مسیریابی شغلی ایران است: تست رایگان، مشاوره هوشمند، برنامه رشد فردی و دانلود آسان از <a href="https://upmee.site/app/upme.apk">upmee.site</a> و بازار.</p>
""",
        "related": [
            ("/blog/mbti-vs-holland.html", "MBTI یا هالند؟"),
            ("/blog/career-change.html", "تغییر شغل در ۳۰ سالگی"),
            ("/blog/student-guide.html", "راهنمای دانشجویان"),
        ],
    },
    {
        "file": "mbti-vs-holland.html",
        "title": "MBTI یا هالند؟ مقایسه تست‌های شخصیت برای انتخاب شغل | UpMe",
        "desc": "مقایسه تست MBTI و تست هالند برای خودشناسی، انتخاب رشته و مسیریابی شغلی. کدام تست برای شما مناسب است؟",
        "h1": "MBTI یا هالند؟ کدام تست خودشناسی بهتر است؟",
        "tag": "تست شخصیت",
        "date": "۱ آگوست ۲۰۲۶",
        "time": "۷ دقیقه",
        "body": """
<p>در جستجوی خودشناسی و انتخاب مسیر شغلی، دو تست پرکاربرد هستند: <strong>MBTI</strong> (تیپ شخصیتی) و <strong>تست هالند</strong> (استعدادیابی شغلی). هر کدام زاویه متفاوتی به شما نشان می‌دهند.</p>
<h2>تست MBTI چیست؟</h2>
<p>MBTI شخصیت را در چهار محور تحلیل می‌کند و یک کد چهارحرفی (مثل INTJ یا ENFP) تولید می‌کند. این تست به درک نحوه تفکر، ارتباط، تصمیم‌گیری و سازگاری با محیط کمک می‌کند. برای شناخت «چگونه فکر می‌کنید و با دیگران کار می‌کنید» بسیار مفید است.</p>
<h2>تست هالند چیست؟</h2>
<p>مدل هالند شش تیپ شغلی (واقع‌گرا، جستجوگر، هنری، اجتماعی، متهور، قراردادی) را بررسی می‌کند و مشاغل مرتبط با علایق شما را پیشنهاد می‌دهد. برای «چه نوع فعالیت‌هایی انرژی‌بخش شماست» ایده‌آل است.</p>
<h2>مقایسه سریع</h2>
<ul>
<li><strong>MBTI:</strong> تمرکز بر شخصیت و روان‌شناسی درونی</li>
<li><strong>هالند:</strong> تمرکز بر علایق شغلی و محیط کار</li>
<li><strong>بهترین رویکرد:</strong> استفاده از هر دو و تحلیل ترکیبی</li>
</ul>
<h2>UpMe هر دو را یکجا ارائه می‌دهد</h2>
<p>اپلیکیشن UpMe تست MBTI و هالند را با تفسیر فارسی و تحلیل هوش مصنوعی ترکیب می‌کند. نتیجه: تصویر کامل‌تری از شخصیت و مسیر شغلی مناسب. <a href="https://upmee.site/app/upme.apk">دانلود رایگان UpMe</a> و تست را امروز شروع کنید.</p>
""",
        "related": [
            ("/blog/career-path.html", "پیدا کردن مسیر شغلی"),
            ("/blog/konkur-tips.html", "انتخاب رشته کنکور"),
            ("/blog/introducing-upme.html", "معرفی UpMe"),
        ],
    },
    {
        "file": "career-change.html",
        "title": "۵ قدم طلایی تغییر شغل در ۳۰ سالگی | UpMe",
        "desc": "راهنمای عملی تغییر مسیر شغلی در ۳۰ سالگی با تست شخصیت، خودشناسی و اپلیکیشن UpMe.",
        "h1": "۵ قدم طلایی برای تغییر شغل در ۳۰ سالگی",
        "tag": "تغییر شغل",
        "date": "۱ آگوست ۲۰۲۶",
        "time": "۹ دقیقه",
        "body": """
<p>تغییر شغل در ۳۰ سالگی نه غیرعادی است و نه دیر. بسیاری از موفق‌ترین افراد حداقل یک بار مسیر شغلی‌شان را تغییر داده‌اند. کلید موفقیت: تصمیم آگاهانه بر پایه خودشناسی، نه فرار از مشکل موقت.</p>
<h2>قدم ۱: ارزیابی صادق وضعیت فعلی</h2>
<p>چرا می‌خواهید شغل عوض کنید؟ آیا مشکل از محیط کار، مدیر، حقوق یا عدم تطابق با شخصیت است؟ یادداشت روزانه و تست شخصیت UpMe کمک می‌کند ریشه را بشناسید.</p>
<h2>قدم ۲: بازنگری استعداد و ارزش‌ها</h2>
<p>شاید در ۲۰ سالگی چیزهایی را نمی‌دانستید که الان می‌دانید. تست مجدد MBTI و هالند در UpMe دید تازه‌ای می‌دهد.</p>
<h2>قدم ۳: تحقیق درباره مسیرهای جدید</h2>
<p>مصاحبه با افراد شغل مورد نظر، دوره‌های کوتاه، پروژه‌های جانبی و بررسی بازار کار ایران. مسیریاب شغلی UpMe فهرست مشاغل مناسب را بر اساس تحلیل شخصیت ارائه می‌دهد.</p>
<h2>قدم ۴: ساخت مهارت و شبکه</h2>
<p>رزومه، لینکدین، مهارت‌های نرم و سخت. حتی ۳ ماه تمرکم می‌تواند شما را قابل‌استخدام کند.</p>
<h2>قدم ۵: اقدام تدریجی</h2>
<p>تغییر یک‌شبه همیشه لازم نیست. گاهی تغییر نقش در همان شرکت، فریلنس یا کارآموزی آغاز مسیر جدید است.</p>
<div class="article-cta">
<p>آماده تغییر مسیر هستید؟</p>
<a href="https://upmee.site/app/upme.apk" class="btn-primary" onclick="trackDownload()" rel="noopener">دانلود رایگان UpMe</a>
</div>
""",
        "related": [
            ("/blog/career-path.html", "مسیر شغلی"),
            ("/blog/student-guide.html", "راهنمای دانشجویان"),
            ("/blog/mbti-vs-holland.html", "MBTI vs هالند"),
        ],
    },
    {
        "file": "introducing-upme.html",
        "title": "معرفی کامل اپلیکیشن UpMe | خودشناسی و مسیریاب شغلی",
        "desc": "معرفی UpMe: اپلیکیشن خودشناسی، تست MBTI و هالند، مسیریابی شغلی و تحصیلی با هوش مصنوعی.",
        "h1": "معرفی کامل اپلیکیشن UpMe",
        "tag": "معرفی UpMe",
        "date": "۱ آگوست ۲۰۲۶",
        "time": "۶ دقیقه",
        "body": """
<p><strong>UpMe</strong> (upme، apme، اپمی) اپلیکیشن ایرانی خودشناسی و مسیریاب هوشمند شغلی و تحصیلی است که با تست‌های علمی و هوش مصنوعی، به شما کمک می‌کند مسیر زندگی‌تان را بشناسید و با اعتمادبه‌نفس انتخاب کنید.</p>
<h2>امکانات اصلی</h2>
<ul>
<li>تست خودشناسی MBTI و هالند با تفسیر فارسی</li>
<li>مسیریابی شغلی و تحصیلی هوشمند</li>
<li>دستیار هوش مصنوعی برای مشاوره</li>
<li>برنامه رشد فردی روزانه</li>
<li>ردیابی پیشرفت و انگیزه</li>
</ul>
<h2>برای چه کسانی؟</h2>
<p>دانش‌آموزان کنکور، دانشجویان سرگردان، شاغلان در جستجوی تغییر مسیر و هر کسی که به رشد فردی علاقه دارد.</p>
<h2>دانلود</h2>
<p>رایگان از <a href="https://upmee.site/app/upme.apk">وب‌سایت</a>، <a href="http://cafebazaar.ir/app/?id=com.example.upme&ref=share">بازار</a>، گوگل پلی و اپ استور. شبکه‌های اجتماعی: <a href="https://t.me/UpMeee">تلگرام</a>، <a href="https://rubika.ir/upme2025">روبیکا</a>.</p>
""",
        "related": [
            ("/blog/career-path.html", "مسیر شغلی"),
            ("/blog/mbti-vs-holland.html", "تست شخصیت"),
            ("/blog/konkur-tips.html", "کنکور"),
        ],
    },
    {
        "file": "student-guide.html",
        "title": "راهنمای خودشناسی برای دانشجویان سرگردان | UpMe",
        "desc": "دانشجوی سرگردان چه کار کند؟ راهنمای انتخاب رشته، تغییر مسیر تحصیلی و تست شخصیت با UpMe.",
        "h1": "راهنمای خودشناسی برای دانشجویان سرگردان",
        "tag": "دانشجویان",
        "date": "۱ آگوست ۲۰۲۶",
        "time": "۷ دقیقه",
        "body": """
<p>سرگردانی تحصیلی در دانشگاه تجربه شایعی است. «رشته‌ام را اشتباه انتخاب کردم»، «نمی‌دانم بعد از فارغ‌التحصیلی چه کار کنم» — اگر این حرف‌ها برایتان آشناست، خودشناسی اولین قدم درست است.</p>
<h2>تفاوت سرگردانی موقت و عمیق</h2>
<p>گاهی فقط نیاز به استراحت یا تغییر سبک مطالعه دارید. اگر اما مدت‌ها احساس بی‌معنایی دارید، احتمالاً مسیر تحصیلی با شخصیت و استعدادتان هم‌خوان نیست.</p>
<h2>ابزارهای عملی</h2>
<p>تست MBTI و هالند، گفتگو با مشاور تحصیلی، شرکت در انجمن‌های دانشگاهی و استفاده از UpMe برای تحلیل مسیرهای شغلی مرتبط با رشته یا علایق جایگزین.</p>
<h2>تغییر رشته یا ادامه مسیر؟</h2>
<p>قبل از تصمیم سنگین، داده جمع کنید: بازار کار، علاقه واقعی، مهارت‌های قابل انتقال و هزینه زمانی. UpMe سناریوهای مختلف را بر اساس شخصیت شما مقایسه می‌کند.</p>
""",
        "related": [
            ("/blog/konkur-tips.html", "انتخاب رشته کنکور"),
            ("/blog/career-path.html", "مسیر شغلی"),
            ("/blog/career-change.html", "تغییر شغل"),
        ],
    },
    {
        "file": "konkur-tips.html",
        "title": "انتخاب رشته کنکور با تست شخصیت | راهنمای UpMe",
        "desc": "چطور با تست MBTI و هالند بهترین رشته کنکور را انتخاب کنیم؟ راهنمای انتخاب رشته تحصیلی.",
        "h1": "انتخاب رشته کنکور با خودشناسی علمی",
        "tag": "کنکور",
        "date": "۱ آگوست ۲۰۲۶",
        "time": "۸ دقیقه",
        "body": """
<p>انتخاب رشته کنکور یکی از مهم‌ترین تصمیم‌های تحصیلی است. فشار رقابت، توصیه‌های اطرافیان و ترس از اشتباه، انتخاب را سخت می‌کند. راهکار: ترکیب علاقه، استعداد و داده‌های بازار کار — نه فقط رتبه.</p>
<h2>اشتباهات رایج</h2>
<ul>
<li>انتخاب رشته فقط به خاطر رتبه بالا</li>
<li>تقلید از دوستان یا خانواده بدون خودشناسی</li>
<li>نادیده گرفتن تیپ شخصیتی و محیط کار آینده</li>
</ul>
<h2>تست شخصیت قبل از انتخاب رشته</h2>
<p>MBTI نشان می‌دهد چگونه یاد می‌گیرید و در چه محیطی رشد می‌کنید. هالند رشته‌ها و مشاغل مرتبط با علایق شما را فهرست می‌کند. UpMe هر دو را به فارسی و با پیشنهاد رشته‌های دانشگاهی ارائه می‌دهد.</p>
<h2>چک‌لیست انتخاب رشته</h2>
<p>علاقه واقعی، استعداد، بازار کار، موقعیت جغرافیایی، هزینه و امکان ادامه تحصیل. اپلیکیشن UpMe این فاکتورها را در یک داشبورد یکجا می‌بینید.</p>
""",
        "related": [
            ("/blog/mbti-vs-holland.html", "MBTI vs هالند"),
            ("/blog/student-guide.html", "دانشجویان"),
            ("/blog/introducing-upme.html", "معرفی UpMe"),
        ],
    },
]

blog_dir = Path("/workspace/blog")
blog_dir.mkdir(exist_ok=True)

for a in articles_data:
    schema = f"""
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{a['h1']}",
        "description": "{a['desc']}",
        "author": {{ "@type": "Organization", "name": "UpMe" }},
        "publisher": {{
            "@type": "Organization",
            "name": "UpMe",
            "logo": {{ "@type": "ImageObject", "url": "{SITE}/logo.png" }}
        }},
        "datePublished": "2026-08-01",
        "mainEntityOfPage": "{SITE}/blog/{a['file']}"
    }}
    </script>"""
    article_html = f"""
<nav class="breadcrumb" aria-label="مسیر"><a href="/">خانه</a> / <a href="/blog/">بلاگ</a> / {a['h1'][:40]}…</nav>
<article class="article-header">
    <span class="blog-tag">{a['tag']}</span>
    <h1>{a['h1']}</h1>
    <div class="article-meta"><span>{a['date']}</span><span>زمان مطالعه: {a['time']}</span></div>
</article>
<div class="article-body">
{a['body']}
</div>
{related_block(a['related'])}
"""
    path = f"/blog/{a['file']}"
    html = page(a["title"], a["desc"], path, article_html, schema)
    (blog_dir / a["file"]).write_text(html, encoding="utf-8")

# Blog index
cards = []
for a in articles_data:
    cards.append(f"""
<article class="blog-card fade-in visible">
    <div class="blog-card-content">
        <span class="blog-tag">{a['tag']}</span>
        <h3><a href="/blog/{a['file']}" style="color:inherit;text-decoration:none">{a['h1']}</a></h3>
        <p>{a['desc'][:120]}…</p>
        <a href="/blog/{a['file']}" class="read-more">ادامه مطلب →</a>
    </div>
</article>""")

index_body = f"""
<div class="section-label">مقالات آموزشی</div>
<h1 style="font-size:clamp(2rem,5vw,2.8rem);font-weight:800;margin-bottom:0.5rem">بلاگ UpMe</h1>
<p style="color:var(--text-secondary);margin-bottom:2rem">خودشناسی، مسیر شغلی، تست شخصیت و رشد فردی</p>
<div class="blog-grid blog-list-page">{''.join(cards)}</div>
"""
index_html = page(
    "بلاگ UpMe | مقالات خودشناسی و مسیریابی شغلی",
    "مقالات رایگان درباره خودشناسی، تست MBTI و هالند، انتخاب رشته، تغییر شغل و اپلیکیشن UpMe.",
    "/blog/",
    index_body,
    "",
    "بلاگ UpMe",
)
(blog_dir / "index.html").write_text(index_html, encoding="utf-8")

print("Generated", len(articles_data) + 1, "blog pages")
