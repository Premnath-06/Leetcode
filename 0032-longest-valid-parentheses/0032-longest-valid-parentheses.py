class Solution(object):
    def longestValidParentheses(self, s):
        left_count = right_count = max_len = 0
        for char in s:
            if char == '(':
                left_count += 1
            else:
                right_count += 1
            if left_count == right_count:
                max_len = max(max_len, 2 * right_count)
            elif right_count > left_count:
                left_count = right_count = 0
        left_count = right_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left_count += 1
            else:
                right_count += 1
            if left_count == right_count:
                max_len = max(max_len, 2 * left_count)
            elif left_count > right_count:
                left_count = right_count = 0
        return max_len

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna