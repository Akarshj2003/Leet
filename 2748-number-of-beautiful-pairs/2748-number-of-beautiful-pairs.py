from math import gcd 
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        c=0
        def get_first_digit(number):
            while number >= 10:
                number//=10
            return number
        def get_last_digit(number):
            return number % 10

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if gcd(get_first_digit(nums[i]),get_last_digit(nums[j]))==1:
                    c+=1
        return c