class Solution(object):
    def searchRange(self, nums, target):
        def find_bound(is_left):
            low, high = 0, len(nums) - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    idx = mid
                    if is_left:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return idx
        left = find_bound(True)
        if left == -1:
            return [-1, -1]
        return [left, find_bound(False)]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna