class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = 0
        total = 0

        for num in nums:
            total += num
            if total < 0:
                res = 0
                total = 0
            else:
                res += 1
                total += num
        
        return res if res != 0 else -1
