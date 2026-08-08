class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix_sum = 0
        count = 0
        
        hashmap = {0: 1}

        for num in nums:
            prefix_sum += num

            remainder = prefix_sum % k

            if remainder in hashmap:
                count += hashmap[remainder]
                hashmap[remainder] += 1
            else:
                hashmap[remainder] = 1

        return count
     
        