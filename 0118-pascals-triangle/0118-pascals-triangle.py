class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for x in range(1,numRows+1):
            min_res = []
            c = 1
            for i in range(1,x+1):
                min_res.append(c)
                c = (c*(x-i))//i
        
            res.append(min_res)
        return res
        