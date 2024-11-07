class Solution:
    def largestCombination(self, candi: List[int]) -> int:
        bitmax=[0]*32
        for n in candi:
            i=0
            while n > 0:
                bitmax[i] += 1&n
                i+=1
                n=n>>1
        return max(bitmax)