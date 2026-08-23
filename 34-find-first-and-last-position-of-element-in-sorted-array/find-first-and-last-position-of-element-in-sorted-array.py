class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)

        low = 0 
        start = -1
        end = -1

       

        high = n-1
        while low<=high:


            guess = (low + high)//2

            if nums[guess] > target:

                high = guess - 1

            

            elif nums[guess] < target:

                low = guess + 1

            else:
                start =guess

                high = guess - 1

                n = len(nums)

        low = 0 

       

        high = n-1
        while low<=high:


            guess = (low + high)//2

            if nums[guess] > target:

                high = guess - 1

            

            elif nums[guess] < target:

                low = guess + 1

            else:

                end = guess

                low = guess + 1

            
        return  [start , end]
           


          

                


                

        
      

       





        

        
        