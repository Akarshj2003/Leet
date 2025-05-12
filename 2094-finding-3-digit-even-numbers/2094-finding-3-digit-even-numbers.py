from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count=Counter(map(str,digits))
        def isposs(n):
            ncount=Counter(str(n))
            return ncount==ncount & count

        return [r for r in range(100,1000) if r%2==0 and isposs(r)]

