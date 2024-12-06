class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cs=0
        c=0
        banned=set(banned)
        for i in range(1,n+1):
            if cs >= maxSum or cs+i > maxSum:
                break
            if i not in banned: 
                cs+=i
                c+=1
        return c
                
        