class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for y in range(len(nums)):
            for x in range(len(nums)):
                if ( (nums[x] + nums[y]) == target) and x!=y:
                    return [x,y]

        