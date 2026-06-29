class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        counter = 0

        for word in words:
            if word[:n] == pref:
                counter += 1
        
        return counter