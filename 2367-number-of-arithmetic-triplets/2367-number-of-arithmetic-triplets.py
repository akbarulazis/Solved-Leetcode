class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i < j < k:
                        if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                            res.append([i,j,k])
        return len(res)
                        