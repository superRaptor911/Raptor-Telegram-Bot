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


def genInvestorDetails(data):
    output = ''
    for i in data:
        user = data[i]
        username = user['name']
        investment = user['investment']
        value = user['value']
        profit = value - investment

        output = output + f'''[{username}]
investment  : {utility.readableValue(investment)}
cur value   : {utility.readableValue(value)}
profit      : {utility.readableValue(profit)}

'''
    return output


def getInvestorDetails(users, coins):
    data = {}
    for user in users:
        data[user["username"]] = {
          "name": user["username"],
          "investment": float(user["investment"]),
          "amount": float(user["amount"]),
          "value": float(user["amount"]),
          "profit": 0,
          "percent": 0
        };
        data[user["username"]]["investment"] = max(data[user["username"]]["investment"], 0)
        for c in user["coins"]:
            coin = coins[c["coin"]]
            if coin:
              data[user["username"]]["value"] += float(coin["last"]) * float(c["count"]);
    return data


def mainMenu(update, context):
    textReceived : str = update.message.text
    username = update.message.from_user.username

    chatType = update.message.chat.type

    if textReceived == "":
        update.message.reply_text(genMainMenuText())
    elif textReceived == "1":
        # State.pushState(username, StonePaperScissors.mainMenu)
        State.changeMenuNow(update, context)
    elif textReceived == "2":
        State.popState(username)
    else:
        update.message.reply_text('Wrong Input')
        update.message.reply_text(genMainMenuText())


def coinPrice(update, context):
    username = update.message.from_user.username
    update.message.reply_text('Please wait.. Let me get latest values')
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


def coinInvestors(update, context):
    username = update.message.from_user.username
    update.message.reply_text('Please wait.. Let me calculate')

    serverResponse = requests.post("https://raptorinc.ga/server/coin.php", json = {"type" :"prices"})
    if serverResponse.status_code != 200:
        update.message.reply_text('Error: I dint get current coin price\nMaybe server is down 😬')
        State.popState(username)
        return

    result = json.loads(serverResponse.text)
    coins = []
    if result["result"] == True:
        coins = result["coins"]
    else:
        update.message.reply_text('Error: Did not get coin pricing')
        State.popState(username)
        return

    serverResponse = requests.post("https://raptorinc.ga/server/transction.php", json = {"type" :"investmentNcoins"})
    if serverResponse.status_code != 200:
        update.message.reply_text('Error: I dint get Investment details\nMaybe server is down 😬')
        State.popState(username)
        return

    result = json.loads(serverResponse.text)
    users = []
    if result["result"] == True:
        users = result["data"]
    else:
        update.message.reply_text('Error: Did not get Investment details')
        State.popState(username)
        return

    update.message.reply_text(genInvestorDetails(getInvestorDetails(users, coins)))
    State.popState(username)


def evalInput(update) -> bool:
    textReceived : str = update.message.text
    username = update.message.from_user.username

    if len(textReceived) > 30:
        return False

    textReceived = textReceived.lower()
    if textReceived in ["coins", "coin menu"]:
        State.pushState(username, mainMenu)
        update.message.text = ""
        return True
    elif textReceived in ["coin price", "coin pricing"]:
        State.pushState(username, coinPrice)
        update.message.text = ""
        return True
    elif textReceived in ["coin investors"]:
        State.pushState(username, coinInvestors)
        update.message.text = ""
        return True
    return False
