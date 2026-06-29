class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        answer_list = []
        
        dictionary = sorted(dictionary.items(), reverse=True)
        print(dictionary)

        for i in range(k):
            answer_list.append(dictionary[i][0])

        return answer_list

        