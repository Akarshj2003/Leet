class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1],grid[1][0])>1:
            return -1
        row,col=len(grid),len(grid[0])
        hep=[(0,0,0)]
        visited=set()

        while hep:
            t,ro,co=heappop(hep)
            if (ro,co)==(row-1,col-1):
                return t

            naiber=[(ro,co+1),(ro,co-1),(ro+1,co),(ro-1,co)]

            for r,c in naiber:
                if r<0 or c<0 or r==row or c==col or (r,c) in visited:
                    continue
                wait = 1
                if abs(grid[r][c] - t) % 2 ==1:
                    wait=0
                nt=max(t+1,grid[r][c]+wait)
                heappush(hep,(nt,r,c))
                visited.add((r,c))

        