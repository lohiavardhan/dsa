class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = 0
        frequency = {}
        for task in tasks:
            if task not in frequency:
                frequency[task] = 0
            frequency[task] += 1
        
        queue = collections.deque()
        frequencies = [-x for x in frequency.values()]
        heapq.heapify(frequencies)
        while frequencies or queue:
            
            count += 1

            if queue and queue[0][1] < count:
                print(count, frequencies, queue)
                curr, _ = queue.popleft()
                curr -= 1
                if curr > 0:
                    queue.append((curr, count + n))
            elif frequencies:
                print(count, frequencies, queue)
                curr = - heapq.heappop(frequencies)
                curr -= 1
                if curr > 0:
                    queue.append((curr, count + n))
                    
            else:
                print('idle')
                continue
            
        return count