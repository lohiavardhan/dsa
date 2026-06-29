class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0:
            return False

        parts = [0 for _ in range(k)]

        length = sum(nums) // k

        nums.sort(reverse=True)

        def backtrack(i):
            
            if i == len(nums):
                return True
            
            for j in range(k):
                if(parts[j] + nums[i] <= length):
                    parts[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    parts[j] -= nums[i]
            
            return False
        
        return backtrack(0)