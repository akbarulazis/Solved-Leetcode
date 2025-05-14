class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            min_val = min(nums)
            index_min_val = nums.index(min_val)

            new_min_val = min_val * multiplier
            nums[index_min_val] = new_min_val

            k -= 1
        
        return nums