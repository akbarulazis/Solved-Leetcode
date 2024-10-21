class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrom(sub, left, right):
            while left < right:
                if sub[left] != sub[right]:
                    return False
                
                left = left + 1
                right = right - 1
            return True
        
        left , right = 0 , len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                return ispalindrom(s, left+1,right) or ispalindrom(s, left,right-1)
            left = left + 1
            right = right - 1 
            
        return True