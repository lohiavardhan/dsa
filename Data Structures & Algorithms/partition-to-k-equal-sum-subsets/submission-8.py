class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        length = sum(nums) / k
        nums.sort(reverse=True)
        visited = [False for _ in nums]

        def backtrace(i, curr_part, curr_sum):
            if curr_part == 0:
                return True
            
            if curr_sum == length:
                return backtrace(0, curr_part - 1, 0)
            
            for j in range(i, len(nums)):
                if visited[j] or nums[j] + curr_sum > length:
                    continue
                
                visited[j] = True
                if backtrace(j + 1, curr_part, curr_sum + nums[j]):
                    return True
                visited[j] = False
            
            return False
        
        return backtrace(0, k, 0)

