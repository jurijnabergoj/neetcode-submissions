class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_index = {}
        i = 0
        j = 0
        for j, c in enumerate(s):
            if c in char_index and char_index[c] >= i:
                i = char_index[c] + 1
            char_index[c] = j
            max_len = max(max_len, j - i + 1)
        return max_len

