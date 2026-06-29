class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        nums.sort()

        print(nums)

        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            value_out = nums[i]

            for j in range(i + 1, len(nums)):
                l = j

                r = len(nums) - 1

                while l < r:
                    if nums[l] + nums[r] == 0 - value_out:
                        print(f'{i=}, {nums[i]=}, {l=}, {nums[l]=}, {r=}, {nums[r]=}')
                        res.append([value_out, nums[l], nums[r]])
                        break
                    
                    if nums[l] + nums[r] > 0-(value_out):
                        r -= 1
                    elif nums[l] + nums[r] < 0-(value_out):
                        l += 1
        
        return res
        