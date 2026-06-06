class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        i = 0
        if (len(s) != len(t)):
            return False
        for c in s:
            if c in seen_s.keys():
                seen_s[c] += 1
            else:
                seen_s[c] = 1
        for c in t:
            if c not in seen_s:
                return False
            else:
                seen_s[c] -= 1
        return all(val == 0 for val in seen_s.values())
            