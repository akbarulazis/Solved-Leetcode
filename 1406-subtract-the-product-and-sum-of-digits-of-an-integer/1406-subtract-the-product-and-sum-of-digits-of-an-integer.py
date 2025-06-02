class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list_n = [int(x) for x in str(n)]

        sop = 1
        for x in list_n:
            sop = sop * x
        
        return sop - sum(list_n)