class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = collections.deque()
        q.append(beginWord)
        
        wordlist_set = set(wordList)
        
        counter = 1
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        visited = set()
        visited.add(beginWord)

        while q:
            print(q)
            for _ in range(len(q)):
                curr_word = q.popleft()
                
                if curr_word == endWord:
                    return counter
                
                curr_word_arr = list(curr_word)
                for i in range(len(curr_word)):
                    for c in alphabets:
                        temp = curr_word_arr[i]
                        curr_word_arr[i] = c
                        new_word = "".join(curr_word_arr)
                        if new_word in wordlist_set and new_word not in visited:
                            visited.add(new_word)
                            q.append(new_word)
                        curr_word_arr[i] = temp
                
            counter += 1
        return 0
