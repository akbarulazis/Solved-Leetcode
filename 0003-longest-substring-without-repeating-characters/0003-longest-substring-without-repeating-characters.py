class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        max_length = 0
        start = 0
        for x in range(len(s)):
            while s[x] in char:
                char.remove(s[start])
                start += 1
            char.add(s[x])
                
            max_length = max(max_length, x-start+1)
        
        return max_length
        