import logging
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)
from config import BOT_TOKEN
from handlers import (
    start,
    help_command,
    about,
    privacy,
    function_placeholder,
    daily,
    quiz,
    grammar,
    quiz_callback,
    grammar_callback,
    # Main Utility dashboard imports
    main_utility_callback,
    main_daily_callback,
    main_quiz_callback,
    main_quiz_answer_callback,
    main_grammar_callback,
    main_grammar_answer_callback,
    main_help_callback,
    # Example & Define
    example_start,
    get_example,
    example_cancel,
    EXAMPLE_WAITING,
    define_start,
    get_definition,
    define_cancel,
    DEFINE_WAITING,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    # ---- Command handlers ----
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("privacy", privacy))
    application.add_handler(CommandHandler("function", function_placeholder))
    application.add_handler(CommandHandler("daily", daily))
    application.add_handler(CommandHandler("quiz", quiz))
    application.add_handler(CommandHandler("grammar", grammar))

    # ---- Conversation handlers ----
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("example", example_start)],
            states={
                EXAMPLE_WAITING: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, get_example)
                ],
            },
            fallbacks=[CommandHandler("cancel", example_cancel)],
        )
    )
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("define", define_start)],
            states={
                DEFINE_WAITING: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, get_definition)
                ],
            },
            fallbacks=[CommandHandler("cancel", define_cancel)],
        )
    )

    # ---- Callback query handlers ----
    # Existing quiz/grammar from /quiz and /grammar commands
    application.add_handler(CallbackQueryHandler(quiz_callback, pattern="^quiz_"))
    application.add_handler(CallbackQueryHandler(grammar_callback, pattern="^grammar_"))

    # Main Utility dashboard
    application.add_handler(CallbackQueryHandler(main_utility_callback, pattern="^main_utility$"))
    application.add_handler(CallbackQueryHandler(main_daily_callback, pattern="^main_daily$"))
    application.add_handler(CallbackQueryHandler(main_quiz_callback, pattern="^main_quiz$"))
    application.add_handler(CallbackQueryHandler(main_quiz_answer_callback, pattern="^main_quiz_ans_"))
    application.add_handler(CallbackQueryHandler(main_grammar_callback, pattern="^main_grammar$"))
    application.add_handler(CallbackQueryHandler(main_grammar_answer_callback, pattern="^main_grammar_ans_"))
    application.add_handler(CallbackQueryHandler(main_help_callback, pattern="^main_help$"))

    # ---- Event-loop fix for Python 3.14 (safe to keep) ----
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    logger.info("Bot started, polling...")
    application.run_polling()


if __name__ == "__main__":
    main()
