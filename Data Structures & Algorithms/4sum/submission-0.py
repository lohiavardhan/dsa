class Solution:
    def twoSum(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] == target:
                return [nums[l], nums[r]]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        
        return []

    def threeSum(self, nums, target):
        for i in range(len(nums)):
            twoSum_res = self.twoSum(nums[:i] + nums[i + 1: ], target - nums[i])
            if len(twoSum_res) > 0:
                twoSum_res.append(nums[i])
                return twoSum_res
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        
        res = set()
        for i in range(len(nums)):
            threeSum_res = self.threeSum(nums[:i] + nums[i + 1: ], target - nums[i])
            if len(threeSum_res) > 0:
                threeSum_res.append(nums[i])
                threeSum_res.sort()
                res.add(tuple(threeSum_res))


        return list(res)