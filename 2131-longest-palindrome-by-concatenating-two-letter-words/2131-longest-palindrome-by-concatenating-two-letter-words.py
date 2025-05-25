class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        not_same={}
        same={}
        odds=0
        res=0
        for word in words:
            if word[0]==word[1]:
                if same.get(word,0) > 0:
                    same[word] -= 1
                    res+=4
                else:
                    same[word]=same.get(word,0)+1
            else:
                if not_same.get(word[::-1],0) > 0:
                    not_same[word[::-1]] -= 1
                    res+=4
                else:
                    not_same[word] = not_same.get(word,0)+1
        for not_used_same_word_count in same.values():
            if not_used_same_word_count > 0:
                res+=2
                break
        return res


                    