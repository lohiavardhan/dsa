class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, len(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            time = math.ceil(sum(piles) / k)

            if time > h:
                l = k + 1
            else:
                r = k - 1
                res = k

        return res
