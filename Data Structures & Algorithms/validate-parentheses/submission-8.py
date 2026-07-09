class Solution:
    def isValid(self, s: str) -> bool:
        bMap = { 
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for c in s:
            if c in set(bMap.keys()):
                stack.append(c)
            elif stack and bMap[stack[-1]]==c:
                stack.pop()
            else:
                return False
        return True if not stack else False

