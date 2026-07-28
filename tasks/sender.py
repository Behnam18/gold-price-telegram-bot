"""Background sender task. Runs continuously while the bot is active, periodically fetching the latest gold price and sending updates to the configured Telegram chat. This module is responsible only for scheduling and sending messages."""

import asyncio
from config import CHANNEL_ID, CHECK_INTERVAL
from loader import bot
from services import get_gold_price
from keyboards import gold_keyboard


async def sender_loop():
    last_data = None
    while True:
        try:
            data = await get_gold_price()
            if data is None:
                await asyncio.sleep(CHECK_INTERVAL)
                continue

            if last_data is not None:
                if data > last_data:
                    color = "success"
                elif data < last_data:
                    color = "danger"
                else:
                    color = "primary"
            else:
                color = None

            if data:
                await bot.send_message(
                    chat_id=CHANNEL_ID,
                    text=f"🧈Gold price: {data:,}$",
                    reply_markup=gold_keyboard(color),
                )

            last_data = data

        except Exception as e:
            print("loop error:", e)

        await asyncio.sleep(CHECK_INTERVAL)
