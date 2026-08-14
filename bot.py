import asyncio
import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler
from config import BOT_TOKEN
from handlers import (
    start, help_command, about, privacy, function_placeholder,
    daily, quiz, grammar, example, define
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    # Create Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("privacy", privacy))
    application.add_handler(CommandHandler("function", function_placeholder))
    application.add_handler(CommandHandler("daily", daily))
    application.add_handler(CommandHandler("quiz", quiz))
    application.add_handler(CommandHandler("grammar", grammar))

    # Conversation handlers for example and define
    application.add_handler(ConversationHandler(
        entry_points=[CommandHandler("example", example.start)],
        states={
            example.WAITING_FOR_WORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, example.get_example)],
        },
        fallbacks=[CommandHandler("cancel", example.cancel)]
    ))
    application.add_handler(ConversationHandler(
        entry_points=[CommandHandler("define", define.start)],
        states={
            define.WAITING_FOR_WORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, define.get_definition)],
        },
        fallbacks=[CommandHandler("cancel", define.cancel)]
    ))

    # Callback query handler for quiz and grammar buttons
    application.add_handler(CallbackQueryHandler(quiz.handle_callback, pattern="^quiz_"))
    application.add_handler(CallbackQueryHandler(grammar.handle_callback, pattern="^grammar_"))

    # Main Utility button callback (placeholder)
    application.add_handler(CallbackQueryHandler(start.main_utility_callback, pattern="^main_utility$"))

    # Run the bot
    logger.info("Bot started, polling...")
    application.run_polling()


if __name__ == "__main__":
    main()
