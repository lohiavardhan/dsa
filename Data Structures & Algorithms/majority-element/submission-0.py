class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        maximum = max(counter.items(), key=lambda x: x[1])
        
        return maximum[0]