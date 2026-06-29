class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index in range(0, len(nums)):
            diff = target - nums[index]

            if diff in nums:
                for index2 in range(index + 1, len(nums)):
                    if nums[index2] == diff:
                        return [index, index2]

        