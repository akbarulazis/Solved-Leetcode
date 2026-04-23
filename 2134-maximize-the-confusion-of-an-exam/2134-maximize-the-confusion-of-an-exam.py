class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def checkKey(findKey):
            count = 0 
            left = 0
            max_length = 0

            for right in range(len(answerKey)):
                if answerKey[right] != findKey:
                    count += 1
                
                while count > k:
                    if answerKey[left] != findKey:
                        count -= 1
                    left += 1
                
                max_length = max(max_length, right - left +1)
            
            return max_length
        
        max_t = checkKey('T')
        max_f = checkKey('F')

        return max(max_t, max_f)