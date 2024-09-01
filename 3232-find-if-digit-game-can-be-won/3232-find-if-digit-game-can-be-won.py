class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        dd = []
        sd = []
        for i in nums:
            if len(str(i)) == 1:
                sd.append(i)
            else:
                dd.append(i)
        if sum(sd) == sum(dd):
            return False
        else:
            return True