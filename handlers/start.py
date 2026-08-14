from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message and a 'Main Utility' button."""
    keyboard = [
        [InlineKeyboardButton("Main Utility", callback_data="main_utility")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! This bot provides useful tools directly inside Telegram.",
        reply_markup=reply_markup
    )

async def main_utility_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the Main Utility button press."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("The main utility has not been configured yet.")
