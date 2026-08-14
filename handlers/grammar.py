import random
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from grammar_questions import GRAMMAR_QUESTIONS, get_random_grammar_question

logger = logging.getLogger(__name__)

async def grammar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a grammar quiz."""
    question = get_random_grammar_question()
    q_text = question["question"]
    options = question["options"]
    correct_index = question["correct"]

    # Store correct answer text in context
    correct_answer = options[correct_index]
    context.user_data["grammar_correct"] = correct_answer

    keyboard = []
    for idx, opt in enumerate(options):
        keyboard.append([InlineKeyboardButton(opt, callback_data=f"grammar_{opt}")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Grammar Quiz:\n\n{q_text}",
        reply_markup=reply_markup
    )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    selected = query.data.replace("grammar_", "")
    correct = context.user_data.get("grammar_correct")

    if selected == correct:
        await query.edit_message_text("✅ Correct! Well done.")
    else:
        await query.edit_message_text(f"❌ Incorrect. The correct answer is: '{correct}'")
    # Clear stored data
    context.user_data.pop("grammar_correct", None)
