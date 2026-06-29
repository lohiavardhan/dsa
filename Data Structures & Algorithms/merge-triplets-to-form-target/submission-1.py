class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        curr = [0, 0, 0]

        for triplet in triplets:
            
            if curr == target:
                return True
            
            if (curr[0] != target[0] and triplet[0] == target[0]) or (curr[1] != target[1] and triplet[1] == target[1]) or (curr[2] != target[2] and triplet[2] == target[2]):
                curr = [max(curr[0], triplet[0]), max(curr[1], triplet[1]), max(curr[2], triplet[2])]
            

        return curr == target