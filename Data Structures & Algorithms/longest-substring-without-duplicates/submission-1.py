class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        chars = set()

        i = 0
        j = 0
        while j < len(s):
            if s[j] in chars:
                max_len = max(max_len, j - i)
                while s[i] != s[j]:
                    chars.remove(s[i])
                    i += 1
                i += 1
                j += 1
            else:
                chars.add(s[j])
                j += 1
        max_len = max(max_len, j - i)
        return max_len

