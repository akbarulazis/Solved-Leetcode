class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a = list(words[0])
        for i in range(1,len(words)):
            k = list(words[i])
            for x in range(len(a)):
                if a[x] not in k:
                    a[x] = '-'
                else:
                    k.remove(a[x])
    
        res = [x for x in a if x != '-']
        return res
            