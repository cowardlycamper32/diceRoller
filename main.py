from dice import dice
from utils import readDiceData as diceRead
import userInput as ui

d2 = dice(2)
d4 = dice(4)
d6 = dice()
d8 = dice(8)
d10 = dice(10)
d12 = dice(12)
d20 = dice(20)
d100 = dice(100)


ui.parseInput(ui.takeInput())
