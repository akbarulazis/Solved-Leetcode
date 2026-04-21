import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        current_max = float('-inf')

        for x in range(len(nums)):
            value = nums[x][0]
            heapq.heappush(heap, (value, x , 0))
            current_max = max(current_max, value)
        
        best_start = float('-inf')
        best_end = float('inf')

        while True:
            current_min , num_list , idx = heapq.heappop(heap)

            current_width = current_max - current_min
            best_width = best_end - best_start

            if (current_width < best_width) or ( current_min < best_start and (current_width == best_width) ):
                best_end = current_max
                best_start = current_min
            
            if idx + 1 < len(nums[num_list]) :
                value = nums[num_list][idx+1]
                heapq.heappush(heap, (value, num_list, idx + 1))
                current_max = max(current_max, value)
            
            else:
                break
            
        return [best_start, best_end]