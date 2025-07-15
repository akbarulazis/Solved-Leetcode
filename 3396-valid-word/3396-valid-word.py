class Solution:
    def isValid(self, word: str) -> bool:
        special_char = ['@','#','$']


        is_vowel = 0
        is_consonant = 0
        vowel = ['a','i','u','e','o','A','I','U','E','O']

        if any(w in special_char for w in word):
            return False

        if len(word) < 3:
            return False


        for w in word:
            if w in vowel:
                is_vowel += 1
            elif w not in vowel:
                is_consonant += 1
            if is_vowel > 0 and is_consonant > 0 and not w.isdigit():
                return True
        
        return False