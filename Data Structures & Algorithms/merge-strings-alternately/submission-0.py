class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_list = []
        w1, w2 = 0, 0

        while w1 < len(word1) and w2 < len(word2):
            new_list.append(word1[w1])
            new_list.append(word2[w2])
            w1 += 1
            w2 += 1
        
        if w1 != len(word1):
            new_list.append(word1[w1:])
        elif w2 != len(word2):
            new_list.append(word2[w1:])
        
        return ''.join(new_list)