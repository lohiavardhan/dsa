class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l = 0
        r = len(arr) - 1
        closest = 0

        while l <= r:
            mid = (l + r + 1) // 2
            if arr[mid] == x:
                break
            
            print(f'{mid=}, {closest=}, {arr[mid]=}, {arr[closest]=}')
            closest = mid if abs(arr[mid] - x) < abs(arr[closest] - x) else closest
            print(f'{mid=}, {closest=}, {arr[mid]=}, {arr[closest]=}')

            if arr[mid] > x:
                r = mid - 1
            elif arr[mid] < x:
                l = mid + 1

        mid = mid if arr[mid] == x else closest
        print(mid)
        left, right = mid, mid

        for i in range(k - 1):
            left_val = arr[left - 1] if left - 1 >= 0 else float('inf')
            right_val = arr[right + 1]  if right + 1 < len(arr) else float('inf')
            print(left_val, right_val)
            if abs(x - left_val) <= abs(x - right_val):
                left -= 1
            else:
                right += 1
        
        return arr[left : right + 1]
