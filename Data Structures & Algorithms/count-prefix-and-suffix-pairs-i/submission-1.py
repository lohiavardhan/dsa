class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def is_prefix_and_suffix(w1, w2):
            return len(w1) <= len(w2) and w2.startswith(w1) and w2.endswith(w1)

        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if is_prefix_and_suffix(words[i], words[j]):
                    count += 1
        
        return count
                