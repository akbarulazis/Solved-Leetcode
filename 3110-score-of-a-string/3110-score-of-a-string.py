class Solution:
    def scoreOfString(self, s: str) -> int:
        k_list = []
        for i in range(len(s)-1):
            jml = abs( ord(s[i]) - ord(s[i+1]) )
            k_list.append(jml)
        return sum(k_list)