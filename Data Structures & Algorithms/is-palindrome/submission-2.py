class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = ''.join(c.lower() for c in s if c.isalnum())
        
        return s_alpha == s_alpha[::-1]