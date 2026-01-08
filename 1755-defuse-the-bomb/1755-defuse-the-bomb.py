class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)

        new_out = []
        new_code = code*2

        n = len(code)

        if k > 0:
            for x in range(n):
                total = sum(new_code[x+1:x+k+1])
                new_out.append(total)
            return new_out
        

        if k < 0 :
            for x in range(n):
                total = sum(new_code[x+n+k:x+n])
                new_out.append(total)
            return new_out