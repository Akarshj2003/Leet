class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ar=sentence.split(" ")
        for i,e in enumerate(ar):
            if searchWord in e and searchWord[0]==e[0] and searchWord[-1]==e[len(searchWord)-1]:
                return(i+1)
        return -1
        