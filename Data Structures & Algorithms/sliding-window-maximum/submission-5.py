class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        out = []
        queue = collections.deque()
        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                l += 1
                queue.popleft()
            
            queue.append(r)

            #print(queue[0], r - k + 1)
       
            if k < r - l + 1:
                print(f'{queue=}, {r=}, {l=}, {nums[r]=}, {nums[l]=}')
                x = queue.popleft()
                l += 1
                
            if r >= k - 1:
                out.append(nums[queue[0]])
            r += 1

        
        return out
