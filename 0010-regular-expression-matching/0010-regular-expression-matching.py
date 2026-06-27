class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 2]
        for i in range(1, m + 1):
            next_dp = [False] * (n + 1)
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    next_dp[j] = next_dp[j - 2] or (dp[j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    next_dp[j] = dp[j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
            dp = next_dp
        return dp[n]
