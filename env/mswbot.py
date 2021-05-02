from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import config
import json
from pathlib import Path
import requests
import asyncio
import aiohttp

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
    return response.json()

def start (update, context):
    update.message.reply_text("Nice to meet you! I am just a prototype, but you can start by keying in /ics or /medisave or /medishield to see links to their claimable limits!")

def help (update, context):
    update.message.reply_text("Nice to meet you! I am just a prototype, but you can start by keying in /ics or /medisave or /medishield to see links to their claimable limits!")

def medisave(update, context):
    medisave = retrieve()["medisave"]["content"]
    update.message.reply_text(medisave)

def medishield(update, context):
    # keyboard = ReplyKeyboardMarkup([['Read More']])
    medishield = retrieve()["medishield"]["content"]
    update.message.reply_text(medishield)
    # update.message.reply_text(medishield, reply_markup=keyboard)

def amkch(update, context):
    update.message.reply_photo(photo=open('/home/ben/Documents/mswtelegrambot/env/amkch.png', 'rb'))

def ics(update, context):
    results = retrieve_ics()
    ntuc_name = results[0]['org_name']
    ntuc_details = results[0]['details']
    ntuc_contact = results[0]['contact']
    ntuc_lastupdate = results[0]['last_updated']

    ag_name = results[1]['org_name']
    ag_details = results[1]['details']
    ag_contact = results[1]['contact']
    ag_lastupdate = results[1]['last_updated']

    thkcare_name = results[2]['org_name']
    thkcare_details = results[2]['details']
    thkcare_contact = results[2]['contact']
    thkcare_lastupdate = results[2]['last_updated']

    thknh_name = results[3]['org_name']
    thknh_details = results[3]['details']
    thknh_contact = results[3]['contact']
    thknh_lastupdate = results[3]['last_updated']

    update.message.reply_text([ntuc_name] + [ntuc_details] + [ntuc_contact] + [ntuc_lastupdate])
    update.message.reply_text([ag_name] + [ag_details] + [ag_contact] + [ag_lastupdate])
    update.message.reply_text([thkcare_name] + [thkcare_details] + [thkcare_contact] + [thkcare_lastupdate])
    update.message.reply_text([thknh_name] + [thknh_details] + [thknh_contact] + [thknh_lastupdate])

def main():
    print("MSW Bot started")
    updater = Updater(config.token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("medisave", medisave))
    dp.add_handler(CommandHandler("medishield", medishield))
    dp.add_handler(CommandHandler("ics", ics))
    dp.add_handler(CommandHandler("amkch", amkch))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
