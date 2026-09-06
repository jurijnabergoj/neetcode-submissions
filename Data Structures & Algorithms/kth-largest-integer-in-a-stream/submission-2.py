class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.sn = sorted(nums)[-k:]

    def add(self, val: int) -> int:
        if not self.sn:
            self.sn.append(val)
            return val
        if val < self.sn[0]:
            return self.sn[0]
        
        i = 0
        while i < len(self.sn) and val > self.sn[i]:
            i += 1
        self.sn.insert(i, val)
        
        if len(self.sn) > self.k:
            self.sn.pop(0)

        return self.sn[0]
