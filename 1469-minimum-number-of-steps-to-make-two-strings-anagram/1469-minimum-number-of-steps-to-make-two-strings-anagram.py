from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)

        count = 0

        for char in set(s_counter.keys()).union(t_counter.keys()):
            count += max(0, s_counter[char] - t_counter[char])

        return count