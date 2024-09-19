class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pref = strs[0]
        
        for strings in strs[1:]:
            while not strings.startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return""
                
        return pref