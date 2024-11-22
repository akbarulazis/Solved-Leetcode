class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y = 0,0
        v = set()
        v.add((x,y))
        
        for k in path:
            if k == 'N':
                y += 1
            elif k == 'S':
                y -= 1
            elif k == 'E':
                x += 1
            elif k == 'W':
                x -= 1
            
            if (x,y) in v:
                return True
            else :
                v.add((x,y))
        return False