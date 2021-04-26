from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import config
import json
from pathlib import Path

# 1. Get dictionary
# 2. Assign each object to a variable
# 3. Call variable when user triggers keyword

def retrieve():
    path = Path(__file__).parent / "resources.json"
    with path.open() as json_file:
        data = json.load(json_file)

    return data

def start (update, context):
    update.message.reply_text("Nice to meet you! I am just a prototype, but you can start by keying in /medisave or /medishield to see links to their claimable limits!")

def help (update, context):
    update.message.reply_text("Nice to meet you! I am just a prototype, but you can start by keying in /medisave or /medishield to see links to their claimable limits!")

def medisave(update, context):
    medisave = retrieve()['medisave']['content']
    update.message.reply_text(medisave)

def medishield(update, context):
    keyboard = ReplyKeyboardMarkup([['Read More']])
    medishield = retrieve()['medishield']['content']
    update.message.reply_text(medishield, reply_markup=keyboard)

def main():
    print("MSW Bot started")
    updater = Updater(config.token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("medisave",medisave))       
    dp.add_handler(CommandHandler("medishield",medishield))      
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
