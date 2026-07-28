> 🇺🇸 **English:** [README.md](README.md)
---

# ربات تلگرام قیمت طلا

یک ربات تلگرام سبک که به‌صورت دوره‌ای آخرین قیمت طلا را از یک وب‌سایت دریافت کرده و آن را در یک چت تلگرام ارسال می‌کند.

> **توجه**
>
> پیاده‌سازی اصلی فایل `services/gold.py` به درخواست کارفرما و برای حفظ حقوق مالکیت فکری (Copyright) از این مخزن حذف شده است. برای اطلاعات بیشتر، Docstring این فایل را مطالعه کنید.

---

## ✨ امکانات

- دریافت خودکار قیمت طلا
- ارسال دوره‌ای قیمت در تلگرام
- کیبورد اینلاین
- ساختار ماژولار و قابل توسعه
- استفاده از متغیرهای محیطی (`.env`)
- نگهداری و توسعه آسان

---

### 🎨 رنگ دکمه اینلاین

رنگ دکمه اینلاین بر اساس آخرین تغییر قیمت به‌صورت خودکار تغییر می‌کند:

- 🟦 **آبی:** قیمت نسبت به بررسی قبلی تغییری نکرده است.
- 🟥 **قرمز:** قیمت کاهش یافته است.
- 🟩 **سبز:** قیمت افزایش یافته است.

این وضعیت در هر بار بررسی قیمت (بر اساس مقدار `CHECK_INTERVAL`) محاسبه و به‌روزرسانی می‌شود.

---

## 🎬 Demo

![Demo](assets/demo.gif)

---

## 📁 ساختار پروژه

```text
.
├── assets/
│   └── demo.gif
├── keyboards/
│   └── gold_keyboard.py
├── services/
│   └── gold.py
├── tasks/
│   └── sender.py
├── loader.py
├── config.py
├── main.py
├── requirements.txt
├── .env.example
├── README.md
└── README_FA.md
```

---

## 🚀 نصب

ابتدا پروژه را Clone کنید.

```bash
git clone https://github.com/Behnam18/gold-price-telegram-bot.git
cd gold-price-telegram-bot
```

(اختیاری ولی پیشنهاد شده) یک محیط مجازی بسازید.

```bash
python -m venv .venv
```

فعال‌سازی محیط مجازی

### ویندوز

```bash
.venv\Scripts\activate
```

### لینوکس / مک

```bash
source .venv/bin/activate
```

نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

---

## ⚙️ تنظیمات

بر اساس فایل `.env.example` یک فایل `.env` بسازید.

نمونه:

```env
BOT_TOKEN = YOUR_BOT_TOKEN

CHANNEL_ID = YOUR_CHAT_ID

CHECK_INTERVAL = CHECK_INTERVAL_ON_SECONDS

URL = SOURCE_OF_RECEIVING_THE_PRICE_ADDRESS

GOLD_KEYBOARD_TEXT = INLINE_GOLD_KEYBOARD_TEXT

GOLD_KEYBOARD_URL = INLINE_GOLD_KEYBOARD_URL
```

---

## ⚠️ فایل حذف‌شده

فایل `services/gold.py` در این مخزن قرار ندارد.

برای اجرای پروژه باید تابع زیر را پیاده‌سازی کنید:

```python
async def get_gold_price() -> int: ...
```

شرایط:

- نام تابع باید **دقیقاً** `get_gold_price` باشد.
- مقدار بازگشتی باید از نوع `int` باشد.
- سایر بخش‌های پروژه بر اساس همین ساختار طراحی شده‌اند.

برای پیاده‌سازی می‌توانید از هر ابزار یا کتابخانه‌ای استفاده کنید؛ مانند:

- aiohttp
- requests
- BeautifulSoup
- Playwright
- Selenium

---

## ▶️ اجرا

```bash
python main.py
```

---

## 📦 وابستگی‌ها

- Python 3.11+
- aiogram
- aiohttp
- python-dotenv

---

## 📄 مجوز

این پروژه صرفاً برای اهداف آموزشی و نمونه‌کار منتشر شده است.

پیاده‌سازی اصلی مربوط به دریافت اطلاعات از وب‌سایت، به احترام حقوق مالکیت فکری و کپی‌رایت کارفرما از این مخزن حذف شده است.
