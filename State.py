import time
# Script to handle state and state changes

GLOBAL_STATE = {}

# state = {username, states[], time}

# Get State
def getState(username : str, level : int = 0) -> str:
    if username in GLOBAL_STATE:
        states = GLOBAL_STATE[username]["states"]
        if len(states) > level:
            return states[level]
    return ""


def lastState(username : str) -> str:
    if username in GLOBAL_STATE:
        states = GLOBAL_STATE[username]["states"]
        if len(states) > 0:
            return states[-1]
    return ""


def createUserState(username: str):
    GLOBAL_STATE[username] = {
            "username" : username,
            "states"   : [],
            "time"     : int(time.time())
        }


def pushState(username: str, state: str):
    if not (username in GLOBAL_STATE):
        createUserState(username)
    GLOBAL_STATE[username]["states"].append(state)


def popState(username: str, count = 1):
    if username in GLOBAL_STATE:
        GLOBAL_STATE[username]["states"] = GLOBAL_STATE[username]["states"][0:-count]

