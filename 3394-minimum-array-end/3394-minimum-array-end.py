class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        ix = 1
        i_n = 1

        while i_n <=n-1:
            if ix & x == 0:
                if i_n & (n-1):
                    res = res | ix
                i_n = i_n << 1

            ix=ix << 1
        return res