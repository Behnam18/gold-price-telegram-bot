"""
NOTICE

This file has been intentionally removed at the client's request to protect their proprietary implementation and copyright.

Originally, this module fetched data from the client's website using `aiohttp` and extracted the required gold price from the HTML using `BeautifulSoup`.

The rest of the project depends on a function named `get_gold_price()`. To keep the project structure unchanged, please implement a function with the same name and make sure it returns the current gold price as an `int`.

You are free to use any suitable libraries or approach, including:

- aiohttp
- requests
- BeautifulSoup
- Playwright
- Selenium
- or any other preferred solution

Don't forget to install the required dependencies (e.g. with `pip install`) and import them into this file before implementing the function.

Thank you for your understanding.
"""

import asyncio


async def get_gold_price() -> int:
    return 123456789
