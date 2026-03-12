from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        x_sum=[]
        n = len(nums)

        for i in range(n-k+1):
            sub_array = nums[i:i+k]
            sub_array.sort(reverse=True)
            c = Counter(sub_array).most_common()
            count = 0
            for y in c[:x]:
                count += y[0] * y[1]
            x_sum.append(count)
        
        return x_sum