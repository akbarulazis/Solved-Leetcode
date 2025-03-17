from collections import Counter 
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_counter = Counter(nums)
        n = len(nums)/2
        res = 0
        for key, value in nums_counter.items():
            if value%2 == 0:
                res += value/2
            else:
                return False
        
        return res == n
        