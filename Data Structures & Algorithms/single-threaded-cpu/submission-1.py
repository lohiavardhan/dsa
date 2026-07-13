class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        pending = []
        available = []
        res = []

        for i, task in enumerate(tasks):
            heapq.heappush(pending, (task[0], task[1], i))
        
        time = 0
        added = False
        
        while pending or available:
            #print(f'{time=}, {pending=}, {available=}')
            while pending and time >= pending[0][0]:
                start, duration, index = heapq.heappop(pending)
                heapq.heappush(available, (duration, start, index))
            
            if available:
                duration, start, index = heapq.heappop(available)
                res.append(index)
                time += duration
                continue
            
            time = pending[0][0]
        
        return res
            
            
            

            
