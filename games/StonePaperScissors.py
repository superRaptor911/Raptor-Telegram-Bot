import State
import random

GAME_DATA = {
    "scores": {},
}

MOVES = ["", "STONE", "PAPER", "SCISSOR"]

def genMainMenuText() -> str:
    return '''Welcome!!!
Stone Paper Scissors v1.0

1. New game
2. Settings
3. Exit
'''

def genGameOverText(username) -> str:
    userScore = GAME_DATA["scores"][username]["userScore"]
    cpuScore = GAME_DATA["scores"][username]["botScore"]
    text = ''
    if userScore > cpuScore:
        text = f"Congratulation {username}. \nYou defeated SuperRaptorBot.\nGGWP"
    else:
        text = "Better Luck next time looser!\nNT"
    return f'''GAME OVER
{text}
'''


def mainMenu(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    chatType = update.message.chat.type
    if chatType != "private":
        update.message.reply_text('This game Can only be played in private chat 🌚')
        State.popState(username)
        State.changeMenuNow(update, context)
        return

    if textReceived == "":
        update.message.reply_text(genMainMenuText())
    elif textReceived == "1":
        startGame(update)
        State.pushState(username, gameLogic)
        State.changeMenuNow(update, context)
    elif textReceived == "2":
        update.message.reply_text('To DO')
    elif textReceived == "3":
        State.popState(username)
        State.changeMenuNow(update, context)
    else:
        update.message.reply_text('Wrong Input')
        update.message.reply_text(genMainMenuText())


def startGame(update):
    username = update.message.from_user.username
    GAME_DATA["scores"][username] =  {
            "userScore" : 0,
            "botScore"  : 0,
            "userMove"  : 1,
            "botMove"   : 1,
            }


def showScore(username):
    if username in GAME_DATA["scores"]:
        userScore = GAME_DATA["scores"][username]["userScore"]
        cpuScore = GAME_DATA["scores"][username]["botScore"]
        return f'{username}: {userScore}\nBot: {cpuScore}\n\n'
    return 'Error: Loading Scores'


def evalMoves(update, context):
    username = update.message.from_user.username
    userMove = GAME_DATA["scores"][username]["userMove"]
    botMove = GAME_DATA["scores"][username]["botMove"]

    if userMove == botMove:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tie!")
        return
    userWins = userMove > botMove
    if abs(userMove - botMove) > 1:
        userWins = not userWins
    if userWins:
        GAME_DATA["scores"][username]["userScore"] += 1
        context.bot.send_message(chat_id=update.effective_chat.id, text="You win!")
    else:
        GAME_DATA["scores"][username]["botScore"] += 1
        context.bot.send_message(chat_id=update.effective_chat.id, text="You lost!")


def getUserInput(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    if not (textReceived in ["1", "2", "3"]):
        update.message.reply_text("Invalid option moron!")
        State.popState(username)
        State.changeMenuNow(update, context)
        return

    GAME_DATA["scores"][username]["userMove"] = int(textReceived)
    GAME_DATA["scores"][username]["botMove"] = random.randint(1,3)

    userMove = MOVES[GAME_DATA["scores"][username]["userMove"]]
    botMove = MOVES[GAME_DATA["scores"][username]["botMove"]]
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"You : {userMove}\nBot: {botMove}")
    evalMoves(update, context)
    State.popState(username)
    State.changeMenuNow(update, context)


def checkGameOver(username) -> bool:
    userScore = GAME_DATA["scores"][username]["userScore"]
    cpuScore = GAME_DATA["scores"][username]["botScore"]
    return (userScore >= 5 or cpuScore >= 5)


def gameLogic(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    score = showScore(username)
    heading = '''Select ur Move

1. Stone
2. Paper
3. Scissor

'''
    if not checkGameOver(username):
        context.bot.send_message(chat_id=update.effective_chat.id, text=score)
        update.message.reply_text(heading)
        State.pushState(username, getUserInput)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=genGameOverText(username))
        State.popState(username)
        State.changeMenuNow(update, context)

