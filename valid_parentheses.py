"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true"""

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
                print('stack1:', stack)
            else:
                if not stack or bracket != pairs[stack.pop()]:
                    print('stack2:', stack)
                    return False
        
        return not stack




