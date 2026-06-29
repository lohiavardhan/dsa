class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            hashmap["".join(sorted(string))].append(string)
        
        return list(hashmap.values())
            