class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""

        for c in s:
            if c.isalnum():
                newstr += c
        
        return newstr.lower() == newstr[::-1].lower()