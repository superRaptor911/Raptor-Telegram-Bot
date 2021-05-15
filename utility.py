# UTILITY SCRIPT

def readableValue(value : float) -> str:
    finalValue = ""
    if value > 1000000:
        value /= 1000000
        finalValue = str(round(value, 2)) + "M"
    elif value > 1000:
        value /= 1000
        finalValue = str(round(value, 2)) + "K"
    elif value < 0.01 and value > 0:
        value *= 1000
        finalValue = str(round(value, 2)) + "m"
    else:
        finalValue = str(round(value, 2))

    return finalValue

def getLinesFromFile(path : str):
    file1 = open(path, 'r')
    arr = []

    while True:
        # Get next line from file
        line = file1.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        arr.append(line.strip())

    file1.close()
    return arr
