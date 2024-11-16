class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res=[]
        if len(nums)==1 or k==1:
            return nums

        for i in range(len(nums)-(k-1)):
            r=-1
            re=nums[i+(k-1)]
            c=1
            for i in range(i,i+(k-1)):
                if nums[i]+1!=nums[i+1]:
                    break
                r=nums[i+1]
                c+=1
            res.append(r if r == re and c==k else -1)
        return res
        