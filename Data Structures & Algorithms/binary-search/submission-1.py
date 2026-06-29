class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r)// 2
            print(f'{l=}, {nums[l]=}, {r=}, {nums[r]=}, {mid=}, {nums[mid]}')

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        
        return -1
        