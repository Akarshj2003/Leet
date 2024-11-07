class Solution:
    def largestCombination(self, candi: List[int]) -> int:
        res=0
        for i in range(32):
            co = sum(1 for n in candi if n & (1<<i) )
            res=max(res,co)
        return res