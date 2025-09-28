#!/usr/bin/env python3

import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from nlp_module import handle_answer
from question_utility import ask_question

# Load token
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start quiz command
async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['current_question'] = 0
    context.user_data['score'] = 0
    await ask_question(update, context)

# Main function
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start_quiz))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))

    application.run_polling()

if __name__ == "__main__":
    main()
