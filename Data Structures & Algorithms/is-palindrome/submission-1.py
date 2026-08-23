import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','', s)
        s = s.lower()
        if s.isalnum() != True:
            s = s[:len(s) - 1]
        # print(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
                break
            l += 1
            r -= 1
        
        return True

        