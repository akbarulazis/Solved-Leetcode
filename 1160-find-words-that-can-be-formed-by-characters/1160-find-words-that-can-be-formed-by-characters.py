from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch = Counter(chars)
        res = 0
        for x in words:
            k = Counter(x)
            temp = 0
            for y in x:
                if ch[y] >= k[y]:
                    temp += 1
                else:
                    break
            if temp == len(x):
                res = res + temp
        return res
        