import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            if largest == second:
                continue
            else:
                diff = (largest) - (second)
                heapq.heappush(max_heap, diff)
        
        return -max_heap[0]