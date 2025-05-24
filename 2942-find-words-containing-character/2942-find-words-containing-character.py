class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        words_having_x=[]
        for i,word  in enumerate(words):
            if x in word:
                words_having_x.append(i)
        return words_having_x
        