class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashtable = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashtable:
                return [hashtable[diff], i]
            else:
                hashtable[nums[i]] = i

            print(hashtable)