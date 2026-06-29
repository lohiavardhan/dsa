class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        parts_sum = [0, 0, 0]

        def backtrack(i):
            if i == len(nums):
                return parts_sum[0] == parts_sum[1] == parts_sum[2]
            
            for x in range(3):
                parts_sum[x] += nums[i]
                res = backtrack(i + 1)
                if res:
                    return True
                parts_sum[x] -= nums[i]

            return False
            
        return backtrack(0)