

def readDiceData(arr):
    out = ""
    for i in range(len(arr[1:]) + 1):
        if i == len(arr[1:]):
            delm = ""
        else:
            delm = ", "
        out += str(arr[i]) + delm
    return out