class Solution:
    def rob(self, nums: List[int]) -> int:
        def hrobber1(new_list):
            if not new_list:
                return 0
            if len(new_list) == 1:
                return new_list[0]
            if len(new_list) == 2:
                return max(new_list)
            
            answer_array = [0 for _ in new_list]
            answer_array[0] = new_list[0]
            answer_array[1] = max(new_list[0], new_list[1])

            for num in range(2, len(new_list)):
                answer_array[num] = max(new_list[num] + answer_array[num - 2], answer_array[num - 1])
                
            
            return answer_array[len(new_list) - 1]
        
        # return hrobber1(nums)
        if len(nums) == 1:
            return nums[0]
        return max(hrobber1(nums[1:]), hrobber1(nums[:-1]))

          