class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for n in nums:
            if n - 1 not in num_set:
                i = 1
                while n + i in num_set:
                    i += 1
                if i > max_len:
                    max_len = i
        return max_len