import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from words import get_random_word, WORDS
from grammar_questions import get_random_grammar_question


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message with a button to open the main dashboard."""
    keyboard = [[InlineKeyboardButton("🚀 Open Main Utility", callback_data="main_utility")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! This bot provides useful tools directly inside Telegram.\n"
        "Press the button below to get started.",
        reply_markup=reply_markup,
    )


async def main_utility_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show the main dashboard with activity buttons."""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📖 Daily Word", callback_data="main_daily")],
        [InlineKeyboardButton("🧠 Vocabulary Quiz", callback_data="main_quiz")],
        [InlineKeyboardButton("✍️ Grammar Practice", callback_data="main_grammar")],
        [InlineKeyboardButton("❓ Help / Commands", callback_data="main_help")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🎯 *Main Utility Dashboard*\n\nChoose an activity to start learning English!",
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )


# ----- Dashboard: Daily Word -----
async def main_daily_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    word_entry = get_random_word()
    message = (
        f"📖 *{word_entry['word'].capitalize()}*\n"
        f"*Definition:* {word_entry['definition']}\n"
        f"*Example:* {word_entry['example']}\n"
        f"*Synonyms:* {', '.join(word_entry['synonyms'])}"
    )
    await query.edit_message_text(message, parse_mode="Markdown")


# ----- Dashboard: Vocabulary Quiz -----
async def main_quiz_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    word_entry = get_random_word()
    correct_answer = word_entry["definition"]
    other_defs = [w["definition"] for w in WORDS if w["word"] != word_entry["word"]]
    random.shuffle(other_defs)
    options = [correct_answer] + other_defs[:3]
    random.shuffle(options)

    # Store for the answer callback
    context.user_data["quiz_correct"] = correct_answer
    context.user_data["quiz_word"] = word_entry["word"]

    keyboard = []
    for opt in options:
        keyboard.append([InlineKeyboardButton(opt, callback_data=f"main_quiz_ans_{opt}")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        f"What is the definition of *{word_entry['word']}*?",
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )


async def main_quiz_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    selected = query.data.replace("main_quiz_ans_", "")
    correct = context.user_data.get("quiz_correct")
    word = context.user_data.get("quiz_word")

    if selected == correct:
        await query.edit_message_text(f"✅ Correct! '{word}' means '{correct}'.")
    else:
        await query.edit_message_text(
            f"❌ Incorrect. The correct definition of '{word}' is:\n'{correct}'"
        )

    context.user_data.pop("quiz_correct", None)
    context.user_data.pop("quiz_word", None)


# ----- Dashboard: Grammar Practice -----
async def main_grammar_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    question = get_random_grammar_question()
    q_text = question["question"]
    options = question["options"]
    correct_answer = options[question["correct"]]
    context.user_data["grammar_correct"] = correct_answer

    keyboard = []
    for opt in options:
        keyboard.append([InlineKeyboardButton(opt, callback_data=f"main_grammar_ans_{opt}")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        f"📚 *Grammar Practice*\n\n{q_text}",
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )


async def main_grammar_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    selected = query.data.replace("main_grammar_ans_", "")
    correct = context.user_data.get("grammar_correct")

    if selected == correct:
        await query.edit_message_text("✅ Correct! Well done.")
    else:
        await query.edit_message_text(f"❌ Incorrect. The correct answer is: '{correct}'")

    context.user_data.pop("grammar_correct", None)


# ----- Dashboard: Help -----
async def main_help_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    help_text = (
        "📋 *Available Commands*\n\n"
        "/start - Welcome & main dashboard\n"
        "/help - Show this list\n"
        "/daily - Get a random word\n"
        "/quiz - Vocabulary quiz\n"
        "/grammar - Grammar quiz\n"
        "/example - Get example sentences\n"
        "/define - Get definition\n"
        "/about - About this bot\n"
        "/privacy - Privacy policy"
    )
    await query.edit_message_text(help_text, parse_mode="Markdown")
