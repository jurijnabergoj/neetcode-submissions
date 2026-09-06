class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stone = max(stones)
        buckets = [0] * (max_stone + 1)

        for stone in stones:
            buckets[stone] += 1
        
        first = second = max_stone
        while first > 0:
            if buckets[first] % 2 == 0:
                buckets[first] = 0
                
                while first > 0 and buckets[first] == 0:
                    first -= 1
                continue
            
            else:
                buckets[first] = 1
                second = first - 1
                while second > 0 and buckets[second] == 0:
                    second -= 1
                
                if second == 0: return first

                buckets[first] = 0
                buckets[second] -= 1
                diff = first - second
                buckets[diff] += 1

                while first > 0 and buckets[first] == 0:
                    first -= 1
        return first