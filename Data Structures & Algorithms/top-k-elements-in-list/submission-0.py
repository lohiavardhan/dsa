class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = defaultdict(int)

        for number in nums:
            hashmap[number] += 1
        
        new_dict = sorted(hashmap.items(), key = lambda x: -x[1])
        print(new_dict)
        answer_list = []
        for i in range(k):
            answer_list.append(k[i][0])
        
        return answer_list
