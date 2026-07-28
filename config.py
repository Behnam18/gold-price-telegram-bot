"""Application configuration. Loads all required environment variables from the `.env` file and exposes them as typed Python constants for the rest of the project. This module serves as the single source of truth for project configuration."""

from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN: str | None = getenv("BOT_TOKEN")

CHANNEL_ID: str | None = str(getenv("CHANNEL_ID"))

CHECK_INTERVAL: int = int(getenv("CHECK_INTERVAL", "60"))

GOLD_KEYBOARD_TEXT: str = str(getenv("GOLD_KEYBOARD_TEXT", "GOLD_KEYBOARD_TEXT"))

GOLD_KEYBOARD_URL: str | None = str(getenv("GOLD_KEYBOARD_URL", "https://example.com"))

URL: str | None = getenv("URL")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in .env file.")

if CHECK_INTERVAL <= 1:
    raise ValueError("CHECK_INTERVAL must be more then 1 second.")
