class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        parts_sum = [0, 0, 0]
        nums.sort()
        if sum(nums) % k != 0:
            return False
        
        length = sum(nums) / k

        def backtrack(i):
            if i == len(nums):
                return parts_sum[0] == parts_sum[1] == parts_sum[2]
            
            for x in range(3):
                if parts_sum[x] > length:
                    continue
                parts_sum[x] += nums[i]
                res = backtrack(i + 1)
                if res:
                    return True
                parts_sum[x] -= nums[i]

            return False
            
        return backtrack(0)