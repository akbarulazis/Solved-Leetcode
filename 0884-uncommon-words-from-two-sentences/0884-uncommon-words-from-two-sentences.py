class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        for x in range(len(list(s1))):
            k = list(s1)
            k.pop(x)
            if s1[x] not in k and s1[x] not in s2:
                res.append(s1[x])
        for y in range(len(s2)):
            k = list(s2)
            k.pop(y)
            if s2[y] not in s1 and s2[y] not in k:
                res.append(s2[y])
        return res
        