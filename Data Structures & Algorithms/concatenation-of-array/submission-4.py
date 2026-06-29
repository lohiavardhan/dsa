class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        for num in nums:
            ans.append(num)
            i += 1
        for num in nums:
            ans.append(num)
            i += 1
        return ans