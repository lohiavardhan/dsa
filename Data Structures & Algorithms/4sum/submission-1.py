class Solution:
    def twoSum(self, nums, target):
        l = 0
        r = len(nums) - 1
        results = []
        while l < r:
            if nums[l] + nums[r] == target:
                results.append([nums[l], nums[r]])
                l += 1
                r -= 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        
        return results

    def threeSum(self, nums, target):
        results = []
        for i in range(len(nums)):
            twoSum_res = self.twoSum(nums[:i] + nums[i + 1: ], target - nums[i])
            if len(twoSum_res) > 0:
                for res in twoSum_res:
                    res.append(nums[i])
                    results.append(res)
        
        return results
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        
        res = set()
        for i in range(len(nums)):
            threeSum_res = self.threeSum(nums[:i] + nums[i + 1: ], target - nums[i])
            if len(threeSum_res) > 0:
                for result in threeSum_res:
                    result.append(nums[i])
                    result.sort()
                    res.add(tuple(result))


        return list(res)