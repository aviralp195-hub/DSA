class Solution(object):
    def findKthLargest(self, nums, k):

        import heapq

        n = len(nums)


        min_heap = []

        for i in range(k):
            heapq.heappush(min_heap, nums[i])

        for i in range(k,n):

            if nums[i] > min_heap[0]:
                
                

                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])

        return min_heap[0]

        