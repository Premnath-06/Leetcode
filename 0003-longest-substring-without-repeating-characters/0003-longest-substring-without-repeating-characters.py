class Solution(object):
    def lengthOfLongestSubstring(self, s):
        basket = []
        max_len = 0
        
        for char in s:
            while char in basket:
                basket.pop(0)
            basket.append(char)
            if len(basket) > max_len:
                max_len = len(basket)
                
        return max_len
