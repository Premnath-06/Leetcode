class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        res = 0
        for char in s:
            if '0' <= char <= '9':
                res = res * 10 + (ord(char) - 48)
            else:
                break
        res *= sign
        if res < -2147483648:
            return -2147483648
        if res > 2147483647:
            return 2147483647
        return res
