"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

"""
from collections import deque


class Solution:
    def isValid(self, string: str) -> bool:
        correct_sequence = {")": "(", "}": "{", "]": "["}
        stack_sequence = deque()
        if (len(string) % 2) != 0 or len(string) == 0:
            return False
        for char in string:
            if char in correct_sequence.values():
                stack_sequence.append(char)
            elif (
                stack_sequence and correct_sequence[char] == stack_sequence[-1]
            ):
                stack_sequence.pop()
            else:
                return False
        return len(stack_sequence) == 0


new = Solution()

print(new.isValid("([}}])"))
