class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashmap = {}
        wordList.append(beginWord)

        for word in wordList:
            word_arr = list(word)
            for i in range(len(word)):
                temp = word_arr[i]
                word_arr[i] = "*"
                pattern = "".join(word_arr)
                if pattern not in hashmap:
                    hashmap[pattern] = []
                hashmap[pattern].append(word)
                word_arr[i] = temp
            
        q = collections.deque()
        q.append(beginWord)
        visited = set(beginWord)
        counter = 1

        while q:
            for i in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return counter
                
                word_arr = list(curr_word)
                for i in range(len(curr_word)):
                    temp = word_arr[i]
                    word_arr[i] = "*"
                    pattern = "".join(word_arr)
                    
                    print(pattern, curr_word, q)

                    if pattern in hashmap:
                        for next_word in hashmap[pattern]:
                            if next_word not in visited:
                                q.append(next_word)
                                visited.add(next_word)
                        
                    word_arr[i] = temp
                
            counter += 1
        
        return 0
