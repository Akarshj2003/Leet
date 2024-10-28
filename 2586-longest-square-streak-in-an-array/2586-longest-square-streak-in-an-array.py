class Solution:
    def longestSquareStreak(self, num: List[int]) -> int:
        nums=set(num)
        def maxl(n):
            re=-1
            sq=n*n
            if sq in nums:
                re=2
                sq*=sq
                while sq in nums:
                    re+=1
                    sq*=sq
            return re
        maxu=-1
        for i in nums:
            maxu= max(maxu,maxl(i))
        return maxu



                
                    

                
        