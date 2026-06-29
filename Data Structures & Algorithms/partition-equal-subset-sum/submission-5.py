class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total / 2
        hashset = {0}

        for i in range(len(nums) - 1, -1, -1):
            set_copy = hashset.copy()
            for val in hashset:
                if val == target:
                    return True
                
                if val + nums[i] == target:
                    return True
                
                set_copy.add(val + nums[i])
            hashset = set_copy
        
        return False