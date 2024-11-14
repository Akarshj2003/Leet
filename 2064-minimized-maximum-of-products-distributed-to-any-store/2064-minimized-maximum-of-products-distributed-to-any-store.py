class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can(x):
            stor=0
            for q in quantities:
                stor+=math.ceil(q/x)
            print(stor)
            return stor<=n


        l,r=1,max(quantities)
        res=0
        while l<=r:
            x=(l+r)//2
            print(x)
            if can(x):
                res=x
                r=x-1
            else:
                l=x+1
        return res
