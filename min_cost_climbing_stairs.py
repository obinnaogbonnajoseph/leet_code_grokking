class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Calculates the minimum cost to reach the top of a staircase.

        This problem is solved using dynamic programming. We can modify the input
        array in-place to store the minimum cost to reach each step. The cost
        to reach a step `i` is the cost of the step itself plus the minimum
        of the costs to reach the two preceding steps (`i-1` and `i-2`).

        The final result is the minimum of the costs to reach the last two
        steps, as we can take a final leap to the "top" from either of them.

        Args:
            cost: A list of integers where cost[i] is the cost of the ith step.

        Returns:
            The minimum cost to reach the top of the floor.
        """
        n = len(cost)

        # We can start from the third step (index 2) because the first two steps
        # (0 and 1) are our potential starting points, and their initial
        # minimum costs are just their own values.
        for i in range(2, n):
            # Update the cost of the current step to be the minimum cost to
            # reach this point. This is its own cost plus the minimum cost of
            # arriving from the previous step or the one before it.
            cost[i] += min(cost[i-1], cost[i-2])

        # The top of the floor can be reached from either the last step or the
        # second-to-last step. We return the minimum of these two values.
        return min(cost[n-1], cost[n-2])

# Example Usage:
if __name__ == '__main__':
    solver = Solution()

    # Example 1
    cost1 = [10, 15, 20]
    # To avoid modifying the original list in tests, pass a copy
    result1 = solver.minCostClimbingStairs(cost1.copy())
    print(f"Input: {cost1}")
    print(f"Minimum cost: {result1}") # Expected output: 15
    print("-" * 20)

    # Example 2
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result2 = solver.minCostClimbingStairs(cost2.copy())
    print(f"Input: {cost2}")
    print(f"Minimum cost: {result2}") # Expected output: 6
    print("-" * 20)
