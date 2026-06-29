class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        for n in range(len(points)):
            x = points[n][0]
            y = points[n][1]
            area = math.sqrt(x**2 + y**2)
            points[n] = [area, x, y]

        
        heapq.heapify(points)
        answer = []
        while k > 0:
            answer.append(heapq.heappop(points)[1:])
            k -= 1


        return answer