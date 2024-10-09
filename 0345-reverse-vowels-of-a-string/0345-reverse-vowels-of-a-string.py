class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','i','u','e','o']
        s_vow = []
        s_index = []
        new_s = list(s)
        for x in range(len(s)):
            if s[x].lower() in vowel:
                s_vow.append(s[x])
                s_index.append(x)
        s_vow.reverse()
        for a in range(len(s_index)):
            new_s[s_index[a]] = s_vow[a]
        return ''.join(new_s)