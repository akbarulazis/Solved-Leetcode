class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0

        for x in nums:
            for y in nums:
                if abs(x-y) <= min(x,y):
                    max_xor = max(max_xor, x^y)
        
        return max_xor