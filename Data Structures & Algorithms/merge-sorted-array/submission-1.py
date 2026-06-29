class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        res = []

        j = len(nums2)

        while j:
            nums1[-j] = nums2[i]
            j -= 1
            i += 1
        
        
        print(nums1)
        nums1.sort()