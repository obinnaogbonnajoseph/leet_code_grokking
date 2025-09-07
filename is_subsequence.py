def isSubsequence(s: str, t: str) -> bool:
    """
    Original function to check if string s is a subsequence of string t.
    This is efficient for single checks.
    """
    s_pointer = 0
    t_pointer = 0

    # Iterate through both strings
    while s_pointer < len(s) and t_pointer < len(t):
        # If characters match, move the pointer for s
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        # Always move the pointer for t
        t_pointer += 1

    # If s_pointer reached the end of s, all its characters were found in order
    return s_pointer == len(s)


class SubsequenceChecker:
    """
    An optimized class for the follow-up problem where we check many strings 's'
    against a single, long string 't'. This version has no external imports.
    """

    def __init__(self, t: str):
        """
        Preprocesses the string t to allow for fast subsequence checks.
        Time complexity: O(len(t))
        """
        # Replace collections.defaultdict with a standard dictionary
        self.char_indices = {}
        for index, char in enumerate(t):
            if char not in self.char_indices:
                self.char_indices[char] = []
            self.char_indices[char].append(index)

    def _binary_search(self, arr: list, target: int) -> int:
        """
        Custom binary search to find the index of the first element in the sorted
        list `arr` that is strictly greater than `target`.
        This is equivalent to the behavior of `bisect.bisect_right`.
        """
        low, high = 0, len(arr) - 1
        # This will be the insertion point if no element is > target
        ans = len(arr)

        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] > target:
                # This is a potential answer. Store it and look for an even
                # smaller index in the left half of the array.
                ans = mid
                high = mid - 1
            else:
                # The element at mid is not greater than the target, so we must
                # search for a valid index in the right half.
                low = mid + 1
        return ans

    def isSubsequence(self, s: str) -> bool:
        """
        Checks if string s is a subsequence of the preprocessed string t.
        Time complexity: O(len(s) * log(len(t)))
        """
        current_match_index = -1
        for char in s:
            # If the character doesn't exist in t, it can't be a subsequence.
            if char not in self.char_indices:
                return False

            indices_list = self.char_indices[char]

            # Use our custom binary search instead of bisect.bisect_right
            insertion_point = self._binary_search(indices_list, current_match_index)

            # If the insertion point is at the end of the list, it means
            # there are no more occurrences of this character that appear after
            # the previous character in s.
            if insertion_point == len(indices_list):
                return False

            # Update the last found index to the new one.
            current_match_index = indices_list[insertion_point]

        return True


# --- How to use the optimized version for the follow-up scenario ---

# 1. Suppose this is our large string 't' that we'll be checking against.
#    We create and preprocess the checker object only ONCE.
t_main = "ahbgdc"
checker = SubsequenceChecker(t_main)

# 2. Now, we can check many incoming 's' strings very efficiently.
s_many = ["abc", "axc", "ahc", "abg", "ad", "ac", ""]

print(f"--- Optimized Check against t = '{t_main}' ---")
for s_query in s_many:
    print(f"Is '{s_query}' a subsequence? {checker.isSubsequence(s_query)}")

# --- Original function calls for comparison ---
print("\n--- Original Function Check ---")
print(f"Is 'abc' a subsequence of '{t_main}'? {isSubsequence('abc', t_main)}")
print(f"Is 'axc' a subsequence of '{t_main}'? {isSubsequence('axc', t_main)}")

