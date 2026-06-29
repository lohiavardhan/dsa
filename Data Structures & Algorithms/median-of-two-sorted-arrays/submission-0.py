class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2

        if len(nums2) < len(nums1):
            A, B = B, A
        
        half = (len(nums1) + len(nums2)) // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            A_Left = A[i] if i >=0 else float('-infinity')
            B_Left = B[j] if j >=0 else float('-infinity')
            A_Right = A[i + 1] if i + 1 < len(A) else float('infinity')
            B_Right = B[j + 1] if j + 1 < len(B) else float('infinity')

            if A_Left <= B_Right and B_Left <= A_Right:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(A_Left, B_Left) + min(A_Right, B_Right)) / 2
                else:
                    return min(A_Right, B_Right)
            elif A_Left > B_Right:
                r = i - 1
            else:
                l = r + 1