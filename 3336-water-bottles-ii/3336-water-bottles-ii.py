class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drinkBottles = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            emptyBottles = emptyBottles - numExchange + 1
            numExchange += 1
            drinkBottles += 1
        
        return drinkBottles