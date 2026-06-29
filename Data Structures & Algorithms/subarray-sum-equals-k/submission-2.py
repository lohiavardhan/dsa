class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0 : 1}
        curr_sum = 0
        answer = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            answer += prefix.get(diff, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
        
        return answer
