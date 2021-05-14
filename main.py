from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from datetime import datetime
import State
import logging
import botHelpMenu
import botConfig
from games import GameMenu
from raptorTrading import coins


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# function to handle the /start command
def start(update, context):
    update.message.reply_text('start command received')


# function to handle the /help command
def help(update, context):
    # reply_keyboard = [['Boy', 'Girl', 'Other']]
    # update.message.reply_text('help command received', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),)
    update.message.reply_text('use \"bot help\"')


# function to handle errors occured in the dispatcher 
def error(update, context):
    update.message.reply_text('an error occured')


# function to handle normal text 
def text(update, context):
    username = update.message.from_user.username

    if State.lastState(username) == False:
        if botHelpMenu.evalInput(update):
            pass
        elif GameMenu.evalInput(update):
            pass
        elif coins.evalInput(update):
            pass
        else:
            return

    # state = State.getState(username, 0)
    state = State.lastState(username)
    if state != False:
        state(update, context)
    else:
        print("State not found")


def main():
    updater = Updater(botConfig.botTokkenId, use_context=True)
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
