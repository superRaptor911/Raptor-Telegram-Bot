# Word Guessing game
import State
import random
import utility

GAME_DATA = {
    "data": {},
}

Resources = {
        "movies": "games/gamedata/wordGuessing/movies.txt"
    }

def shuffleString(string : str) -> str:
    return ''.join(random.sample(string,len(string)))

def getCrypticWord(word : str) -> str:
    output = ""
    strings = word.lower().split(" ")
    for i in strings:
        output = output + shuffleString(i) + " "

    return output


def getTheme(username):
    theme = "movies"
    userdata = getUserData(username)
    if userdata:
        theme = userdata["theme"]
    return theme

def getUserData(username):
    if username in GAME_DATA["data"]:
        return GAME_DATA["data"][username]
    return False

def createUser(username):
    if not (username in GAME_DATA["data"]):
        GAME_DATA["data"][username] = {
                "theme": "movies",
                "word": "",
                "type": "gaps"
                }
        print("Created Account for " + username)


def genGameMenu(username):
    return f'''Guess the Word v1.0

1. Start game
2. Select Theme
3. Select Game Type
4. Exit

Current Theme: {getTheme(username)}
'''

def showCorrectGuessMessage(update, context):
    username = update.message.from_user.username
    word = GAME_DATA["data"][username]["word"]
    text = f"Great!!! You guessed correctly!!\n{word} is the word"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def showQuitGameMessage(update, context):
    username = update.message.from_user.username
    word = GAME_DATA["data"][username]["word"]
    text = f"Lol!!! You are so stupid 😂😂\n\"{word}\" is the correct word"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def startGame(update, context):
    username = update.message.from_user.username
    theme = GAME_DATA["data"][username]["theme"]
    word = random.choice(utility.getLinesFromFile(Resources[theme]))
    GAME_DATA["data"][username]["word"] = word
    crypticWord = getCrypticWord(word)

    message = 'GAME STARTED\n\nGet Ready!!!\n Type quit to quit the Game'
    update.message.reply_text(message)

    message2 = f'Guess The Word\n\n{crypticWord}'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message2)


def gameLogic(update, context):
    textReceived : str = update.message.text.lower()
    username = update.message.from_user.username

    if textReceived in ["quit", "exit"]:
        showQuitGameMessage(update, context)
        State.popState(username)
        State.changeMenuNow(update, context)
    elif textReceived == GAME_DATA["data"][username]["word"].lower():
        showCorrectGuessMessage(update, context)
        State.popState(username)
        State.changeMenuNow(update, context)


def mainMenu(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    createUser(username)
    if textReceived == "":
        update.message.reply_text(genGameMenu(username))
    elif textReceived == "1":
        startGame(update, context)
        State.pushState(username, gameLogic)
        # State.changeMenuNow(update, context)
    elif textReceived == "2":
        update.message.reply_text('To DO')
    elif textReceived == "3":
        update.message.reply_text('To DO')
    elif textReceived == "4":
        State.popState(username)
        State.changeMenuNow(update, context)
    else:
        update.message.reply_text('Wrong Input')
        update.message.reply_text(genGameMenu(username))
