class Solution(object):
    def longestPalindrome(self, s):

        total = 0 

        hashmap = {}

        odd = False 

        for ch in s:
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1
      
        for chs in hashmap:

            count = hashmap[chs]

            if count % 2 == 0:

                total+=count
            else:

                total+=count - 1
                odd = True 

        if odd:

            total += 1 
        return total 