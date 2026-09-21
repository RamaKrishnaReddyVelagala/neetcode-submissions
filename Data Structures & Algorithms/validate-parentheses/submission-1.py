class Solution:
    def isValid(self, s: str) -> bool:
        char_dic = {
            '(': ')', '{': '}', '[' : ']'
        }
        if len(s) %  2 == 1:
            return False

        stack = []
        for char in s:
            if char in char_dic:
                stack.append(char)
            else:
                if not stack or char_dic[stack.pop()] != char:
                    return False
            
        return True