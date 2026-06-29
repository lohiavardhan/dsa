
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1
            
            hashmap[tuple(count)].append(string)
        
        return list(hashmap.values())

        # First sort the current string so it is alphabetically so anagrams are the same.
        # Then append it to the current alphabet's string and then return only the values.


        
            