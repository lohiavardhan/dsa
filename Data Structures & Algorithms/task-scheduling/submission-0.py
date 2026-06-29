class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = collections.deque()

        while maxHeap or queue:
            time += 1
            if maxHeap:
                top = heapq.heappop(maxHeap)
                top += 1

                if top < 0:
                    queue.append((top, time + n))
            
            if queue:
                if queue[0][1] == time:
                    add_to_heap = queue.popleft()
                    heapq.heappush(maxHeap, add_to_heap[0])
        
        return time