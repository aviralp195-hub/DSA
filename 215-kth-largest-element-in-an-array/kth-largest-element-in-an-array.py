import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        # Initialize a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Process the remaining elements
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])
                
        # The root of the min-heap is the kth largest element
        return min_heap[0]