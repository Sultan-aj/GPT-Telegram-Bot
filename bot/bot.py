# Import required packages
from dotenv import load_dotenv
import os
import logging
from telegram import Update
from telegram.ext import *

from llama_index import GPTSimpleVectorIndex

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Get API key from environment variable
TELEGRAM_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")
application = Application.builder().token(TELEGRAM_API_KEY).build()


# Define helper functions
async def start(update: Update, context):
    user = update.message.from_user # Get user information from the update object

    # Send a welcome message to the user
    await update.message.reply_text(
        f"Hi {user['username']}! I am ChatGeniuses bot. How can I assist you today?",
    )


# Get the response from the GPT index based on user input
# Send the response to the user
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = anserMe(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Load the GPT index from disk
# Query the GPT index with the user input
def anserMe(text):
    vInex = GPTSimpleVectorIndex.load_from_disk("vectorIndex.json")
    response = vInex.query(text, response_mode="compact")
    return f"{response} \n" # Return the response
    


# Commands
application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))


# Run bot
application.run_polling()