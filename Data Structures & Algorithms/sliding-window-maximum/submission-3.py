class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = 0
        out = []
        queue = collections.deque()
        while r < len(nums):
            print(queue, out)
            while queue and nums[r] > nums[queue[0]]:
                queue.popleft()
            
            queue.append(r)
       
            if queue[0] < r - k + 1:
                queue.popleft()
            if r >= k - 1:
                out.append(nums[queue[0]])
            r += 1

        
        return out
