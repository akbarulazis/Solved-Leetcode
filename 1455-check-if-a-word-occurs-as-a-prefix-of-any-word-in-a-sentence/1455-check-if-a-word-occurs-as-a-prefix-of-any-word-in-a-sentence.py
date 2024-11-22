class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        k = sentence.split(' ')
        p = len(searchWord)
        for x in range(len(k)):
            if searchWord in k[x][:p]:
                return x+1
        
        return -1