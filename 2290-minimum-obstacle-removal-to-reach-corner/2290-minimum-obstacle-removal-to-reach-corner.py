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
                nr=r+mr
                nc=c+mc
                if min(nr,nc) < 0 or nr==row or nc==col or (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                if grid[nr][nc]==1:
                    q.append((nr,nc,orum+1))
                else:
                    q.appendleft((nr,nc,orum))
        return -1

