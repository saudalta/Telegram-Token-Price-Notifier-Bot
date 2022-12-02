from datetime import datetime
from binance import binance_config
ticker = 'BTC'
min_price = 0
max_price = 1


def sample_responses(input_text):
    global ticker, max_price, min_price
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi", "sup",):
        return "Hey! How's it going?"
    elif user_message in ("who are you", "who are you"):
        return "I am ABC bot!"
    elif user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    elif user_message in ('alert', 'start alert'):
        price = binance_config("BTC")
        return price

    # SAUD EDITS & ADDITIONS:
    elif 'ticker =' in user_message:
        ticker = user_message.split()[-1]
        return f'you have set ticker to {ticker}'

    elif 'max price =' or 'max price=' in user_message:
        max_price = int(user_message.split()[-1])
        return f'You have set the max price alert to {str(max_price)} USD '

    elif 'min price =' or 'min price=' in user_message:
        min_price = int(user_message.split()[-1])
        return f'You have set the max price alert to {str(min_price)} USD '

    elif user_message in ('this ', 'what is the current price'):
        print(ticker)
        price = binance_config(ticker)
        return f'The current price of is {price} '

    return "I don't understand, please make sure you are typing the commands in the format mentioned in the help menu "
