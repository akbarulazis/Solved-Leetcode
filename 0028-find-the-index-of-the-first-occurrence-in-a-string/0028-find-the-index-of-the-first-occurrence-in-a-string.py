class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ind  = []
        for i in range(len(haystack)-len(needle)+1):
            # print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                ind.append(i)
        if not ind: 
            ind.append(-1)
        # print(ind)
        return min(ind)