class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        check = [i for i in range(1, (len(grid)*len(grid))+1)]
        new_grid = [y for x in grid for y in x]
        res = []

        for i in grid:
            for x in i:
                if x in check:
                    check.remove(x)
                else:
                    res.append(x)
        
        for x in range(1,len(new_grid)+1):
            if x not in new_grid:
                res.append(x)
        
        return res