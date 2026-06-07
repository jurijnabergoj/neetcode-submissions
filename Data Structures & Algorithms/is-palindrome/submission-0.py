class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = ''.join(c for c in s if c.isalnum())
        
        i = 0
        j = len(s_alpha) - 1
        while i <= j:
            if s_alpha[i].casefold() != s_alpha[j].casefold():
                return False
            i += 1
            j -= 1
        return True