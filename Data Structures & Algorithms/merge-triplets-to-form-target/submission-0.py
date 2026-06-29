class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        for i in range(len(triplets)):
            for j in range(i, len(triplets)):
                if [max(triplets[i][0], triplets[j][0]), max(triplets[i][1], triplets[j][1]), max(triplets[i][2], triplets[j][2])] == target:
                    return True
        
        return False