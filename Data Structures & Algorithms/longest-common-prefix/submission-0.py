class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for i, word in enumerate(strs):
            strs[i] = list(word)
        
        for r in range(1, len(min(strs)) + 1):
            if not all(a[0:r] == strs[0][0:r] for a in strs):
                return "".join(strs[0][0:r - 1])
        
        return ""