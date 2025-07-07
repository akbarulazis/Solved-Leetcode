class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0
        events.sort()
        
        count = 0
        day = 1
        i = 0
        heap = []  
        

        while i < len(events) or heap:
    
            while i < len(events) and events[i][0] == day:
                heapq.heappush(heap, events[i][1])  
                i += 1
            
         
            while heap and heap[0] < day:
                heapq.heappop(heap)
            

            if heap:
                heapq.heappop(heap)  
                count += 1
            
            day += 1
        
        return count