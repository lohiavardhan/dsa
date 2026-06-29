class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        list_present = []

        for num in nums:
            if num in list_present:
                return True
            else:
                list_present.append(num)
        
        return False   