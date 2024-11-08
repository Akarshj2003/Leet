class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor=0
        ans=[]
        for i in nums:
            xor ^= i
        mask=(1<<maximumBit)-1
        for n in reversed(nums):
            ans.append(xor^mask)
            xor^=n
        return ans

        