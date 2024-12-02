class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ar=sentence.split(" ")
        for i,e in enumerate(ar):
            if e.startswith(searchWord):
                return i + 1
        return -1
        