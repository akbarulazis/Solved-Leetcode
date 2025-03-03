class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        numLess = []
        numEqual = []
        numMoreThan = []

        for x in nums:
            if x < pivot:
                numLess.append(x)
            elif x == pivot:
                numEqual.append(x)
            elif x > pivot:
                numMoreThan.append(x)
        
        return numLess + numEqual + numMoreThan