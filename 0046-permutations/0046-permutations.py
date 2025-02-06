class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]

        def backTracking(path,dataNum):
            if not dataNum:
                res.append(path[:])
                return
            
            for x in range(len(dataNum)):
               
                path.append(dataNum[x])
                backTracking(path, dataNum[:x]+dataNum[x+1:] )
                path.pop()
        
        backTracking([],nums)

        return res