#!/usr/bin/python3
import telegram
import os
import subprocess
bot = telegram.Bot(token='1490870889:AAHiuHg4XsvM3DfCIAeR737uaPElRzk8O1s')
chat_id = 1283339789 
#chat_id = 714967564 #J_ale
output = str(subprocess.check_output("./status.sh", shell=True))
output = output[2:-3]
msg = ""
if output == "inactive":
    msg = "La base se cayo"
else:
    msg = "la base esta activa"
bot.send_message(chat_id=chat_id, text=msg)


