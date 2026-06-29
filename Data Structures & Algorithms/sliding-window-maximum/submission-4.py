class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = 0
        out = []
        queue = collections.deque()
        while r < len(nums):
            print(queue, out)
            if queue:
                print(f'outside {nums[r]=} {nums[queue[0]]=}')
            while queue and nums[r] > nums[queue[-1]]:
                queue.popleft()
            
            queue.append(r)

            print(queue[0], r - k + 1)
       
            if k <= r - queue[0]:
                x = queue.popleft()
                print(nums[x])
            if r >= k - 1:
                out.append(nums[queue[0]])
            r += 1

        
        return out
