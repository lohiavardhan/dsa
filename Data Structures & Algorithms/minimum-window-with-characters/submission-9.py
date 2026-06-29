class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        original = collections.defaultdict(int)
        for char in t:
            original[char] += 1

        curr_window = collections.defaultdict(int)

        similarity = 0
        answer = ''
        max_size = float('inf')
        print(original)
        
        for r in range(len(s)):
            curr_window[s[r]] += 1
        
            if curr_window[s[r]] <= original[s[r]]:
                similarity += 1

            while similarity == len(t):
                if (r - l + 1) < max_size:
                    max_size = r - l + 1
                    answer = s[l:r + 1]
                if curr_window[s[l]] == original[s[l]]:
                    similarity -= 1
                
                curr_window[s[l]] -= 1
                l += 1



        return answer