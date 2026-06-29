class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        index1 = 0
        
        for index1 in range(len(nums)):

            for index2 in range(index1 + 1, len(nums)):
                if(nums[index2] == nums[index1]):
                    print(index2, index1)
                    return True
        
        return False

         