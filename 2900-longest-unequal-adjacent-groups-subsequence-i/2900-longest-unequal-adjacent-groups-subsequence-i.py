class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return words
        out=[words[0]]
        for i in range(1,len(words)):
            if groups[i]!=groups[i-1]:
                out.append(words[i]) 
        return out