class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c=0
        for i in arr:
            if i%2!=0:
                c+=1
                if c==3:
                    return True
            else:
                c=0
        return False