class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for x in range(len(nums)-n):
            res.append(nums[x])
            res.append(nums[x+n])
        return res