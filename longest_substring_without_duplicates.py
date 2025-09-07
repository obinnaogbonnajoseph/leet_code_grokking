def lengthOfLongestSubstring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
      s: The input string.

    Returns:
      The length of the longest substring.
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If the character is already in the window,
        # shrink the window from the left until it's gone.
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the new character to the window.
        char_set.add(s[right])
        
        # Update the maximum length found so far.
        max_length = max(max_length, right - left + 1)
        
    return max_length

# Example Usage:
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3
