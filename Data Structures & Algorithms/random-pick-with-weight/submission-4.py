class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.curr_sum = 0

        for i, weight in enumerate(w):
            start = self.curr_sum
            self.curr_sum += weight
            self.prefix.append([start, self.curr_sum, i])
        


    def pickIndex(self) -> int:
        random_pick = random.randint(1, self.curr_sum)
        
        l, r = 0, len(self.prefix) - 1
        res = -1

        while l <= r:
            
            mid = (l + r) // 2
            #print(l, r, mid)

            if self.prefix[mid][1] > random_pick:
                r = mid - 1
                #res = self.prefix[mid][2]
            elif self.prefix[mid][0] < random_pick:
                l = mid + 1
                res = self.prefix[mid][2]
            else:
                res = self.prefix[mid][2]
        
       
        
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()