from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        sub_string = []
        max_substring = 0

        for i in range(len(s)):
            if s[i] not in sub_string:
                sub_string.append(s[i])
            elif s[i] in sub_string and Counter(sub_string)[s[i]] == 1:
                sub_string.append(s[i])
            else:
                
                max_substring = max(len(sub_string), max_substring)
                sub_string = sub_string[sub_string.index(s[i])+1:]
                sub_string.append(s[i])

        
        max_substring = max(len(sub_string), max_substring)

        return max_substring 