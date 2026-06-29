class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        res = []

        while j < len(nums2):
            nums1[-(len(nums2) + j) + 1] = nums2[j]
            j += 1
        
        nums1.sort()