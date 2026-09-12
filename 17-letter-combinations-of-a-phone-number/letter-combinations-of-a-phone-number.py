class Solution(object):
    def letterCombinations(self, digits):


        if not digits:
            
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        current = []

        def backtrack(index):

            if index == len(digits):
                result.append("".join(current))
                return

            letters = phone[digits[index]]

            for letter in letters:

                current.append(letter)

                backtrack(index + 1)

                current.pop()

        backtrack(0)

        return result


        
        