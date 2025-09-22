from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        res = []
        for x,y in num_count.items():
            if y == max(num_count.values()):
                res.append(y)
        
        return sum(res)
