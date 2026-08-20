class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        hashmap = {}

        for i in magazine:

            if i in hashmap:
                hashmap[i] += 1
            else:

                hashmap[i] = 1

        for j in ransomNote:
            if j not in hashmap or hashmap[j] == 0:
                return False
            hashmap[j] -= 1

        return True
       
        

        
        
    

            


    