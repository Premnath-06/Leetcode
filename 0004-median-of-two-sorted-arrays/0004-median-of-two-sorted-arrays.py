class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        total_length = len(merged)
        if total_length % 2 == 1:
            middle_index = total_length // 2
            return merged[middle_index]
        else:
            middle_right = total_length // 2
            middle_left = middle_right - 1
            median = (merged[middle_left] + merged[middle_right]) / 2.0
            return median
