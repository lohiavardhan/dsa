class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        
        min_heap = []
        i = 0
        res = []
        time = 0 

        while min_heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][0], tasks[i][2]))
                i += 1
            
            if min_heap:
                duration, start, index = heapq.heappop(min_heap)
                res.append(index)
                time += duration
            else:
                time = tasks[i][0]
        
        return res
