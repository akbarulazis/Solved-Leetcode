class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n=len(nums)
        res = 0
        for i in range(n-1):
            for j in range(n):
                if i < j :
                    t = nums[i] + nums[j]
                    if t < target:
                        res = res + 1
        return res
                    