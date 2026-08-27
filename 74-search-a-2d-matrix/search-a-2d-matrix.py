class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Find the possible row
        low = 0
        high = rows - 1

        while low <= high:

            mid = (low + high) // 2

            # Target is below this row
            if target > matrix[mid][-1]:
                low = mid + 1

            # Target is above this row
            elif target < matrix[mid][0]:
                high = mid - 1

            # Target lies in this row
            else:
                break

        # No possible row found
        if low > high:
            return False

        # Step 2: Binary search in the selected row
        row = (low + high) // 2

        low = 0
        high = cols - 1

        while low <= high:

            mid = (low + high) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False
       
        
        