class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = collections.defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        res = []
        print(counter)
        for (num, count) in counter.items():
            if count > len(nums) / 3:
                res.append(num)
        
        return res