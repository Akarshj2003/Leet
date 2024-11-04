class Solution:
    def compressedString(self, word: str) -> str:
        c=word[0]
        no=0
        ans=""
        for i in word:
            if c != i or no >= 9:
                ans+=f"{no}{c}"
                c=i
                no=1
            elif c==i and no < 10:
                no+=1
        ans+=f"{no}{c}"
        return ans