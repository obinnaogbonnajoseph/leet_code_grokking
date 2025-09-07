class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb a staircase of n steps,
        where you can climb either 1 or 2 steps at a time.

        This problem is a classic example of the Fibonacci sequence.
        The number of ways to reach step 'n' is the sum of the ways to reach
        step 'n-1' and the ways to reach step 'n-2'.

        Args:
            n: The total number of stairs.

        Returns:
            The total number of distinct ways to climb to the top.
        """
        # Base cases:
        # If there is 1 step, there is only 1 way.
        # If there are 2 steps, there are 2 ways (1+1 or 2).
        if n <= 2:
            return n

        # We only need to keep track of the last two values to calculate the next one.
        # 'one_step_before' stores the ways to reach the (i-1)th step.
        # 'two_steps_before' stores the ways to reach the (i-2)th step.
        two_steps_before = 1
        one_step_before = 2

        # Iterate from the 3rd step up to the nth step.
        for _ in range(3, n + 1):
            # The number of ways to reach the current step is the sum of the previous two.
            current_ways = one_step_before + two_steps_before
            
            # Update the pointers for the next iteration.
            two_steps_before = one_step_before
            one_step_before = current_ways

        return one_step_before

# Example Usage (for testing)
if __name__ == '__main__':
    solver = Solution()

    # Example 1
    n1 = 2
    print(f"Input: n = {n1}")
    print(f"Output: {solver.climbStairs(n1)}") # Expected: 2

    print("-" * 20)

    # Example 2
    n2 = 3
    print(f"Input: n = {n2}")
    print(f"Output: {solver.climbStairs(n2)}") # Expected: 3
    
    print("-" * 20)

    # Constraint check
    n3 = 45
    print(f"Input: n = {n3}")
    print(f"Output: {solver.climbStairs(n3)}") # Expected: 1836311903
