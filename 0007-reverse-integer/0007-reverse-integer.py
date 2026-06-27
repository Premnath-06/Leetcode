class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = int(str(x)[::-1]) * sign
        if res < -2147483648 or res > 2147483647:
            return 0
        return res