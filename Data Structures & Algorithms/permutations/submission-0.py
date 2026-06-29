class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        
        def backtrack(curr_idx):
            if(curr_idx >= len(nums)):
                res.append(nums.copy())
                return
            
            for i in range(curr_idx, len(nums)):
                nums[curr_idx], nums[i] = nums[i], nums[curr_idx]
                backtrack(curr_idx + 1)
                nums[curr_idx], nums[i] = nums[i], nums[curr_idx]

        backtrack(0) 
        return res
            
            
            
            


            



        return res