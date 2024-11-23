class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ro,co=len(box),len(box[0])
        for r in range(ro):
            i=co-1
            for c in reversed(range(co)):
                if box[r][c]=="#":
                    box[r][c], box[r][i]=box[r][i], box[r][c]
                    i-=1
                elif box[r][c]=='*':
                    i=c-1
        print(box)
        res=[]
        for c in range(co):
            col=[]
            for r in reversed(range(ro)):
                col.append(box[r][c])
            res.append(col)
        return res
        