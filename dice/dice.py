import random
from dice.exceptions import InvalidArgumentError

class dice:
    def __init__(self, sides: int=6):
        if sides < 4 and sides != 2:
            raise InvalidArgumentError("Invalid argument in dice: Sides must be 4 or more.")
        self.sides = sides

    def roll(self, count: int = 1):
        if count < 1:
            raise InvalidArgumentError("Invalid argument in dice.roll: count must be an integer of 1 or more")
        total = [0]
        for i in range(count):
            temp = random.randint(1, self.sides)
            total[0] += temp
            total.append(temp)

        return total
