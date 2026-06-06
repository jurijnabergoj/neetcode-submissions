class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        max_freq = 0

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts[n] > max_freq:
                max_freq = counts[n]

        buckets = [[] for _ in range(max_freq + 1)]
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