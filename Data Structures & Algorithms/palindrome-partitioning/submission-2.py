class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = list()

        def is_pali(string):
            return string == string[::-1]

        def dfs(curr_list, i):
            if i == len(s):
                answer.append(curr_list.copy())
                return

            for j in range(i, len(s)):
                if is_pali(s[i:j+1]):
                    curr_list.append(s[i:j+1])
                    dfs(curr_list, j+1)
                    curr_list.pop()
        dfs([], 0)
        return answer



                



                