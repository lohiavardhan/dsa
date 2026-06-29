class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashtable = {}

        for string in s:
            if string in hashtable:
                hashtable[string] += 1
            else:
                hashtable[string] = 1
        
        for string in t:
            if string in hashtable:
                hashtable[string] -= 1
            else:
                return False
        
        return all(hashtable[x] == 0 for x in s)