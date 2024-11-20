class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        co=[0,0,0]
        for i in s:
            co[ord(i)-ord("a")]+=1
        if min(co) < k :
            return -1 
        res=float("inf")
        l=0
        for r in range(len(s)):
            co[ord(s[r])-ord("a")]-=1
            while min(co) < k:
                co[ord(s[l])-ord("a")]+=1
                l+=1
            res=min(res,len(s)-(r-l+1))
        return res