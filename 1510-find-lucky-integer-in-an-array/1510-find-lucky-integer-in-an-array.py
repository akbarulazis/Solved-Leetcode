from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_number = -1

        res = Counter(arr)

        for num, val in res.items():
            if num == val:
                lucky_number = max(lucky_number, num)
        
        return lucky_number