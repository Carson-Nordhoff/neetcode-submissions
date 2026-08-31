class Solution:
    def isValid(self, s: str) -> bool:
        
        valids = '[](){}'
        
        matches = {
            ')': '(',
            '}': '{',
            ']': '['
            }

        stack = []

        for c in s:

            if c not in valids:
                return False

            if not stack or c not in matches or matches[c] != stack[-1]:
                stack.append(c)
                continue

            else:
                stack.pop()

        if stack:
            return False

        else:
            return True