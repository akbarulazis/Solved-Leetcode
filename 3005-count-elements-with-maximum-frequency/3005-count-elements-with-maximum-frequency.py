from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        x = Counter(nums)
        max_c = list(x.values())
        cnt = 0
        for i in max_c :
            if i == max(max_c):
                cnt = cnt + i
        return cnt