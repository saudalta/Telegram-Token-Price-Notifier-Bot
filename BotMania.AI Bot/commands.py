import time

import Responses as R


def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('If you need help! You should ask for it on Google!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(str(response))


def error(update, context):
    print(f"Update {update} caused error {context.error}")
