class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for a in range(len(words)):
            if x in words[a]:
                res.append(a)
        return res