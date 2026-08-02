class Solution(object):
    def maxSubArray(self, nums):
        
        n = len(nums)
        total = 0
        x = float('-inf')
        for i in range(0,n):

            total = total + nums[i]

            x= max(x,total)

            if total < 0:
                total = 0

             
        return x 
