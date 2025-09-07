# main.py
from typing import List

def max_subarray_linear(nums: List[int]) -> int:
    """
    Finds the subarray with the largest sum using Kadane's Algorithm.
    This is an O(n) time complexity solution.

    Args:
        nums: A list of integers.

    Returns:
        The sum of the subarray with the largest sum.
    """
    # If the list is empty, there's no subarray, so we can return 0 or raise an error.
    # The constraints say nums.length >= 1, so we don't need to handle this.
    
    # Initialize global_max and current_max with the first element of the array.
    # global_max will store the maximum sum found so far across the entire array.
    # current_max will store the maximum sum of a subarray ending at the current position.
    global_max = nums[0]
    current_max = nums[0]

    # Iterate through the array starting from the second element.
    for i in range(1, len(nums)):
        num = nums[i]
        # For each element, we have two choices:
        # 1. Start a new subarray at the current element.
        # 2. Extend the previous subarray by adding the current element.
        # We choose the one that gives a larger sum.
        current_max = max(num, current_max + num)

        # Update the global maximum sum if the current maximum sum is greater.
        if current_max > global_max:
            global_max = current_max
            
    return global_max

def max_subarray_divide_conquer(nums: List[int]) -> int:
    """
    Wrapper function to start the divide and conquer approach.

    Args:
        nums: A list of integers.

    Returns:
        The sum of the subarray with the largest sum.
    """
    return find_max_subarray_recursive(nums, 0, len(nums) - 1)

def find_max_crossing_sum(nums: List[int], left: int, mid: int, right: int) -> int:
    """
    Finds the maximum subarray sum that crosses the midpoint.
    This is a helper for the divide and conquer approach.

    Args:
        nums: The list of integers.
        left: The left index of the subarray.
        mid: The middle index of the subarray.
        right: The right index of the subarray.

    Returns:
        The maximum sum of a subarray that crosses the midpoint.
    """
    # --- Find max sum on the left side of mid ---
    # Start from the middle element and move leftwards.
    left_sum = float('-inf')
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += nums[i]
        if current_sum > left_sum:
            left_sum = current_sum

    # --- Find max sum on the right side of mid ---
    # Start from the element just after the middle and move rightwards.
    right_sum = float('-inf')
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += nums[i]
        if current_sum > right_sum:
            right_sum = current_sum
            
    # The max crossing sum is the sum of the max left-side sum and max right-side sum.
    return left_sum + right_sum

def find_max_subarray_recursive(nums: List[int], left: int, right: int) -> int:
    """
    Recursively finds the maximum subarray sum using divide and conquer.

    Args:
        nums: The list of integers.
        left: The starting index of the current subarray.
        right: The ending index of the current subarray.

    Returns:
        The maximum subarray sum within the given indices.
    """
    # Base Case: If there is only one element, it is the max subarray.
    if left == right:
        return nums[left]

    # Find the middle point to divide the array into two halves.
    mid = (left + right) // 2

    # The maximum sum can be in one of three places:
    # 1. Entirely in the left half.
    # 2. Entirely in the right half.
    # 3. Crossing the midpoint.
    
    max_left_sum = find_max_subarray_recursive(nums, left, mid)
    max_right_sum = find_max_subarray_recursive(nums, mid + 1, right)
    max_crossing = find_max_crossing_sum(nums, left, mid, right)

    # Return the maximum of the three possible sums.
    return max(max_left_sum, max_right_sum, max_crossing)


# --- Example Usage ---
print("--- Testing O(n) Linear Solution (Kadane's Algorithm) ---")
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Input: {nums1}")
print(f"Output: {max_subarray_linear(nums1)}")  # Expected: 6

nums2 = [1]
print(f"Input: {nums2}")
print(f"Output: {max_subarray_linear(nums2)}")  # Expected: 1

nums3 = [5, 4, -1, 7, 8]
print(f"Input: {nums3}")
print(f"Output: {max_subarray_linear(nums3)}")  # Expected: 23

print("\n--- Testing Divide and Conquer Solution ---")
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Input: {nums1}")
print(f"Output: {max_subarray_divide_conquer(nums1)}")  # Expected: 6

nums2 = [1]
print(f"Input: {nums2}")
print(f"Output: {max_subarray_divide_conquer(nums2)}")  # Expected: 1

nums3 = [5, 4, -1, 7, 8]
print(f"Input: {nums3}")
print(f"Output: {max_subarray_divide_conquer(nums3)}")  # Expected: 23
