class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n,m=len(str1),len(str2)
        if m>n:
            return False
        s1,s2=0,0
        while s1 < n and s2 < m :
            nex=chr((ord(str1[s1])-ord('a')+1)%26 + ord('a'))
            if(str2[s2]==str1[s1] or str2[s2]==nex ):
                s2+=1
            s1+=1
        return s2==m