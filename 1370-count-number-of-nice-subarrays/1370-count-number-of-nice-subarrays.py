class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        odd_position = [-1]
        n = len(nums)

        for i in range(n):
            if nums[i] % 2 == 1 :
                odd_position.append(i)
            if len(odd_position) > k:
                left_bound = odd_position[-k]
                prev_odd = odd_position[-k-1]

                res += left_bound - prev_odd
        
        return res