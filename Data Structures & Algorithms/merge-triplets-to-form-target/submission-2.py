class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        curr = [0, 0, 0]

        for triplet in triplets:

            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            if curr == target:
                return True
            
            if (triplet[0] == target[0]) or (triplet[1] == target[1]) or (triplet[2] == target[2]):
                curr = [max(curr[0], triplet[0]), max(curr[1], triplet[1]), max(curr[2], triplet[2])]
            
            
            print(curr, triplet)

        return curr == target