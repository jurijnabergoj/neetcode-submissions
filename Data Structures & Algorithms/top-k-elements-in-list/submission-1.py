from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        result = []
        for l in range(len(buckets) - 1, -1, -1):
            for x in buckets[l]:
                if len(result) < k:
                    result.append(x)
                else:
                    return result
        return result