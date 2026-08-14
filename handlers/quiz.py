import random
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from words import get_random_word, WORDS

logger = logging.getLogger(__name__)

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a vocabulary quiz."""
    # Pick a random word
    word_entry = get_random_word()
    correct_answer = word_entry["definition"]
    # Get distractors: definitions of other words
    other_defs = [w["definition"] for w in WORDS if w["word"] != word_entry["word"]]
    random.shuffle(other_defs)
    options = [correct_answer] + other_defs[:3]
    random.shuffle(options)

    # Store correct answer and word in context for callback
    context.user_data["quiz_correct"] = correct_answer
    context.user_data["quiz_word"] = word_entry["word"]

    keyboard = []
    for opt in options:
        keyboard.append([InlineKeyboardButton(opt, callback_data=f"quiz_{opt}")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"What is the definition of *{word_entry['word']}*?",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    selected = query.data.replace("quiz_", "")
    correct = context.user_data.get("quiz_correct")
    word = context.user_data.get("quiz_word")

    if selected == correct:
        await query.edit_message_text(f"✅ Correct! '{word}' means '{correct}'.")
    else:
        await query.edit_message_text(
            f"❌ Incorrect. The correct definition of '{word}' is:\n'{correct}'"
        )
    # Clear stored data
    context.user_data.pop("quiz_correct", None)
    context.user_data.pop("quiz_word", None)
