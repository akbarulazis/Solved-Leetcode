class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l = [0,0]
        for x in moves:
            if x == 'U':
                l[1] = l[1] + 1
            elif x == 'D':
                l[1] = l[1] - 1
            elif x == 'R':
                l[0] = l[0] + 1
            elif x == 'L':
                l[0] = l[0] - 1
        
        return l == [0,0]