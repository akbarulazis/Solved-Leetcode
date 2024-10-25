import collections
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        ban = set(banned)
        c = Counter(word for word in words if word not in ban)
        mc = c.most_common()[0][0]
        return mc
        
        