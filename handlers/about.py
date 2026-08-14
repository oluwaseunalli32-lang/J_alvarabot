from telegram import Update
from telegram.ext import ContextTypes

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    about_text = (
        "This bot is a utility framework designed to help you learn English.\n\n"
        "It provides vocabulary, grammar exercises, and word lookups—all within Telegram.\n"
        "The bot is built with a clear focus on utility and adheres to Telegram's advertising policies."
    )
    await update.message.reply_text(about_text)
