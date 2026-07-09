class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if i in set("[{("):
                a.append(i)
            else:
                if not a:
                    return False
                if a[-1]=='{' and i=='}':
                    a.pop()
                elif a[-1]=='(' and i==')':
                    a.pop()
                elif a[-1]=='[' and i==']':
                    a.pop()
                else:
                    return False
        if not a:
            return True
        return False
        