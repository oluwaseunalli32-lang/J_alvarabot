from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Available commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/about - About this bot\n"
        "/privacy - Privacy policy\n"
        "/function - Placeholder for main function\n"
        "/daily - Get a random English word with definition and example\n"
        "/quiz - Start a vocabulary quiz\n"
        "/grammar - Start a grammar practice quiz\n"
        "/example - Get example sentences for a word\n"
        "/define - Get definition of a word\n"
    )
    await update.message.reply_text(help_text)
