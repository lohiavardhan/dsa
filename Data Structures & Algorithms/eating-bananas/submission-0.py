class Solution:



    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        res = right

        while(left <= right):

            mid = (left + right) // 2

            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / mid)
            
            if(time_taken <= h):
                res = min(res, mid)
                right = mid - 1
            elif(time_taken > h):
                left = mid + 1
        
        
        return res
        

