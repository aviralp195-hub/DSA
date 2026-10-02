class Solution(object):

    def combinationSum(self, candidates, target):

        ans = []

        def backtrack(start, target, path):

            if target == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):

                if candidates[i] > target:
                    continue

                path.append(candidates[i])

                backtrack(i, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])

        return ans