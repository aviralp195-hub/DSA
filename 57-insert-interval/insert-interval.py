
class Solution(object):
    def insert(self, intervals, newInterval):
   
        inserted = False

        # Step 1: Insert newInterval at the correct position
        for i in range(len(intervals)):

            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                inserted = True
                break

        # If newInterval is greater than all intervals
        if inserted == False:
            intervals.append(newInterval)

        # Step 2: Merge overlapping intervals
        result = [intervals[0]]

        for i in range(1, len(intervals)):

            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])

            else:
                result.append(intervals[i])

        return result

    
        
     
        
        