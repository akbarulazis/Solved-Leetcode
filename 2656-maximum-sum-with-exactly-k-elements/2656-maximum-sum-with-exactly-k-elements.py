class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = []
        for _ in range(k):
            res.append(nums[-1])
            nums[-1] = nums[-1] + 1
        return sum(res)
        