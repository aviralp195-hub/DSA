class Solution(object):
    def maxTurbulenceSize(self, arr):
        i = 0

        j = 1

        prev = ""
        res = 1

        while j < len(arr):

            if arr[j]> arr[j-1] and prev != ">":
                res = max(res , j-i+1)
                


                prev = ">"
            elif  arr[j]< arr[j-1] and prev != "<":

                
                res = max(res , j-i+1)
                

               

                prev = "<"

            else:

                if arr[j] == arr[j-1]:

                    i = j

                    prev = ""

                else:

                    i = j-1

                    if arr[j] > arr[i]:

                        prev = ">"

                    else :

                        prev = "<"

                    res = max(res , j-i+1)

                   
            j = j+1
        return res




               
                

                
        