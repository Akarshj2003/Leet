class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[1]*n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i]= max(lis[i],lis[j]+1)
        print(lis)
        return max(lis)