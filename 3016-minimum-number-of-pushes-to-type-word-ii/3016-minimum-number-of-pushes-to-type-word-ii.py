class Solution:
    def minimumPushes(self, word: str) -> int:
        res= 0
        i = 0
        sorted_values = sorted(Counter(word).values(), reverse=True)
        print(sorted_values)
        for n in sorted_values:
            res += n * (i//8 + 1)
            i += 1
        return res
            