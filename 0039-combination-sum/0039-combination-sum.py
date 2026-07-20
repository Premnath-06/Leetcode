class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def dfs(i, target, path):
            if target == 0:
                res.append(list(path))
                return
            if target < 0 or i >= len(candidates):
                return
            path.append(candidates[i])
            dfs(i, target - candidates[i], path)
            path.pop()
            dfs(i + 1, target, path)
        dfs(0, target, [])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna