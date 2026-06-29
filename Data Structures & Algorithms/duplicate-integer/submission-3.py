class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}

        for number in nums:
            if number in hashtable:
                return True
            else:
                hashtable[number] = 1
        
        return False