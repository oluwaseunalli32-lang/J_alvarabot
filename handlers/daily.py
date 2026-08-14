from telegram import Update
from telegram.ext import ContextTypes
from words import get_random_word

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    word_entry = get_random_word()
    message = (
        f"📖 *{word_entry['word'].capitalize()}*\n"
        f"*Definition:* {word_entry['definition']}\n"
        f"*Example:* {word_entry['example']}\n"
        f"*Synonyms:* {', '.join(word_entry['synonyms'])}"
    )
    await update.message.reply_text(message, parse_mode="Markdown")
