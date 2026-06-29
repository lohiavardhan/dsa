class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        rate = 1
        
        while True:
            time = 0

            for pile in piles:
                time += math.ceil(pile / rate)
            
            if time > h:
                rate += 1
            else:
                return rate 