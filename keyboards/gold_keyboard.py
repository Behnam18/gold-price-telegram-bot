"""Telegram keyboard builders. Contains helper functions responsible for creating inline keyboards used by the bot. Separating keyboard generation from business logic keeps handlers clean and easier to maintain."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GOLD_KEYBOARD_TEXT, GOLD_KEYBOARD_URL


def gold_keyboard(color) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=GOLD_KEYBOARD_TEXT, style=color, url=GOLD_KEYBOARD_URL
                )
            ]
        ]
    )
