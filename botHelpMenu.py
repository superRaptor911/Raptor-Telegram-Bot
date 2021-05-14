import State

# Help commands

def listCommands() -> str:
    return '''List of Commands
* bot help  - Opens help menu
* bot games - Opens game menu
'''

def helpMessageMenu(update, context):
    username = update.message.from_user.username
    text = f'''
    Hello {username}, I'm SuperRaptorBot

---------HELP MENU------------
0. commands
1. About me
2. Source code
3. random facts
4. quit help
    '''

    textReceived : str = update.message.text
    if textReceived == "":
        update.message.reply_text(text)
    elif textReceived == "0":
        update.message.reply_text(listCommands())
    elif textReceived == "1":
        State.pushState(username, aboutBotMenu)
        State.changeMenuNow(username, update, context)
    elif textReceived == "2":
        update.message.reply_text('To Do')
    elif textReceived == "3":
        update.message.reply_text('To Do')
    elif textReceived == "4":
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
        State.changeMenuNow(username, update, context)
    elif textReceived == "1":
        State.popState(username)
        State.changeMenuNow(username, update, context)
    elif textReceived == "2":
        State.popAllStates(username)
    else:
        update.message.reply_text('Invalid Option')
        update.message.reply_text(text)


def evalInput(update) -> bool:
    textReceived : str = update.message.text
    username = update.message.from_user.username

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
    return False
