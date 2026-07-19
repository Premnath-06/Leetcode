class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        current = "1"
        for _ in range(n - 1):
            next_str = []
            i = 0
            while i < len(current):
                count = 1
                while i + 1 < len(current) and current[i] == current[i + 1]:
                    count += 1
                    i += 1
                next_str.append(str(count))
                next_str.append(current[i])
                i += 1
            current = "".join(next_str)
        return current


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna