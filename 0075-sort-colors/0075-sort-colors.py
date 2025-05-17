class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #three flag for three area
        red,white,blue=0,0,len(nums)-1
        while white<=blue:
            if nums[white]==0:
                nums[red],nums[white]=nums[white],nums[red]
                white+=1
                red+=1
            elif nums[white]==1:
                white+=1
            else:
                nums[blue],nums[white]=nums[white],nums[blue]
                blue-=1