class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        movs ={
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }
        b="".join([str(c) for row in board for c in row])
        q=deque([(b.index("0"),b,0)])
        seen=set([b])
        while q:
            i,b,leng=q.popleft()
            if b=="123450":
                return leng
            ba=list(b)
            for j in movs[i]:
                nb=ba.copy()
                nb[i],nb[j]=nb[j],nb[i]
                nb="".join(nb)
                if nb not in seen:
                    q.append((j,nb,leng+1))
                    seen.add(nb)
        return -1