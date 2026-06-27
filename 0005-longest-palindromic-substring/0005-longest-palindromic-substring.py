class Solution(object):
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            s1 = self.expand(s, i, i)
            if len(s1) > len(longest):
                longest = s1
            s2 = self.expand(s, i, i + 1)
            if len(s2) > len(longest):
                longest = s2
        return longest
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
