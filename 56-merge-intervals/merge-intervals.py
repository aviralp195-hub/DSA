class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        result = [intervals[0]]

        for i in range (1 , len(intervals)):

            curr_s= intervals[i][0]
            curr_e= intervals[i][1]

            lastend = result[-1][1]

            if curr_s <= lastend:

                result[-1][1] = max( lastend , curr_e)

            else:

                 result.append(intervals[i])

        return result
     
        