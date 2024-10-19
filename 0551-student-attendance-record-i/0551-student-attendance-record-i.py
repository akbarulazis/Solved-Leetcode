from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        scount = Counter(s)
        if 'LLL' in s or scount['A'] > 1 :
            return False
        return True