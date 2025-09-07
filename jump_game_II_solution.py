def jump(nums):
    """
    Calculates the minimum number of jumps to reach the end of the array.

    This function uses a greedy approach to solve the Jump Game II problem.
    It iterates through the array, keeping track of the farthest reachable
    index and the end of the current jump's range.

    Args:
        nums: A list of non-negative integers where each element represents
              the maximum jump length from that position.

    Returns:
        The minimum number of jumps required to reach the last index.
    """
    # The number of jumps made so far.
    jumps = 0
    
    # The end of the range that can be reached with the current number of jumps.
    # Initially, this is index 0.
    current_jump_end = 0
    
    # The farthest index that can be reached from any position within the current jump's range.
    farthest = 0
    
    # We iterate through the array, but stop before the last element.
    # If we reach the second-to-last element, we are guaranteed to be able
    # to jump to the last element.
    for i in range(len(nums) - 1):
        # Update the farthest reachable index. We take the maximum of the
        # current farthest and the new potential reach from the current index (i + nums[i]).
        farthest = max(farthest, i + nums[i])
        
        # If we have reached the end of the current jump's range...
        if i == current_jump_end:
            # ...it means we must make another jump to continue.
            jumps += 1
            # The new jump's range ends at the 'farthest' point we've found so far.
            current_jump_end = farthest
            
            # Optimization: If the new jump range can reach or exceed the end,
            # we can stop early and return the answer.
            if current_jump_end >= len(nums) - 1:
                return jumps

    return jumps

# Example 1
nums1 = [2, 3, 1, 1, 4]
print(f"For nums = {nums1}, Min Jumps: {jump(nums1)}")  # Output: 2

# Example 2
nums2 = [2, 3, 0, 1, 4]
print(f"For nums = {nums2}, Min Jumps: {jump(nums2)}")  # Output: 2
