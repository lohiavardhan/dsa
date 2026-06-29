class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False
        
        string1, string2 = [0] * 26, [0] * 26
        
        for i in range(len(s1)):
            string1[ord(s1[i]) - ord('a')] += 1
            string2[ord(s2[i]) - ord('a')] += 1
        
        common = 0
        for i in range(26):
            if string1[i] == string2[i]:
                common += 1
            
        l = 0
        for i in range(len(s1), len(s2)):
            print(common)
            if common == 26:
                return True
            
            index = ord(s2[i]) - ord('a')
            string2[index] += 1

            if string2[index] == string1[index]:
                common += 1
            elif string2[index] - 1 == string1[index]:
                common -= 1

            index = ord(s2[l]) - ord('a')
            string2[index] -= 1
            if string2[index] == string1[index]:
                common += 1
            elif string2[index] + 1 == string1[index]:
                common -= 1

            l += 1 
        print(common, string2, string1)
        return common == 26