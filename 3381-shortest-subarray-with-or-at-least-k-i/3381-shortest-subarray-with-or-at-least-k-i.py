class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float('inf')
        n = len(nums)

        for x in range(n):
            or_value = 0
            for y in range(x,n):
                or_value |= nums[y]
                if or_value >= k:
                    min_length = min(min_length, y-x + 1)
                    break
        
        return min_length if min_length != float('inf') else -1