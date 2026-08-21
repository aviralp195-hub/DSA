class Solution(object):
    def maxNumberOfBalloons(self, text):
        hashmap = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }

        result = float('inf')

        for ch in hashmap:
            result = min(result, text.count(ch) // hashmap[ch])

        return result

        