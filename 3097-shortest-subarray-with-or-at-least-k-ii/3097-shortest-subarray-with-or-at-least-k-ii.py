class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res= float("inf")
        leg=len(str(bin(max(max(nums),k))[2:]))
        bits=[0]*leg
        def bup(bit,n,to):
            for i in range(leg):
                if n & (1 << i):
                    bit[i] += to
            return bit

        def btoi(bit):
            res=0
            for i in range(leg):
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


        