def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Finds two numbers in a list that sum up to a target value.

    Args:
        nums: A list of integers.
        target: The target integer sum.

    Returns:
        A list containing the indices of the two numbers.
    """
    seen_numbers = {}  # Dictionary to store number -> index
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen_numbers:
            # If the complement is found, return its index and the current index
            return [seen_numbers[complement], index]
        # Otherwise, add the current number and its index to the dictionary
        seen_numbers[num] = index
