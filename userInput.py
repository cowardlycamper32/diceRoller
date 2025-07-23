from dice import dice
from utils import readDiceData


def takeInput():
    prompt = input("enter a dice ??? in the format xdy where x is the number of dice and y is the dice")
    return prompt
def parseInput(inp):
    dies = inp.split(" ")
    total = 0
    rolls = []
    for die in dies:
        temp = die.split("d")
        tempDice = dice(int(temp[1]))
        roll = tempDice.roll(int(temp[0]))
        total += roll[0]
        for i in roll[1:]:
            rolls.append(i)

    print(rolls)

    print(str(total) + ": " + readDiceData(rolls))
    return(total)