class MedianFinder:

    def __init__(self):
        self.heap = []
        

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        heapq.heapify(self.heap)

    def findMedian(self) -> float:
        lst = []

        while self.heap:
            lst.append(heapq.heappop(self.heap))
        
        self.heap = lst
        heapq.heapify(self.heap)

        if (len(lst) % 2) == 0:
            print(len(lst) // 2, len(lst) // 2 - 1)
            return (lst[len(lst) // 2] + lst[(len(lst) // 2) - 1]) / 2
        else:
            return lst[len(lst) // 2]
        
        
        
        