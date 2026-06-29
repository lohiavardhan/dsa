class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        answer = 0

        def xor(xor_list):
            if(xor_list == []):
                return 0
            xor_answer = 0
            for numer in xor_list:
                xor_answer ^= numer
            
            return xor_answer

        def dfs(i, curr_list):
            nonlocal answer

            if i == len(nums):
                answer += xor(curr_list.copy())
                return
            
            curr_list.append(nums[i])
            dfs(i + 1, curr_list)
            curr_list.pop()
            dfs(i + 1, curr_list)

        dfs(0, [])
        return answer
        