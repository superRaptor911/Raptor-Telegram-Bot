import time
# Script to handle state and state changes

GLOBAL_STATE = {}

# state = {username, states[], time}

# Get State
def getState(username : str, level : int = 0):
    if username in GLOBAL_STATE:
        states = GLOBAL_STATE[username]["states"]
        if len(states) > level:
            return states[level]
    return False


def lastState(username : str):
    if username in GLOBAL_STATE:
        states = GLOBAL_STATE[username]["states"]
        if len(states) > 0:
            return states[-1]
    return False


def createUserState(username: str):
    GLOBAL_STATE[username] = {
            "username" : username,
            "states"   : [],
            "time"     : int(time.time())
        }


def pushState(username: str, state):
    if not (username in GLOBAL_STATE):
        createUserState(username)
    GLOBAL_STATE[username]["states"].append(state)


def popState(username: str, count = 1):
    if username in GLOBAL_STATE:
        GLOBAL_STATE[username]["states"] = GLOBAL_STATE[username]["states"][0:-count]


def popAllStates(username: str):
    if username in GLOBAL_STATE:
        GLOBAL_STATE[username]["states"].clear()


def changeMenuNow(update, context):
    username = update.message.from_user.username
    update.message.text = ""
    menu = lastState(username)
    if menu:
        menu(update, context)
    else:
        print("Faled To change Menu for " + username)
