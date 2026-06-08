class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_index = {}
        i = 0
        j = 0
        while j < len(s):
            if s[j] in char_index and char_index[s[j]] >= i:
                i = char_index[s[j]] + 1
            char_index[s[j]] = j
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len

