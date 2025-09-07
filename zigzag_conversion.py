class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a string into a zigzag pattern on a given number of rows.

        Args:
            s: The input string.
            numRows: The number of rows for the zigzag pattern.

        Returns:
            The converted string, read line by line.
        """

        # Edge case: If there's only one row or the number of rows is
        # greater than or equal to the string length, the pattern is just
        # the string itself. No conversion is needed.
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings, one for each row.
        rows = [''] * numRows
        
        # Initialize the current row index and the direction of movement.
        # We start at row 0 and will move downwards.
        current_row = 0
        # The direction will be 1 for moving down and -1 for moving up.
        # We start with -1 because the direction is flipped before the first move.
        direction = -1 

        # Iterate through each character in the input string.
        for char in s:
            # Append the character to the string representing the current row.
            rows[current_row] += char

            # Check if we have reached the top or bottom row.
            # If so, we need to reverse the direction of movement.
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            
            # Move to the next row based on the current direction.
            current_row += direction

        # After placing all characters, join the strings in each row
        # to form the final converted string.
        return "".join(rows)

# Example Usage:
solver = Solution()

# Example 1:
s1 = "PAYPALISHIRING"
numRows1 = 3
output1 = solver.convert(s1, numRows1)
print(f"Input: s = \"{s1}\", numRows = {numRows1}")
print(f"Output: \"{output1}\"") # Expected: "PAHNAPLSIIGYIR"

print("-" * 20)

# Example 2:
s2 = "PAYPALISHIRING"
numRows2 = 4
output2 = solver.convert(s2, numRows2)
print(f"Input: s = \"{s2}\", numRows = {numRows2}")
print(f"Output: \"{output2}\"") # Expected: "PINALSIGYAHRPI"

print("-" * 20)

# Example 3:
s3 = "A"
numRows3 = 1
output3 = solver.convert(s3, numRows3)
print(f"Input: s = \"{s3}\", numRows = {numRows3}")
print(f"Output: \"{output3}\"") # Expected: "A"
