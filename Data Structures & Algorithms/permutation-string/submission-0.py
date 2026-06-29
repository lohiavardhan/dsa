class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        checkHash = defaultdict(int)
        slidingHash = defaultdict(int)

        for s in s1:
            checkHash[s] += 1
        

        l = 0


        for r in range(len(s2)):
            slidingHash[s2[r]] += 1

            if slidingHash == checkHash:
                return True

            if (r - l + 1) >= len(s1):
                slidingHash[s2[l]] -= 1
                if slidingHash[s2[l]] == 0:
                    del slidingHash[s2[l]]
                l += 1
            
            
            
                


        return False