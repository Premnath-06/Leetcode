class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def dfs(i, target, path):
            if target == 0:
                res.append(list(path))
                return
            if target < 0:
                return
            for curr in range(i, len(candidates)):
                if curr > i and candidates[curr] == candidates[curr - 1]:
                    continue
                path.append(candidates[curr])
                dfs(curr + 1, target - candidates[curr], path)
                path.pop()
        dfs(0, target, [])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna