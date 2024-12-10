class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left,right):
            while left >= 0  and right < len(s) and s[left] == s[right]:
                right += 1
                left -= 1
            
            return right - left - 1
          
        if len(s) < 2:
            return s
        start,end = 0,0
        for i in range(len(s)):
            
            odd = expand(i,i)
            
            even = expand(i,i+1)
            
            max_len = max(odd,even)
            
            if max_len > end - start:
                start = i - ( max_len - 1 )//2
                end = i + (max_len//2)
            
        return s[start:end+1]