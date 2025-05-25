class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        not_same={}
        same={}
        odds=0
        res=0
        def is_same(word):
            if word[0]==word[1]:
                return True
            else :
                return False
        for word in words:
            if word in same:
                same[word]+=1
                res+=2
            elif is_same(word):
                same[word]=1
                res+=2
            elif word[::-1] in not_same and not_same[word[::-1]] > 0:
                not_same[word[::-1]]-=1
                res+=4
            else:
                not_same[word]=not_same.get(word,0)+1
        odds = sum(1 for count in same.values() if count % 2 == 1)
        if odds < 2:
            return res
        else:
            return res-((odds-1)*2)