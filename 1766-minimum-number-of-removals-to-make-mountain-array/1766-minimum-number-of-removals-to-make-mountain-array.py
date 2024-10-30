class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[1]*n

        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    lis[i]=max(lis[i],lis[j]+1)
        print(lis)
        lds=[1]*n

        for i in reversed(range(n)):
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    lds[i]=max(lds[i],lds[j]+1)
        r=n
        print(lds)
        for i in range(1,n-1):
            if min(lis[i],lds[i]) > 1:
                r = min(
                    r,
                    (n-(lis[i]+lds[i]-1))
                )
        return r

        