class Solution(object):
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = []
        for i in range(13):
            if num == 0:
                break
            count = num // values[i]
            if count:
                res.append(symbols[i] * count)
                num %= values[i]
        return "".join(res)
