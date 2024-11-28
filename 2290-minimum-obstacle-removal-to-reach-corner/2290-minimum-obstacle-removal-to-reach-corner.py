class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        moves=[[1,0],[-1,0],[0,1],[0,-1]]
        q=deque([(0,0,0)])
        visit=set()
        visit.add((0,0))

        while q:
            r,c,orum=q.popleft()
            if r==row-1 and c==col-1:
                return orum
            for mr,mc in moves:
                if min(r+mr,c+mc) < 0 or r+mr==row or c+mc==col or (r+mr,c+mc) in visit:
                    continue
                visit.add((r+mr,c+mc))
                if grid[r+mr][c+mc]==1:
                    q.append((r+mr,c+mc,orum+1))
                else:
                    q.appendleft((r+mr,c+mc,orum))
        return -1

