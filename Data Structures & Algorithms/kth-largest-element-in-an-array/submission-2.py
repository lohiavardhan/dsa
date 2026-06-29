class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []
        for i in range(k):
            min_heap.append(nums[i])
        
        heapq.heapify(min_heap)
        
        i += 1
        while i < len(nums):
            heapq.heappush(min_heap, nums[i])
            heapq.heappop(min_heap)
            i += 1
        
        return min_heap[0]