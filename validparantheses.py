class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for a in s:
            if a in braces:
                stack.append(a)
            else:
                if len(stack) > 0 and braces[stack[-1]] == a:
                    stack.pop()
                else:
                    return False
        if len(stack):
            return False
        else:
            return True
