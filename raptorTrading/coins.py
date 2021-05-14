import State
import requests
import json
import utility


def genMainMenuText():
    return ''''''

def genCoinPricing(data):
    output = ''
    for coin in data:
        price = float(data[coin]["last"])
        coinName = data[coin]["base_unit"]
        output = output + f'[{coinName}]\nPrice: {utility.readableValue(price)}\n\n'
    return output

def mainMenu(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    chatType = update.message.chat.type

    if textReceived == "":
        update.message.reply_text(genMainMenuText())
    elif textReceived == "1":
        # State.pushState(username, StonePaperScissors.mainMenu)
        State.changeMenuNow(username, update, context)
    elif textReceived == "2":
        State.popState(username)
    else:
        update.message.reply_text('Wrong Input')
        update.message.reply_text(genMainMenuText())


def coinPrice(update, context):
    username = update.message.from_user.username
    update.message.reply_text('Please wait.. Fetching your request')
    serverResponse = requests.post("https://raptorinc.ga/server/coin.php", json = {"type" :"prices"})

    if serverResponse.status_code != 200:
        update.message.reply_text('Error: Request to server failed')
        return

    result = json.loads(serverResponse.text)
    if result["result"] == True:
        update.message.reply_text(genCoinPricing(result["coins"]))
    else:
        update.message.reply_text('Error: Did not get coin pricing')
    State.popState(username)


def evalInput(update) -> bool:
    textReceived : str = update.message.text
    username = update.message.from_user.username

    if textReceived in ["coins", "coin menu"]:
        State.pushState(username, mainMenu)
        update.message.text = ""
        return True
    elif textReceived in ["coin price", "coin pricing"]:
        State.pushState(username, coinPrice)
        update.message.text = ""
        return True
    return False
