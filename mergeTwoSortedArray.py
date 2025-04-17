
from typing import List


def merge(nums1, m, nums2, n):
    # Pointers for nums1, nums2, and the merged array
    p1 = m - 1  # Last element in the initial part of nums1
    p2 = n - 1  # Last element in nums2
    p = m + n - 1  # Last position in nums1

    # Traverse from the end and fill nums1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
