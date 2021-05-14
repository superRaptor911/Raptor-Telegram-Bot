import State
from . import StonePaperScissors
from . import guessTheWord

def genMainMenuText() -> str:
    return '''Games

1. Stone Paper Scissors
2. Guess The Word
0. Exit
'''

def mainMenu(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username



    if textReceived == "":
        update.message.reply_text(genMainMenuText())
    elif textReceived == "1":
        State.pushState(username, StonePaperScissors.mainMenu)
        State.changeMenuNow(update, context)
    elif textReceived == "2":
        State.pushState(username, guessTheWord.mainMenu)
        State.changeMenuNow(update, context)
    elif textReceived == "0":
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

