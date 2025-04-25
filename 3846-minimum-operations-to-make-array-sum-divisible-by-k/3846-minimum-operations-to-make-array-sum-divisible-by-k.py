class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        x = sum(nums)

        while x%k != 0:
            cnt += 1
            x -= 1
        
        return cnt