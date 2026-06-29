class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_cap = s.upper()
        t_cap = t.upper()

        l = 0
        original = [0 for _ in range(26)]
        for char in t_cap:
            original[ord(char)- ord('A')] += 1

        curr_window = [0 for _ in range(26)]

        similarity = 0
        answer = ''
        max_size = float('inf')
        
        for r in range(len(s_cap)):
            curr_window[ord(s_cap[r]) - ord('A')] += 1
        
            if curr_window[ord(s_cap[r]) - ord('A')] == original[ord(s_cap[r]) - ord('A')]:
                similarity += 1
            
            while similarity == len(t):
                print(f'{l=}, {r=}, {s[l:r + 1]=}, {similarity=}')
                if (r - l + 1) < max_size:
                    max_size = r - l + 1
                    answer = s[l:r + 1]
                if curr_window[ord(s_cap[l]) - ord('A')] == original[ord(s_cap[l]) - ord('A')]:
                    similarity -= 1
                
                curr_window[ord(s_cap[l]) - ord('A')] -= 1
                l += 1



        return answer