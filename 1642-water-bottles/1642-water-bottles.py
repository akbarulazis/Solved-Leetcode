class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        drinkBottles = numBottles

        while emptyBottles >= numExchange:
            ExchangeBottles = emptyBottles // numExchange
            emptyBottles = ExchangeBottles + emptyBottles % numExchange

            drinkBottles += ExchangeBottles
        
        return drinkBottles