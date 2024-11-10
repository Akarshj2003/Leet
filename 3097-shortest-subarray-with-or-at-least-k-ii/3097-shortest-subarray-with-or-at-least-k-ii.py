class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res= float("inf")
        bits=[0]*32
        def bup(bit,n,to):
            for i in range(32):
                if n & (1 << i):
                    bit[i] += to
            return bit

        def btoi(bit):
            res=0
            for i in range(32):
                if bit[i]:
                    res+=(1<<i)
            return res
        l=0
        for r in range(len(nums)):
            bits=bup(bits,nums[r],1)
            ore=btoi(bits)
            while ore>=k and l<=r:
                res = min( res ,r-l+1)
                bits=bup(bits,nums[l],-1)
                ore =btoi(bits)
                l+=1
        return -1 if res==float("inf") else res


        