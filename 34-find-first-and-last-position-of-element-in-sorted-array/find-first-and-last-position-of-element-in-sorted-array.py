class Solution(object):
    def searchRange(self, nums, target):
        i = 0 

        j = len(nums) - 1

        res = [-1, -1]

        while i <= j:

            mid = (i + j) // 2

            if nums[mid] == target:

                res[0] = mid 

                j = mid - 1

                

                   

            elif nums[mid] < target:

                i = mid + 1
                
            else :

                j = mid - 1
        i = 0 

        j = len(nums) - 1

        

        while i <= j:

            mid = (i + j) // 2

            if nums[mid] == target:

                res[1] = mid 

                i = mid + 1

                

                   

            elif nums[mid] < target:

                i = mid + 1
                
            else :

                j = mid - 1
        return res

        
           


          

                


                

        
      

       





        

        
        