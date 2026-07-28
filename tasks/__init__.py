"""
Background tasks executed independently of Telegram updates.
"""

from .sender import sender_loop

all = ["sender_loop"]
