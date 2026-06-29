import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        total_sum = sum(piles)
        maximum = max(piles)
        length = len(piles)

        print(f'{piles=}, {total_sum=}. {maximum=}, {length=}')


        l = 1
        r = maximum

        while l <= r:
            mid = (l + r) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / mid)
            

            if time > h:
                l = mid + 1
            else:
                r = mid - 1
            print(time, mid, l, r)
        
        print(mid, l, r)

        return max(mid, l, r)
