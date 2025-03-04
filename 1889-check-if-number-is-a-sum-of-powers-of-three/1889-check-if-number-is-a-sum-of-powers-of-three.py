class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        base3 = []

        while n:
            n,r = divmod(n,3)
            base3.append(str(r))
        
        nums = ''.join(base3)

        if '2' in nums:
            return False
        else:
            return True