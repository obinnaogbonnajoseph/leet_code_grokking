def generate(numRows):
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly
    above it.

    Args:
      numRows: An integer representing the number of rows to generate.

    Returns:
      A list of lists of integers representing Pascal's triangle.
    """
    if numRows <= 0:
        return []

    triangle = [[1]]

    for i in range(1, numRows):
        # Get the previous row to calculate the new one
        prev_row = triangle[-1]
        
        # Start the new row with 1
        new_row = [1]

        # Calculate the middle elements of the new row
        # Each element is the sum of the two elements directly above it
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j+1])
        
        # End the new row with 1
        new_row.append(1)
        
        # Add the newly generated row to the triangle
        triangle.append(new_row)
        
    return triangle

# Example Usage:
numRows1 = 5
print(f"Input: numRows = {numRows1}")
print(f"Output: {generate(numRows1)}")
# Expected Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

print("-" * 20)

numRows2 = 1
print(f"Input: numRows = {numRows2}")


print(f"Output: {generate(numRows2)}")
# Expected Output: [[1]]

numRows3 = 2
print(f"Input: numRows = {numRows3}")
print(f"Output: {generate(numRows3)}")
