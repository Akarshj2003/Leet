class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n
        csum=0
        l=0
        if k==0:
            return res
        for r in range(n+abs(k)):
            csum+=code[r%n]
            if (r-l)+1 > abs(k):
                csum-=code[l%n]
                l+=1
                if k>0:
                    res[(l-1)%n]=csum
                elif k<0:
                    res[(r+1)%n]=csum
        return res