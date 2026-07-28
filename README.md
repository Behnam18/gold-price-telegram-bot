> 🇮🇷 **فارسی:** [README_FA.md](README_FA.md)
---

# Gold Price Telegram Bot

A lightweight Telegram bot that periodically fetches the latest gold price from a website and posts updates to a Telegram chat.

> **Note**
>
> The original implementation of `services/gold.py` has been intentionally removed at the client's request to protect proprietary code. See the module's docstring for implementation requirements.

---

## Features

- Automatic gold price monitoring
- Periodic updates
- Inline keyboard
- Modular project structure
- Environment variable configuration
- Easy to extend and maintain

---



### 🎨 Inline Keyboard color

The inline keyboard button color is automatically updated based on the latest price change:

- 🟦 **Blue:** The price has not changed since the previous check.
- 🟥 **Red:** The price has decreased.
- 🟩 **Green:** The price has increased.

The button state is recalculated on every price check according to the configured `CHECK_INTERVAL`.

---

## 🎬 Demo

![Demo](assets/demo.gif)

---

## Project Structure

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

## Installation

Clone the repository.

```bash
git clone https://github.com/Behnam18/gold-price-telegram-bot.git
cd gold-price-telegram-bot
```

Create a virtual environment (optional but recommended).

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file based on `.env.example`.

Example:

```env
BOT_TOKEN = YOUR_BOT_TOKEN

CHANNEL_ID = YOUR_CHAT_ID

CHECK_INTERVAL = CHECK_INTERVAL_ON_SECONDS

URL = SOURCE_OF_RECEIVING_THE_PRICE_ADDRESS

GOLD_KEYBOARD_TEXT = INLINE_GOLD_KEYBOARD_TEXT

GOLD_KEYBOARD_URL = INLINE_GOLD_KEYBOARD_URL
```

---

## Missing Module

The `services/gold.py` file is **not included** in this repository.

To run the project, implement a function with the following signature:

```python
async def get_gold_price() -> int: ...
```

Requirements:

- Function name **must remain** `get_gold_price`
- Return type **must be** `int`
- The rest of the project depends on this interface

You may use any technology you prefer, including:

- aiohttp
- requests
- BeautifulSoup
- Playwright
- Selenium

---

## Running

```bash
python main.py
```

---

## Requirements

- Python 3.11+
- aiogram
- aiohttp
- python-dotenv

---

## License

This repository is provided for educational purposes.

The original website scraping implementation has been removed to respect the client's copyright and intellectual property.
