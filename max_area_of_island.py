from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Calculates the maximum area of an island in a binary grid using DFS.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            """
            Performs a Depth-First Search to find the area of an island
            and sinks it by changing 1s to 0s to mark as visited.
            """
            # Check for out-of-bounds or if the cell is water (0)
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            # Mark the current cell as visited by "sinking" it
            grid[r][c] = 0

            # The area includes the current cell (1) plus the area of its
            # 4-directionally connected neighbors.
            area = 1
            # down, up, right, left
            directions = [(1,0), (-1,0), (0, 1), (0, -1)]
            for direction in directions:
              dr, dc = direction
              nr, nc = r+dr, c+dc
              area += dfs(nr, nc)
            
            return area

        # Iterate through each cell in the grid to find islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # If a land cell is found, calculate the area of the island
                    # it belongs to and update the max_area.
                    current_island_area = dfs(r, c)
                    max_area = max(max_area, current_island_area)
        
        return max_area
