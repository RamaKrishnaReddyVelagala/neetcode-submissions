class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        temp = 0

        while l < r:
            if not self.alphanumeric(s[l]):
                l += 1
            if not self.alphanumeric(s[r]):
                r -= 1

            if s[l] != s[r] and l < r:
                if s[l + 1] == s[r]:
                    l += 1
                    temp += 1
                elif s[r - 1] == s[l]:
                    r -= 1
                    temp += 1
                else:
                    return False
            else:
                l, r = l+1, r-1

        return True if temp < 2 else False
    
    def alphanumeric(self, c):
        return (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9"))
        