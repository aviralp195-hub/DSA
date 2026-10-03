class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        i = 0
        j = k - 1
        count = 0

        total = sum(arr[i:j+1])

        while j < len(arr):

            avg = total / k

            if avg >= threshold:
                count += 1
            i += 1
            j += 1

            if j < len(arr):
                total = total - arr[i-1] + arr[j]

        return count
       