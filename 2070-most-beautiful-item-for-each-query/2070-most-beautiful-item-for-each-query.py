class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q,i) for i,q in enumerate(queries)]) 
        maxb =0
        j=0
        res=[0]*len(queries)
        for q,i in queries:
            while j < len(items)and items[j][0] <= q:
                maxb =max(maxb,items[j][1])
                j+=1
            res[i]=maxb
        return res

                 

        