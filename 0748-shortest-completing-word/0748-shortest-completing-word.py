import collections
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license = [x.lower() for x in licensePlate if x.isalpha()]
        li = Counter(license)
        short = None
        for word in words:
            l_word  = Counter(word)
            
            if all(l_word[char] >= li[char] for char in li):
                if short == None or len(word) < len(short):
                    short = word
        return short