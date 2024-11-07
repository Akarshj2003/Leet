class Solution:
    def largestCombination(self, candi: List[int]) -> int:
        res=0
        m=len(str(bin(max(candi))))#can use  32 also
        for i in range(m):
            co = sum(1 for n in candi if n & (1<<i) )
            res=max(res,co)
        return res