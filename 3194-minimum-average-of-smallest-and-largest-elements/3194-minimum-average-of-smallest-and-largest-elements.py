class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = int(len(nums)/2)
        aver = []
        nums.sort()
        for i in range(n):
            averages = (nums[0]+nums[-1])/2
            aver.append(averages)
            nums.pop(0)
            nums.pop(-1)
        return min(aver)