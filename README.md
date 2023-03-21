#GPT-Telegram Bot
GPT-Telegram Bot is a chatbot for Telegram that uses GPT-based language models to provide intelligent responses to user input.

###Setup
To use GPT-Telegram Bot, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages by running pip install -r requirements.txt.
3. Open bot.py and add your Telegram API key:
'
TELEGRAM_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")
'

4. Open wrapper.py and add your OpenAI API key:
'
os.environ['openai_api_key'] = "ADD OPENAI API KEY"
'

5. Run python wrapper.py to create the vectorIndex.json file.
6. Run python bot.py to start the Telegram bot.