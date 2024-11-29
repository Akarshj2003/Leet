class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1],grid[1][0])>1:
            return -1
        row,col=len(grid),len(grid[0])
        hep=[(0,0,0)]
        visited = [[False] * col for _ in range(row)]
        visited[0][0] = True
        naiber=((0,1),(0,-1),(1,0),(-1,0))

        while hep:
            t,ro,co=heappop(hep)
            for nr,nc in naiber:
                r,c=ro+nr,co+nc
                if r<0 or c<0 or r>=row or c>=col or visited[r][c]:
                    continue
                wait = 1
                if abs(grid[r][c] - t) % 2 ==1:
                    wait=0
                nt=max(t+1,grid[r][c]+wait)
                if (r,c)==(row-1,col-1):
                    return nt
                heappush(hep,(nt,r,c))
                visited[r][c]=True

        