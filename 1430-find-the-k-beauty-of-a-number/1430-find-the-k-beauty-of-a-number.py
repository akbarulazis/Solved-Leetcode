class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        cnt = 0

        for i in range(len(num)-k+1):
            divisor = int(num[i:i+k])
            if divisor != 0 and int(num)%divisor == 0:
                cnt += 1
        
        return cnt