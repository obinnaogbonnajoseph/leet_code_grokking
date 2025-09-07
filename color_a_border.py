class Solution:
  def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
    """
    Finds the connected component of a starting cell, identifies its border, 
    and colors it using only built-in data structures.

    Args:
      grid: The m x n integer matrix representing the grid colors.
      row: The row of the starting square.
      col: The column of the starting square.
      color: The new color for the border.

    Returns:
      The modified grid with the border colored.
    """
    m, n = len(grid), len(grid[0])
    original_color = grid[row][col]

    # If the new color is the same as the original, no changes are needed.
    if original_color == color:
      return grid

    # We use a standard list as a queue for BFS.
    queue = [(row, col)] 
    visited = {(row, col)}
    border_cells = []

    # Start BFS to find the component and identify the border
    while queue:
      # Dequeue by popping from the front of the list.
      r, c = queue.pop(0) 
      is_on_border = False

      # Check 4-directional neighbors
      for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc

        # A cell is on the border if a neighbor is out of bounds 
        # or has a different color.
        if not (0 <= nr < m and 0 <= nc < n and grid[nr][nc] == original_color):
          is_on_border = True
        # If the neighbor is part of the component but not visited, add it to the queue.
        elif (nr, nc) not in visited:
          visited.add((nr, nc))
          # Enqueue by appending to the end of the list.
          queue.append((nr, nc))
      
      if is_on_border:
        border_cells.append((r, c))

    # After traversal, color the identified border cells
    for r, c in border_cells:
      grid[r][c] = color
      
    return grid
