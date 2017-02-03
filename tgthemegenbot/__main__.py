from telegram.ext import Updater, CommandHandler
from argparse import ArgumentParser


def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name +
                                                update.message.from_user.last_name))

def generate(bot, update):
    pass

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--token', required=True)
    args = parser.parse_args()

    updater = Updater(args.token)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('generate', generate, pass_args=True))
    updater.start_polling()
    updater.idle()
