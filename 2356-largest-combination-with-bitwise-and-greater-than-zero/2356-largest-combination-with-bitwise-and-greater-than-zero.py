class Solution:
    def largestCombination(self, candi: List[int]) -> int:
        res=0
        for i in range(32):
            co = 0
            for n in candi:
                co+=1 if (1<<i) & n else 0
            
            res=max(res,co)
        return res