import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Calculates the number of unique paths a robot can take on an m x n grid.

        The robot starts at (0, 0) and wants to reach (m-1, n-1).
        It can only move down or right.

        This problem can be solved using dynamic programming or combinatorics.

        Method: Dynamic Programming (DP)
        Let dp[j] be the number of ways to reach the j-th cell in the current row.
        To reach cell (i, j), the robot can come from (i-1, j) or (i, j-1).
        The number of ways to reach (i, j) is the sum of the ways to reach the
        cell above and the cell to the left.
        
        The recurrence relation is: dp[i][j] = dp[i-1][j] + dp[i][j-1].

        To optimize space, we only need to store the previous row's DP values
        to calculate the current row. We can use a single 1D array for this.
        The number of ways to reach any cell in the first row is 1 (by only moving right).
        So, we initialize a dp array of size n with all 1s.

        Then, we iterate through the grid row by row (from the second row),
        and for each cell, we update the number of paths. The new value for
        dp[j] will be the sum of the value from the left (dp[j-1]) and the value
        from above (the old dp[j] from the previous row's calculation).
        
        Args:
            m: The number of rows in the grid.
            n: The number of columns in the grid.

        Returns:
            The number of possible unique paths.
        """
        
        # We will use the space-optimized dynamic programming approach.
        # Initialize a 1D array representing a row.
        # The number of ways to reach any cell in the first row is 1.
        dp = [1] * n

        # Iterate through the rest of the rows
        for i in range(1, m):
            # Iterate through the columns, starting from the second column
            for j in range(1, n):
                # The number of ways to get to the current cell is the sum of
                # ways to get to the cell above (dp[j]) and the cell to the left (dp[j-1]).
                dp[j] = dp[j] + dp[j-1]
        
        # The result is the number of ways to reach the bottom-right corner.
        return dp[n-1]


# Example Usage:
solver = Solution()

# Example 1: m = 3, n = 7
print(f"For m = 3, n = 7, Unique Paths: {solver.uniquePaths(3, 7)}") # Expected: 28

# Example 2: m = 3, n = 2
print(f"For m = 3, n = 2, Unique Paths: {solver.uniquePaths(3, 2)}") # Expected: 3

