import logging
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from words import find_word

logger = logging.getLogger(__name__)

WAITING_FOR_WORD = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Please enter the word you'd like to define."
    )
    return WAITING_FOR_WORD

async def get_definition(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    word = update.message.text.strip()
    entry = find_word(word)
    if entry:
        definition = entry.get("definition", "No definition available.")
        synonyms = ", ".join(entry.get("synonyms", []))
        await update.message.reply_text(
            f"*{entry['word'].capitalize()}*\n\n*Definition:* {definition}\n*Synonyms:* {synonyms}",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(f"Sorry, I don't have information about '{word}'. Please try another word.")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END
