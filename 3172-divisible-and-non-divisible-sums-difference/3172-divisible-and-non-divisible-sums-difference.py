class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = [x for x in range(n+1) if x%m != 0]
        num2 = [x for x in range(n+1) if x%m == 0]

        return sum(num1) - sum(num2)