class Solution(object):
    def findMaxLength(self, nums):
        zeros = 0
        ones = 0
        max_len = 0
        
        # diff : first index
        mp = {0: -1}
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
            
            diff = zeros - ones
            
            # Same diff pehle aa chuka hai
            if diff in mp:
                length = i - mp[diff]
                max_len = max(max_len, length)
            
            # Diff pehli baar aaya hai
            else:
                mp[diff] = i
        
        return max_len
   