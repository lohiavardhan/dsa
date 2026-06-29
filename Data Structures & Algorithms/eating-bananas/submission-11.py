class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = min(piles)
        r = max(piles)
        answer = r
        

        while l < r:
            
            mid = (l + r) // 2
            time = 0
            
            for pile in piles:
                time += math.ceil(pile / mid)
            
            if time > h:
                l = mid + 1
            elif time < h:
                answer = mid
                r = mid - 1
            else:
                return mid
        
        return answer



            
