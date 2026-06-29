class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        answer_list = []
        
        sorted_dictionary = sorted(dictionary.items(), key= lambda item: item[1], reverse=True)
        print(sorted_dictionary)

        for i in range(k):
            answer_list.append(sorted_dictionary[i][0])

        return answer_list

        