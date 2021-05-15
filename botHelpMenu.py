import State

# Help commands

def genCommandList() -> str:
    return '''List of Commands
* help  - Opens help menu
* commands  - Lists commands
* about - Opens About menu
* games - Opens game menu
* word guess - Starts word guessing game
* stone paper - Starts stone paper scissor game
* coin price - Lists current coin price
* coin investors - Lists investor\'s details
'''

def helpMessageMenu(update, context):
    username = update.message.from_user.username
    text = f'''
    Hello {username}, I'm SuperRaptorBot

---------HELP MENU------------
1. Commands
2. About me
3. Source code
0. Quit help
    '''

    textReceived : str = update.message.text
    if textReceived == "":
        update.message.reply_text(text)
    elif textReceived == "1":
        update.message.reply_text(genCommandList())
    elif textReceived == "2":
        State.pushState(username, aboutBotMenu)
        State.changeMenuNow(update, context)
    elif textReceived == "3":
        update.message.reply_text('https://github.com/superRaptor911/Raptor-Telegram-Bot')
        update.message.reply_text(text)
    elif textReceived == "0":
        State.popState(username)
    else:
        update.message.reply_text('Invalid Option')
        update.message.reply_text(text)


def aboutBotMenu(update, context):
    text = '''I am a bot created by Raptor

---------ABOUT MENU------------
0. To Know More
1. Back to Help Menu
2. Quit
    '''
    textReceived : str = update.message.text
    username = update.message.from_user.username

    if textReceived == "":
        update.message.reply_text(text)
    elif textReceived == "0":
        update.message.reply_text('I was created using python3 and im currently running in Raptor\'s laptop')
        State.popState(username)
        State.changeMenuNow(update, context)
    elif textReceived == "1":
        State.popState(username)
        State.changeMenuNow(update, context)
    elif textReceived == "2":
        State.popAllStates(username)
    else:
        update.message.reply_text('Invalid Option')
        update.message.reply_text(text)


def evalInput(update) -> bool:
    textReceived : str = update.message.text
    username = update.message.from_user.username

    if len(textReceived) > 30:
        return False

    textReceived = textReceived.lower()
    if textReceived in ["help", "bot help", "bh", "bot"]:
        State.pushState(username, helpMessageMenu)
        # Eat input
        update.message.text = ""
        return True
    elif textReceived in ["about", "bot details"]:
        State.pushState(username, aboutBotMenu)
        # Eat input
        update.message.text = ""
        return True
    elif textReceived in ["commands", "command"]:
        update.message.reply_text(genCommandList())
        return False
    return False
