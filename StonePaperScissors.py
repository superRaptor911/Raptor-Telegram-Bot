import State

GAME_DATA = {
    "scores": {},
    "highScore": {
        "username" : "",
        "score"    : 0
    }
}

def genMainMenuText() -> str:
    return '''Welcome!!!
Stone Paper Scissors v1.0

1. New game
2. High Score
3. Exit
'''


def mainMenu(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    if textReceived == "":
        update.message.reply_text(genMainMenuText())
    elif textReceived == "1":
        startGame(update)
        State.pushState(username, "playGame")
        changeMenu(State.lastState(username), update, context)
    elif textReceived == "2":
        update.message.reply_text('To DO')
    elif textReceived == "3":
        State.popState(username)
    else:
        update.message.reply_text('Wrong Input')
        update.message.reply_text(genMainMenuText())


def startGame(update):
    username = update.message.from_user.username
    GAME_DATA["scores"][username] =  [0, 0] # User, Bot score


def showScore(username):
    if username in GAME_DATA["scores"]:
        userScore = GAME_DATA["scores"][username][0]
        cpuScore = GAME_DATA["scores"][username][1]
        return f'{username}: {userScore}\nBot: {cpuScore}\n\n'
    return 'Error: Loading Scores'


def getUserInput(update, context):
    pass


def gameLogic(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    score = showScore(username)
    heading = '''Select ur Move

1. Stone
2. Paper
3. Scissor

'''
    output = score + heading
    update.message.reply_text(output)


#----------------------------------------------
Menu_config = {
        "stonePaper" : mainMenu,
        "playGame" : gameLogic,
    }


def changeMenu(menuName, update, context):
    update.message.text = ""
    Menu_config[menuName](update, context)


def controller(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    state = State.lastState(username)
    Menu_config[state](update, context)
