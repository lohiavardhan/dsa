class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dictionary = collections.defaultdict(int)
        for i in range(len(nums)):
            dictionary[nums[i]] += 1

            if len(dictionary) >= 2:
                new_dict = collections.defaultdict(int)
                for key, value in dictionary.items():
                    if value > 1:
                        new_dict[key] = value - 1
                
                dictionary = new_dict
        
        return next(iter(dictionary))