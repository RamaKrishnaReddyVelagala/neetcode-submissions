class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s.startswith(')') or s.startswith(']') or s.startswith('}'):
            return False

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else: stack.append(i)
            elif i == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else: stack.append(i)
            elif i == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else: stack.append(i)
        
        if len(stack) == 0:
            return True
        else: return False

        