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
        State.pushState(username, "about")
        changeMenu(State.lastState(username), update, context)
    elif textReceived == "4":
        State.popState(username, 2)
    else:
        update.message.reply_text('Invalid Option')
        update.message.reply_text(text)



def aboutBotMenu(update, context):
    text = '''I am a bot created by Raptor

---------ABOUT MENU------------
0. To Know More
1. Back to Help Menu
2. Quit Help
    '''
    textReceived : str = update.message.text
    username = update.message.from_user.username

    if textReceived == "":
        update.message.reply_text(text)
    elif textReceived == "0":
        update.message.reply_text('I was created using python3 and im currently running in Raptor\'s laptop')
        State.popState(username)
        changeMenu(State.lastState(username), update, context)
    elif textReceived == "1":
        State.popState(username)
        changeMenu(State.lastState(username), update, context)
    elif textReceived == "2":
        State.popState(username, 2)
    else:
        update.message.reply_text('Invalid Option')
        update.message.reply_text(text)



#----------------------------------------------
Menu_config = {
        "help" : helpMessageMenu,
        "about" : aboutBotMenu,
    }


def changeMenu(menuName, update, context):
    update.message.text = ""
    Menu_config[menuName](update, context)

def controller(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    state = State.lastState(username)
    Menu_config[state](update, context)
