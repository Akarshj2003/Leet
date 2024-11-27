class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj=[[i+1] for i in range(n)]
        
        def short():
            q=deque()
            q.append((0,0))
            visit=set()
            visit.add((0,0))
            while q:
                cur,leng =q.popleft()
                if cur == n-1:
                    return leng
                for nei in adj[cur]:
                    if nei not in visit:
                        q.append((nei,leng+1))
                        visit.add(nei)
                


        res=[]
        for s,e in queries:
            adj[s].append(e)
            res.append(short())


        return res
        