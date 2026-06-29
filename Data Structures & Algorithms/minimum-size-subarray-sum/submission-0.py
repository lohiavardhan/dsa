class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        length = float('inf')
        l = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                length = min(length, (r - l + 1))
                curr_sum -= nums[l]
                l += 1
            
        return length if length != float('inf') else 0
