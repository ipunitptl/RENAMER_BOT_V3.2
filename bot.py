import asyncio
from pyrogram import Client, compose,idle
import os

from flask import Flask
from threading import Thread

web = Flask(__name__)

@web.route("/")
def home():
    return "Bot Running"

def run_web():
    web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

Thread(target=run_web).start()

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
