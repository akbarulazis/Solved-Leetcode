class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = nums.copy()
        count = 0
        n = len(nums)
        for x in range(n-2):
            if nums[x] == 0:
                count += 1

                for j in range(3):
                    if j + x < n:
                        nums[j+x] = 1- nums[j+x]
        
        return count if all( num == 1 for num in nums) else -1