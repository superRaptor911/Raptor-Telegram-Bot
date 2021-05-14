from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from datetime import datetime
import State
import logging
import botHelpMenu
import GameMenu


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# function to handle the /start command
def start(update, context):
    update.message.reply_text('start command received')


# function to handle the /help command
def help(update, context):
    reply_keyboard = [['Boy', 'Girl', 'Other']]
    update.message.reply_text('help command received', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),)


# function to handle errors occured in the dispatcher 
def error(update, context):
    update.message.reply_text('an error occured')


# function to handle normal text 
def text(update : Update, context):
    text_received : str = update.message.text
    username = update.message.from_user.username

    if State.lastState(username) == False:
        if text_received == "bot help":
            State.pushState(username, botHelpMenu.helpMessageMenu)
            update.message.text = ""
        elif text_received == "bot games":
            State.pushState(username, GameMenu.mainMenu)
            update.message.text = ""
        else:
            return

    # state = State.getState(username, 0)
    state = State.lastState(username)
    if state != False:
        state(update, context)
    else:
        print("State not found")


        # update.message.reply_text(f'{reply_text}')


def main():
    TOKEN = "1806495603:AAHOGGg9uwThVQLv6YRCeauKXIubIg2w-7M"
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))
    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()
    # run the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
