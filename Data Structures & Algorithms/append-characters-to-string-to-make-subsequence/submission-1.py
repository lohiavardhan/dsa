class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        max_common = 0
        l = 0

        for r in range(len(s)):
            size = r - l + 1
            print(f'{s[l : r + 1]=}, {t[max_common: max_common + size]=}')
            if s[l:r + 1] == t[0: size]:
                max_common = max(max_common, size)
            elif s[l : r + 1] == t[max_common: max_common + size]:
                print(f'{s[l : r + 1]=}, {t[max_common: max_common + size]=}')
                max_common = max_common + size
            else:
                l = r + 1
        
        return len(t) - max_common