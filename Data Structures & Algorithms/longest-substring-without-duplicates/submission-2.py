class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        l = 0
        r = 1

        res = 0

        visited = set()
        visited.add(s[l])
        curr = 1

        while r < len(s):
            if s[r] in visited:
                visited.clear()
                res = max(res, curr)
                curr = 1
                l += 1
                visited.add(s[l])
                r = l + 1
            else:
                visited.add(s[r])
                curr += 1
                r += 1
        
        res = max(res, curr)
        return res

            