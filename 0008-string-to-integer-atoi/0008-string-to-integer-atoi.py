class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res *= sign
        if res < -2147483648:
            return -2147483648
        if res > 2147483647:
            return 2147483647
        return res
