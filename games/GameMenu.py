import State
from . import StonePaperScissors

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
        State.pushState(username, StonePaperScissors.mainMenu)
        State.changeMenuNow(username, update, context)
    elif textReceived == "2":
        State.popState(username)
    else:
        update.message.reply_text('Wrong Input')
        update.message.reply_text(genMainMenuText())


def evalInput(update) -> bool:
    textReceived : str = update.message.text
    username = update.message.from_user.username
    # Eat input
    # update.message.text = ""
    if textReceived in ["bot games", "bot game", "games"]:
        State.pushState(username, mainMenu)
        update.message.text = ""
        return True
    return False

