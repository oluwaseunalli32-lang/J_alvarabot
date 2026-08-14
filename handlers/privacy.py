from telegram import Update
from telegram.ext import ContextTypes

async def privacy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    privacy_text = (
        "Privacy Policy:\n"
        "This bot only processes the information you provide directly (e.g., words you ask to define).\n"
        "We do not store your personal information, messages, or any identifiable data.\n"
        "No data is shared with third parties. Your privacy is respected."
    )
    await update.message.reply_text(privacy_text)
