class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        cnt = 0
        for i in gain:
            cnt = cnt + i
            res.append(cnt)
        return max(res)
            
        