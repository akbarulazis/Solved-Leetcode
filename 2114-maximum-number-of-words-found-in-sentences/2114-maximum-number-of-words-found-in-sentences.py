class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = []
        for i in sentences:
            num = len(i.split(' '))
            res.append(num)
        return max(res)