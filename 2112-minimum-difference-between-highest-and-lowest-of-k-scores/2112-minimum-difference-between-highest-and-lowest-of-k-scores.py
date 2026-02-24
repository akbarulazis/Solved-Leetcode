class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        min_num = max(nums)
        nums.sort()

        for i in range(len(nums)-k+1):
            min_num = min(nums[i+k-1]-nums[i], min_num)
        
        return min_num
        
