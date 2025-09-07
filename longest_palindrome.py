def longestPalindrome(s: str) -> str:
    """
    Finds the longest palindromic substring in s using the expand-around-center method.
    """
    if not s or len(s) < 1:
        return ""

    start = 0
    end = 0

    for i in range(len(s)):
        # Case 1: Odd length palindrome (center is s[i])
        # Example: "racecar"
        len1 = expand_around_center(s, i, i)
        
        # Case 2: Even length palindrome (center is between s[i] and s[i+1])
        # Example: "aabbaa"
        len2 = expand_around_center(s, i, i + 1)
        
        # Get the maximum length from the two cases
        max_len = max(len1, len2)
        
        # If we found a new longer palindrome, update its boundaries
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end + 1]

def expand_around_center(s: str, left: int, right: int) -> int:
    """
    Helper function to expand from a center and find the length of the palindrome.
    """
    L, R = left, right
    # Expand as long as the pointers are in bounds and characters match
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    # Return the length of the palindrome found
    return R - L - 1

# Example Usage:
print(longestPalindrome("babad"))  # Output: "bab"
print(longestPalindrome("cbbd"))   # Output: "bb"
