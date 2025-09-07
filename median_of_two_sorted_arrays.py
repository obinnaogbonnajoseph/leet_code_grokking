def findMedianSortedArrays(nums1, nums2):
    """
    Finds the median of two sorted arrays using binary search.
    The overall time complexity is O(log(min(m, n))).
    """
    # Ensure nums1 is the smaller array to optimize the binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    # The total number of elements in the conceptual "left part" of the merged array
    half_len = (m + n + 1) // 2

    while low <= high:
        # partitionX is the number of elements from nums1 in the left part
        partitionX = (low + high) // 2
        # partitionY is the number of elements from nums2 in the left part
        partitionY = half_len - partitionX

        # Get the four boundary elements for the partitions
        # maxLeftX is the largest element in the left part of nums1
        maxLeftX = nums1[partitionX - 1] if partitionX != 0 else float("-inf")
        # minRightX is the smallest element in the right part of nums1
        minRightX = nums1[partitionX] if partitionX != m else float("inf")

        # maxLeftY is the largest element in the left part of nums2
        maxLeftY = nums2[partitionY - 1] if partitionY != 0 else float("-inf")
        # minRightY is the smallest element in the right part of nums2
        minRightY = nums2[partitionY] if partitionY != n else float("inf")

        # Check if we found the correct partition
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # If the total number of elements is even
            if (m + n) % 2 == 0:
                max_of_left = max(maxLeftX, maxLeftY)
                min_of_right = min(minRightX, minRightY)
                return (max_of_left + min_of_right) / 2.0
            # If the total number of elements is odd
            else:
                return float(max(maxLeftX, maxLeftY))
        elif maxLeftX > minRightY:
            # The partition in nums1 is too far to the right, move left
            high = partitionX - 1
        else:
            # The partition in nums1 is too far to the left, move right
            low = partitionX + 1
