class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        if self.small and self.large and -self.small[0] > self.large[0]:
            n1, n2 = heapq.heappop(self.small), heapq.heappop(self.large)
            heapq.heappush(self.small, -n2)
            heapq.heappush(self.large, -n1)
        


    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]
        
        