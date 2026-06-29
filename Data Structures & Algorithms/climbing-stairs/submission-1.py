class Solution:
    def climbStairs(self, n: int) -> int:

        arr = [0 for i in range(n)]
        arr[n-1] = 1
        arr[n-2] = 1

        i = n - 3
        while(i >= 0):
            print(arr)
            arr[i] = arr[i + 1] + arr[i + 2]
            i -= 1
            
        
        return arr[0] + arr[1]
        