#!/usr/bin/python3
import telegram
import os
import time
bot = telegram.Bot(token='1490870889:AAHiuHg4XsvM3DfCIAeR737uaPElRzk8O1s')

while True:
    updates = bot.get_updates()
    text = [u.message.text for u in updates] #check if anyone send status_db
    time.sleep(2)
    if text[-1] == "/check_db":
        os.system("./tele.py")
    else:
        continue
    

