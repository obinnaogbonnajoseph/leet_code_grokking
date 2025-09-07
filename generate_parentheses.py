from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all combinations of well-formed parentheses given n pairs.

        This function uses a backtracking algorithm to build the parenthesis strings.
        At each step, it tries to add either an opening or a closing parenthesis,
        respecting the rules of well-formedness:
        1. The number of opening parentheses cannot exceed n.
        2. A closing parenthesis can only be added if it is preceded by an
           unmatched opening parenthesis.

        Args:
            n: The number of pairs of parentheses.

        Returns:
            A list of strings containing all valid combinations.
        """
        # List to store the resulting combinations
        result = []
        
        # The backtracking function
        # current_string: The string being built so far
        # open_count: The number of opening parentheses used
        # close_count: The number of closing parentheses used
        def backtrack(current_string: str, open_count: int, close_count: int):
            # Base case: if the string has reached the maximum length (2 * n),
            # it's a complete and valid combination.
            if len(current_string) == 2 * n:
                result.append(current_string)
                return

            # --- Recursive Step ---

            # 1. Add an opening parenthesis if we haven't used all `n` of them.
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)

            # 2. Add a closing parenthesis if the number of closing parentheses
            # is less than the number of opening ones. This ensures that
            # we never have an invalid prefix like ")(".
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)

        # Start the backtracking process with an empty string and zero counts.
        backtrack("", 0, 0)
        return result

# Example Usage:
solver = Solution()

# Example 1: n = 3
n1 = 3
output1 = solver.generateParenthesis(n1)
print(f"Input: n = {n1}")
print(f"Output: {output1}")
# Expected: ["((()))","(()())","(())()","()(())","()()()"]

print("-" * 20)

# Example 2: n = 1
n2 = 1
output2 = solver.generateParenthesis(n2)
print(f"Input: n = {n2}")
print(f"Output: {output2}")
# Expected: ["()"]
