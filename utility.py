# UTILITY SCRIPT

def readableValue(value : float) -> str:
    finalValue = ""
    if value > 1000000:
        value /= 1000000
        finalValue = str(round(value, 2)) + "M"
    elif value > 1000:
        value /= 1000
        finalValue = str(round(value, 2)) + "K"
    else:
        finalValue = str(round(value, 2))

    return finalValue

