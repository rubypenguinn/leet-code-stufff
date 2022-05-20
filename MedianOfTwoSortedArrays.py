def findMedian(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    if len(nums1) % 2 == 0:
        right = nums1[len(nums1) // 2]
        left = nums1[(len(nums1) // 2) - 1]
        return (right + left) / 2
    else:
        return nums1[len(nums1) // 2]

nums1 = [1, 2]
nums2 = [3, 4]
median = findMedian(nums1, nums2)

print(median)

# Works.
# Faster than 84.71%
# Less than 96.89%

# So a faster solution exists