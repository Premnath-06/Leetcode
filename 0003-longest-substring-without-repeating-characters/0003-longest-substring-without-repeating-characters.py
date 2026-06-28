class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        max_len = 0
        left = 0
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        return max_len
