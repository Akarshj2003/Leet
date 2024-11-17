class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res=len(nums) + 1
        dq=deque()
        csum=0
        for  r in range(len(nums)):
            csum+=nums[r]
            if csum >= k:
                res=min(res,r+1)
            while dq and csum- dq[0][0] >= k:
                v,e=dq.popleft()
                res=min(res,r-e)
            while dq and dq[-1][0]>csum:
                dq.pop()
            dq.append((csum,r))
        return -1 if res==len(nums) + 1 else res 
