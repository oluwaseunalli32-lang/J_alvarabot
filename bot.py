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
    main_utility_callback,
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

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("privacy", privacy))
    application.add_handler(CommandHandler("function", function_placeholder))
    application.add_handler(CommandHandler("daily", daily))
    application.add_handler(CommandHandler("quiz", quiz))
    application.add_handler(CommandHandler("grammar", grammar))

    # Conversation handler for /example
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

    # Conversation handler for /define
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

    # Callback query handlers
    application.add_handler(CallbackQueryHandler(quiz_callback, pattern="^quiz_"))
    application.add_handler(CallbackQueryHandler(grammar_callback, pattern="^grammar_"))
    application.add_handler(CallbackQueryHandler(main_utility_callback, pattern="^main_utility$"))

    # 🛡️ Force a new event loop if none exists (Python 3.14 fix)
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    logger.info("Bot started, polling...")
    application.run_polling()


if __name__ == "__main__":
    main()
