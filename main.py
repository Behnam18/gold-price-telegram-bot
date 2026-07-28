"""Application entry point. Initialises the Telegram bot, registers handlers, starts background tasks, and begins polling Telegram for incoming updates. Run this file to start the bot."""

import asyncio
from loader import bot, dp
from tasks import sender_loop


async def main():
    asyncio.create_task(sender_loop())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
