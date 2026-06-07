class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        i = 0
        n = len(nums)
        while i < n:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            left = i + 1
            right = n - 1
            while left < right:
                res = nums[left] + nums[right]
                if res + nums[i] == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    continue
                elif res + nums[i] > 0:
                    right -= 1
                elif res + nums[i] < 0:
                    left += 1
            i += 1
        return [list(t) for t in result]