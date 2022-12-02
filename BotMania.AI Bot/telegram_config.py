from telegram.ext import *
import constant as keys
from commands import *
import requests
def telegram_resp_config():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

def telegram_send_config(message):
    tel_url = f"https://api.telegram.org/bot{keys.API_KEY}/sendMessage?chat_id={'1219744516'}&text={message}"
    print(requests.get(tel_url).json())
