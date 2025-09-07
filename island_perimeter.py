def islandPerimeter(grid: list[list[int]]) -> int:
    """
    Calculates the perimeter of a single island in a grid.

    Args:
      grid: A 2D list of integers where 1 is land and 0 is water.

    Returns:
      The integer perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell initially adds 4 to the perimeter
                perimeter += 4
                
                # Check for land cell above and subtract 2 for the shared edge
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                
                # Check for land cell to the left and subtract 2 for the shared edge
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2
                    
    return perimeter

# Example 1
grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(f"Example 1 Output: {islandPerimeter(grid1)}") # Output: 16

# Example 2
grid2 = [[1]]
print(f"Example 2 Output: {islandPerimeter(grid2)}") # Output: 4

# Example 3
grid3 = [[1,0]]
print(f"Example 3 Output: {islandPerimeter(grid3)}") # Output: 4
