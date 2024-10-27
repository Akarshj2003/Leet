class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ro,co=len(matrix),len(matrix[0])
        save={}
        def find(r,c):
            if r == ro or c == co or not matrix[r][c]:
                return 0
            if (r,c) in save:
                return  save[(r,c)]

            save[(r,c)]= 1 + min(find(r+1,c),find(r,c+1),find(r+1,c+1))
            return save[(r,c)]
        res=0
        for r in range(ro):
            for c in range(co):
                res+=find(r,c)  
        return res