class Solution:
    def isValid(self, s: str) -> bool:
        chars = {")": "(", "}": "{", "]": "["}

        stack = []
        for c in s:
            if c in chars:
                if stack:
                    temp = stack.pop()
                    if chars[c] != temp:
                        return False
                else: #closing but empty stack
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True