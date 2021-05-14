import State
import StonePaperScissors

def genMainMenuText() -> str:
    return '''Games

1. Stone Paper Scissors
2. Exit
'''

def mainMenu(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    if textReceived == "":
        update.message.reply_text(genMainMenuText())
    elif textReceived == "1":
        State.pushState(username, "stonePaper")
        changeMenu(State.lastState(username), update, context)
    elif textReceived == "2":
        State.popState(username)
    else:
        update.message.reply_text('Wrong Input')
        update.message.reply_text(genMainMenuText())

#----------------------------------------------
Menu_config = {
        "gameMenu" : mainMenu,
        "stonePaper" : StonePaperScissors.controller,
    }


def changeMenu(menuName, update, context):
    update.message.text = ""
    Menu_config[menuName](update, context)


def controller(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    state = State.lastState(username)
    Menu_config[state](update, context)
