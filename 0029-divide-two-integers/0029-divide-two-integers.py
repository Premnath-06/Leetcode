class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            num_divisors = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisors <<= 1
            dividend -= temp_divisor
            quotient += num_divisors
        return quotient * sign

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna