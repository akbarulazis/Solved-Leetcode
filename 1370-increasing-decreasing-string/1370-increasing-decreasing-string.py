class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        s_count = Counter(s)
        result = []
        
        unique = sorted(s_count.keys())
        
        while s_count:
            for char in unique:
                if char in s_count:
                    result.append(char)
                    s_count[char] -= 1
                if s_count[char] == 0:
                    del s_count[char]
            
            for char in reversed(unique):
                if char in s_count:
                    result.append(char)
                    s_count[char] -= 1
                if s_count[char] == 0:
                    del s_count[char]
            
        return "".join(result)