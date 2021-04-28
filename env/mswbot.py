from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import config
import json
from pathlib import Path
import requests

# 1. Get dictionary
# 2. Assign each object to a variable
# 3. Call variable when user triggers keyword

# Retrieving from local json file
def retrieve():
    path = Path(__file__).parent / "resources.json"
    with path.open() as json_file:
        data = json.load(json_file)
    return data

# Retrieving from api
def retrieve_ics():
    response = requests.get("https://icschecker.herokuapp.com/api/index")
    print(response.content())
    print(response.text())
    print(response.json())
    return response.json()

def start (update, context):
    update.message.reply_text("Nice to meet you! I am just a prototype, but you can start by keying in /ics or /medisave or /medishield to see links to their claimable limits!")

def help (update, context):
    update.message.reply_text("Nice to meet you! I am just a prototype, but you can start by keying in /ics or /medisave or /medishield to see links to their claimable limits!")

def medisave(update, context):
    medisave = retrieve()['medisave']['content']
    update.message.reply_text(medisave)

def medishield(update, context):
    keyboard = ReplyKeyboardMarkup([['Read More']])
    medishield = retrieve()['medishield']['content']
    update.message.reply_text(medishield, reply_markup=keyboard)

def ics(update, context):
    ntuc = retrieve_ics()[0]['org_name']
    ntuc_details = retrieve_ics()[0]['details']
    ntuc_contact = retrieve_ics()[0]['contact']
    ntuc_lastupdate = retrieve_ics()[0]
    update.message.reply_text(ntuc + ntuc_details + ntuc_contact + ntuc_lastupdate)

def main():
    print("MSW Bot started")
    updater = Updater(config.token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("medisave",medisave))       
    dp.add_handler(CommandHandler("medishield",medishield))     
    dp.add_handler(CommandHandler("ics", ics)) 
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
