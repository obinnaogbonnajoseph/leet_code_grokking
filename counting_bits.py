def countBits_nlogn(n: int) -> list[int]:
    """
    Calculates the number of 1's in the binary representation of each number
    from 0 to n.

    This solution has a time complexity of O(n log n) because for each number 'i'
    up to 'n', we perform a series of bitwise operations that take log(i) time.

    Args:
      n: The upper bound of the range of numbers (inclusive).

    Returns:
      A list of integers where the element at index i is the count of 1's
      in the binary representation of i.
    """
    ans = []
    for i in range(n + 1):
        count = 0
        num = i
        # Keep checking the last bit and right-shifting until the number is 0
        while num > 0:
            # Add 1 to count if the last bit is 1
            count += num & 1
            # Right shift the number to check the next bit
            num >>= 1
        ans.append(count)
    return ans

# Example Usage:
n1 = 2
print(f"Input: n = {n1}")
print(f"Output: {countBits_nlogn(n1)}") # Expected: [0, 1, 1]

print("-" * 20)

n2 = 5
print(f"Input: n = {n2}")
print(f"Output: {countBits_nlogn(n2)}") # Expected: [0, 1, 1, 2, 1, 2]
