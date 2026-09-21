class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
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

        