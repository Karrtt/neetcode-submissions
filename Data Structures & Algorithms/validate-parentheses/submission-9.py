class Solution:
    def isValid(self, s: str) -> bool:
        bMap = { 
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for c in s:
            if c in bMap:  # opening bracket
                stack.append(c)
            else:  # closing bracket
                if not stack or bMap[stack[-1]] != c:
                    return False
                stack.pop()

        return not stack

