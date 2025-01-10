class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        num = 0
        for k in patterns:
            if k in word:
                num += 1
        return num