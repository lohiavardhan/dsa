class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = collections.defaultdict(int)

        for num in nums:
            counter[num] += 1

            if len(counter) > 2:
                nc = defaultdict(int)
                for n, c in counter.items():
                    if c > 1:
                        nc[n] = c - 1
                
                counter = nc
        
        res = []
        for num in counter:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res