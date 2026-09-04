
    

import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s):

        freq = Counter(s)

        # Python has a min heap, so use negative frequency
        max_heap = []

        for char, count in freq.items():
            heapq.heappush(max_heap, (-count, char))

        result = []

        # Previous character that we cannot use immediately
        prev_count = 0
        prev_char = ""

        while max_heap:

            count, char = heapq.heappop(max_heap)

            # Use this character
            result.append(char)

            # We used one occurrence
            count += 1

            # Put previous character back into heap
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            # Current character becomes previous
            prev_count = count
            prev_char = char

        # If we couldn't use all characters
        if len(result) != len(s):
            return ""

        return "".join(result)
