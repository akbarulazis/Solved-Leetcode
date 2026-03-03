class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        sub_array = [0]

        for i in range(len(nums)):
            cnt = 0
            if nums[i]%2 == 0 and nums[i] <= threshold:
                j = i
                cnt += 1
                while j < len(nums)-1:
                    if nums[j]%2 != nums[j+1]%2 and nums[j] <= threshold and nums[j+1] <= threshold:
                        j+= 1
                        cnt += 1
                    else:
                        break
                sub_array.append(cnt)
        
        return max(sub_array)


