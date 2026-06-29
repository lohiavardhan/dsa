import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordlist = set(wordList)
        visited = set()
        

        def dfs(curr_word, res):
            print(curr_word)
            if curr_word == endWord:
                return res
            if curr_word in visited:
                return 0
            
            visited.add(curr_word)

            for i in range(len(curr_word)):
                for c in string.ascii_lowercase:
                    word_list = list(curr_word)
                    temp = word_list[i]
                    word_list[i] = c
                    word_string = "".join(word_list)
                    if word_string in wordlist:
                        x = dfs(word_string, res + 1)
                        if x:
                            print(x)
                            return x
            visited.remove(curr_word)
        

        x = dfs(beginWord, 0)
        print(x)

        return x if x else 0

