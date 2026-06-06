from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())