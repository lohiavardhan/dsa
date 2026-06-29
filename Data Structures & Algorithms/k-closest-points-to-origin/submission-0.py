class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance = [math.sqrt(n[0]**2 + n[1]**2) for n in points]
        heapq.heapify(points)
        answer = []

        while k > 0:
            answer.append(heapq.heappop(points))
            k -= 1
        
        print(answer)

        return answer