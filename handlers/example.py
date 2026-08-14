import logging
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from words import find_word

logger = logging.getLogger(__name__)

WAITING_FOR_WORD = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Please enter the word you'd like to see example sentences for."
    )
    return WAITING_FOR_WORD

async def get_example(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    word = update.message.text.strip()
    entry = find_word(word)
    if entry:
        examples = entry.get("example", "No example available.")
        await update.message.reply_text(
            f"*Examples for '{entry['word']}':*\n{examples}",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            f"Sorry, I don't have information about '{word}'. Please try another word."
        )
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END
