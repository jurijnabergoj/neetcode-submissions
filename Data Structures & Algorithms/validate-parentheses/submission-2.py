class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if bracket_dict[c] != last:
                    return False
        return len(stack) == 0
                