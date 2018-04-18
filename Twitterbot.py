from telegram.ext import Updater, CommandHandler
import commands.basic as cba 

with open("token.secret",'r') as tokenFile:
    token = tokenFile.read().splitlines()[0]

updater = Updater(token=token, workers=200)
dispatcher = updater.dispatcher

start_handler = CommandHandler(command = list(['iniciar','start']),callback = cba.start)

dispatcher.add_handler(handler = start_handler)

updater.start_polling(timeout=1)

updater.idle()


