class Solution:
  def divisorGame(self, n: int) -> bool:
    """
    Determines if Alice can win the Divisor Game.

    Args:
      n: The starting number on the chalkboard.

    Returns:
      True if Alice wins, False otherwise.
    """

    # Game Theory Analysis:
    # Let's analyze the game for small values of n:
    # n = 1: Alice has no moves. She loses.
    # n = 2: Alice chooses x=1. n becomes 1. Bob has no moves. Alice wins.
    # n = 3: Alice must choose x=1. n becomes 2. Now it's Bob's turn, and we know
    #        that starting with 2 is a winning position. So, Bob wins. Alice loses.
    # n = 4: Alice can choose x=1. n becomes 3. We know starting with 3 is a
    #        losing position for the next player (Bob). So, Alice wins.

    # Pattern Observation:
    # - If n is odd: Any divisor x of n must also be odd.
    #   The next number is n - x (odd - odd), which is always even.
    #   So, if Alice starts with an odd number, she must give Bob an even number.
    # - If n is even: Alice can always choose x=1.
    #   The next number is n - 1, which is always odd.
    #   So, if Alice starts with an even number, she can always give Bob an odd number.

    # Optimal Strategy:
    # If Alice starts with an even number, she can always force Bob into a state
    # with an odd number. Bob, in turn, must always return an even number to Alice.
    # This continues until the numbers decrease. Alice, by always receiving an even number,
    # will never be stuck, while Bob will eventually be given n=1 (an odd number) and lose.
    # Therefore, Alice wins if and only if the starting number n is even.

    return n % 2 == 0
