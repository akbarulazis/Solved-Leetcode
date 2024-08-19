class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            k = 0
            for j in range(n):
                if i != j:
                    if nums[i] > nums[j]:
                        k = k+1
            res.append(k)
        return res
                        
                
        