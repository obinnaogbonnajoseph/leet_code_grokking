def isValid(s: str) -> bool:
    """
    Determines if the input string containing just '(', ')', '{', '}', '[' and ']' is valid.

    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

    Args:
      s: The input string consisting of parentheses.

    Returns:
      True if the string is valid, False otherwise.
    """
    # The stack will be used to store the opening brackets.
    stack = []

    # This dictionary maps closing brackets to their corresponding opening brackets.
    # This makes it easy to check for a match.
    bracket_map = {")": "(", "}": "{", "]": "["}

    # Iterate through each character in the input string.
    for char in s:
        # If the character is a closing bracket...
        if char in bracket_map:
            # ...we check if the stack is empty. If it is, there's no matching
            # opening bracket, so we return False.
            # Otherwise, we pop the top element from the stack. If it doesn't
            # match the corresponding opening bracket for the current closing
            # bracket, the string is invalid.
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, we push it onto the stack.
            stack.append(char)

    # After iterating through the whole string, if the stack is empty,
    # it means every opening bracket was correctly closed.
    # If the stack is not empty, it means there are unclosed opening brackets.
    return not stack

# --- Example Usage ---
s1 = "()"
print(f"Input: s = \"{s1}\"")
print(f"Output: {isValid(s1)}") # Expected: True

print("-" * 20)

s2 = "()[]{}"
print(f"Input: s = \"{s2}\"")
print(f"Output: {isValid(s2)}") # Expected: True

print("-" * 20)

s3 = "(]"
print(f"Input: s = \"{s3}\"")
print(f"Output: {isValid(s3)}") # Expected: False

print("-" * 20)

s4 = "([)]"
print(f"Input: s = \"{s4}\"")
print(f"Output: {isValid(s4)}") # Expected: False

print("-" * 20)

s5 = "{[]}"
print(f"Input: s = \"{s5}\"")
print(f"Output: {isValid(s5)}") # Expected: True
