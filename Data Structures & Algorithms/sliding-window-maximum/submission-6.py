class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        out = []
        queue = collections.deque()
        while r < len(nums):
            print(queue, out)
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            print(queue, out)
            

            queue.append(r)
       
            if k < r - queue[0] + 1:
                print(f'{queue=}, {r=}, {l=}, {nums[r]=}, {nums[l]=}')
                x = queue.popleft()
                l += 1
            
            
            if r >= k - 1:
                out.append(nums[queue[0]])
            r += 1
            print(queue, out)

            print()

        
        return out
