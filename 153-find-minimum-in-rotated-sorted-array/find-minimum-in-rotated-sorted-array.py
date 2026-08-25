class Solution(object):
    def findMin(self, nums):
        min_element = nums[0]

        for i in range(len(nums)):

            if nums[i] < min_element:

                min_element = nums[i]

        return min_element