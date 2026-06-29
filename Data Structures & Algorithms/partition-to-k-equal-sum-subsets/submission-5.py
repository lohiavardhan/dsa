class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) // k

        used = [False for _ in nums]
        nums.sort(reverse=True)

        def backtrack(i, side, curr_size):
            if side == 0:
                return True
            
            if curr_size == target:
                return backtrack(0, side - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or (curr_size + nums[j]) > target:
                    continue

                used[j] = True
                if backtrack(j + 1, side, curr_size + nums[j]):
                    return True
                
                used[j] = False
        
            return False
        
        return backtrack(0, k, 0)