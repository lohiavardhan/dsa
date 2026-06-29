class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        out = []
        queue = collections.deque()
        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            

            queue.append(r)
       
            if k < r - queue[0] + 1:
                x = queue.popleft()
            
            
            if r >= k - 1:
                out.append(nums[queue[0]])
            r += 1


        
        return out
