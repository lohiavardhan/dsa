class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def is_suffix(w1, w2):
            if w1 < w2 and w1 == w2[:len(w1)]:
                return True
        
        def is_prefix(w1, w2):
            if w1 < w2 and w1 == w2[:-len(w1)]:
                return True

        count = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if is_suffix(i, j) and is_prefix(i, j):
                    count += 1
        
        return count
                