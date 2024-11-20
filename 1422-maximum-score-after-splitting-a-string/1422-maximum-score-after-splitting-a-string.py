class Solution:
    def maxScore(self, s: str) -> int:
        one_score = s.count('1')
        
        zero_score = 0
        max_score = 0
        
        for x in range(len(s) - 1):
            if s[x] == '0':
                zero_score += 1
            else:
                one_score -= 1
            
            score = zero_score + one_score
            
            max_score = max(max_score, score)

        return max_score