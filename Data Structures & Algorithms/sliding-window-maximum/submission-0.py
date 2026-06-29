class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        answer = []
        
        for r in range(k, len(nums) + 1):
            curr = nums[l: r]
            curr.sort()
            answer.append(curr[-1])
            l += 1

        return answer

