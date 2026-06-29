class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        answer_list = []
        for key in dictionary:
            if dictionary[key] >= k:
                answer_list.append(key)

        return answer_list

        