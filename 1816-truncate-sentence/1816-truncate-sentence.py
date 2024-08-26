class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        word = s.split(' ')
        return ' '.join(word[:k])