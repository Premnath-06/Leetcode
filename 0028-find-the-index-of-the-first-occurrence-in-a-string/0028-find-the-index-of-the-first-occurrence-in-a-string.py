class Solution(object):
    def strStr(self, haystack, needle):
        h_len, n_len = len(haystack), len(needle)
        for i in range(h_len - n_len + 1):
            if haystack[i:i + n_len] == needle:
                return i
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna