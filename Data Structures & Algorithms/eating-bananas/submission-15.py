class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        answer = r
        

        while l <= r:
            
            mid = (l + r) // 2
            time = 0
            
            for pile in piles:
                time += math.ceil(pile / mid)

            if time > h:
                l = mid + 1
            else:
                answer = mid
                r = mid - 1
                
        return answer



            
