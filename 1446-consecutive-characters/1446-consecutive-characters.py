class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_res = [1]
        for c in range(1,len(s)):
            if s[c-1] == s[c]:
                count+=1
                max_res.append(count)
            else:
                count = 1
 
        return max(max_res)
        
            
                