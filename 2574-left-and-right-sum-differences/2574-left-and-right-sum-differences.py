class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right = nums.copy()
        right.reverse()
        leftsums =[0]
        rightsums =[0]
        for i in range(1,len(nums)):
            leftsums.append(sum(nums[0:i]))
        for i in range(1,len(right)):
            rightsums.append(sum(right[0:i]))
        rightsums.reverse()
        res = []
        for i in range(len(nums)):
            x = abs(leftsums[i]-rightsums[i])
            res.append(x)
        return res