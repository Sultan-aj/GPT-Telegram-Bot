# GPT-Telegram Bot
GPT-Telegram Bot is a chatbot for Telegram that uses GPT-based language models to provide intelligent responses to user input.

## Setup
To use GPT-Telegram Bot, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages by running 
```pip install -r requirements.txt```
3. Set up a Telegram bot and obtain an API key. See [Telegram's Bot API documentation](https://core.telegram.org/bots#how-do-i-create-a-bot) for instructions.
4. Create a `.env` file in the root directory of the project and add the telegram bot API to the following line: 
```
TELEGRAM_BOT_API_KEY=<your-telegram-bot-api-key> 
```
5. Open `bot.py` and add your Telegram API key:
```
TELEGRAM_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")
```

6. Open `wrapper.py` and add your OpenAI API key:
```
os.environ['openai_api_key'] = "ADD OPENAI API KEY" 
```

7. Run python `wrapper.py` to create the vectorIndex.json file.
8. Run python `bot.py` to start the Telegram bot.



## Acknowledgements
- OpenAI - for providing the GPT language model.
- python-telegram-bot - for providing the Telegram bot API wrapper.
