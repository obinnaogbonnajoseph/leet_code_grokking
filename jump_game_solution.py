class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Determines if it's possible to jump from the start to the end of the array.

        This function uses a greedy approach. It iterates through the array,
        keeping track of the farthest index that can be reached at any point.

        Args:
            nums: A list of non-negative integers where each element represents
                  the maximum jump length from that position.

        Returns:
            True if the last index can be reached, False otherwise.
        """
        # This variable will store the farthest index we can reach.
        max_reach = 0
        n = len(nums)

        # We iterate through the array with both the index and the value.
        for i, jump_length in enumerate(nums):
            # If the current index `i` is greater than the farthest index we
            # could possibly have reached so far, it means this part of the
            # array is unreachable.
            if i > max_reach:
                return False

            # We update our farthest reachable index by checking if the jump
            # from the current position `i` gives us a new maximum.
            max_reach = max(max_reach, i + jump_length)

            # If our farthest reachable index is at or beyond the last index,
            # we know it's possible to finish, so we can return True early.
            if max_reach >= n - 1:
                return True
        
        # Under the problem's constraints (1 <= nums.length), this line
        # is technically unreachable because one of the return statements
        # inside the loop will always be executed.
        return False
