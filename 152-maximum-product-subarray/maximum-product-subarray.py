class Solution(object):
    def maxProduct(self, nums):
        
        maxi= float('-inf')
        n = len(nums)
        prefix = 1
        sufix = 1
        for i in range(0,n):

            if prefix == 0:
                prefix = 1
            if sufix == 0:
                sufix = 1    

            prefix = prefix * nums[i]
            sufix = sufix * nums[n - i - 1]

            

            
            

                

            maxi = max(maxi, max(sufix,prefix))

        return maxi     
       
        return result