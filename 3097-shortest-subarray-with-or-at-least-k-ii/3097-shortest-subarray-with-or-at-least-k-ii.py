class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        co=[]
        for i in range(len(nums)):
            ore=nums[i]
            c=1
            for j in range(i+1,len(nums)):
                if ore >= k:
                    break
                ore=ore|nums[j]
                c+=1
            if ore >= k:    
                co.append(c)
        if not co:
            return -1
        return min(co)


        