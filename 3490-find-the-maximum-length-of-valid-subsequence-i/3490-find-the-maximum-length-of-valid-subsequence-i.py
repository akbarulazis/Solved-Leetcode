class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_num = [x for x in nums if x%2==0]
        odd_num = [x for x in nums if x%2!=0]

        alternating = []

        for x in nums:
            if len(alternating)==0:
                alternating.append(x)
            elif x%2 == 0 and alternating[-1]%2 != 0:
                alternating.append(x)
            elif x%2 != 0 and alternating[-1]%2 == 0:
                alternating.append(x)
        
        return max(len(even_num),len(odd_num), len(alternating))
