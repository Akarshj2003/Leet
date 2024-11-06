class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        d={}
        for i in nums:    
            d[i]=(sum(map(int,(bin(i)[2:]))))

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] > nums[j]:
                    if d[nums[i]]==d[nums[j]]:
                        temp=nums[i]
                        nums[i]=nums[j]
                        nums[j]=temp
                    else:
                        return False
        return True
        