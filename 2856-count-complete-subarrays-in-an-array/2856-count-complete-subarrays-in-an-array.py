class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        target_len = len(uniq_nums)
        subarrays = 0

        for i in range(len(nums)):
            current_set = set()
            for j in range(i, len(nums)):
                current_set.add(nums[j])
                if len(current_set) == target_len:
                    subarrays += 1
                elif len(current_set) > target_len:
                    break  

        return subarrays
    
