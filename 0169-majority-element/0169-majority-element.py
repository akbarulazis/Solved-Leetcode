from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = Counter(nums).most_common(1)
        return k[0][0]
        