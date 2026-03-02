class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_b = blocks[:k].count('B')
        min_ops = k - count_b

        for i in range(1,len(blocks)-k+1):
            if blocks[i-1] == 'B':
                count_b -= 1
            if blocks[i+k-1] == 'B':
                count_b += 1 
            ops = k - count_b
            min_ops = min(ops, min_ops)

        return min_ops