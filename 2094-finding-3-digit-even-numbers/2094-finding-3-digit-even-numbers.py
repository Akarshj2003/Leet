class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        out=set()
        lofD=len(digits)
        for i in range(lofD):
            for j in range(lofD):
                for k in range(lofD):
                    if i!=j and digits[i]!=0 and j!=k and k!=i:
                        num=digits[i]*100+digits[j]*10+digits[k] 
                        if num%2==0:
                            out.add(num)
        return sorted(out)