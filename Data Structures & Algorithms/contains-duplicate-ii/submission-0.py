class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        res = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]] = i
            else:
                if abs(res[nums[i]] - i) <= k:
                    return True
                else:
                    res[nums[i]] = i
        
        return False