class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:
            
            if l + r % 2 == 0:
                mid = (l + r) // 2
            else:
                mid = (l + r + 1) // 2
            print(f'l = {l}, r = {r}, mid={mid}, nums[l] = {nums[l]}, nums[r] = {nums[r]}, nums[mid] = {nums[mid]}')
            if nums[l] < nums[mid]:
                l = mid
                continue
            elif nums[r] > nums[mid]:
                r = mid
                continue
            
            break

        return nums[mid]
