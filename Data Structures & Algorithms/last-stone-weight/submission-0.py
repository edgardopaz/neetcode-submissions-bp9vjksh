import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
            
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)

            if stone1 != stone2:
                stone3 = stone1 - stone2
                heapq.heappush(maxHeap, stone3)
        
        return -maxHeap[0] if maxHeap else 0