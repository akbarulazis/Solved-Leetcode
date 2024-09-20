class Solution:
    def isValid(self, s: str) -> bool:
        a = {'}':'{',']':'[',')':'('}
        stack = []
        
        for char in s:
            
            if char in a:
                element = stack.pop() if stack else '#'
                
                if a[char] != element:
                    return False
            else:
                stack.append(char)
        
        return not stack