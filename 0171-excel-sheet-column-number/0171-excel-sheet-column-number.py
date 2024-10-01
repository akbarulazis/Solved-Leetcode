class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = []
        title = ''.join(columnTitle[::-1])
        for i in range(len(title)):
            char = ord(title[i]) - ord('A')
            char += 1
            result.append(char*(26**i))
        
        return sum(result)