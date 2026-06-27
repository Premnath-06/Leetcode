class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            h_left = height[left]
            h_right = height[right]
            current_water = (right - left) * (h_left if h_left < h_right else h_right)
            if current_water > max_water:
                max_water = current_water
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        return max_water
