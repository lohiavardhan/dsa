class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = defaultdict(int)
        freq_arr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] += 1

        
        for number, freq in hashmap.items():
            freq_arr[freq].append(number)


        result = []
        for i in range(len(nums), 0 , -1):
           
            
            while(len(freq_arr[i]) > 0):
                if(k == 0):
                    return result
                else:
                    result.append(freq_arr[i].pop())
                    k -= 1
            if(k == 0):
                return result
