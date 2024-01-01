def isValid(self, s: str) -> bool:
    stack = []
    matches = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in "({[":
            stack.append(c)
        elif len(stack) == 0 or stack[-1] != matches[c]:
            return False
        else:
            stack.pop()

    if len(stack) > 0:
        return False
    return True
