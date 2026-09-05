
import heapq
class Solution(object):

    def findMaximizedCapital(self, k, w, profits, capital):


        projects = sorted(zip(capital, profits))

        max_heap = []
        i = 0

        for _ in range(k):
            # Jo projects current capital me possible hain
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # Koi project affordable nahi hai
            if not max_heap:
                break

            # Affordable projects me maximum profit wala choose karo
            w += -heapq.heappop(max_heap)

        return w

      
        