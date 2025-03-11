class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        substring = {'a':0,'b':0,'c':0}
        left = 0
        res = 0
        for right in range(len(s)):
            substring[s[right]] += 1
            while substring['a'] > 0 and substring['b'] > 0 and substring['c'] > 0:
                res += len(s) - right
                substring[s[left]] -= 1
                left += 1
        
        return res