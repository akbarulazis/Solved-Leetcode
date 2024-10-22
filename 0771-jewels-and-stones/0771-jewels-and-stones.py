class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        numb = 0
        for x in stones:
            if x in jewels:
                numb += 1
        return numb