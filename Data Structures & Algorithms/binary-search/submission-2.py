class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target <= nums[mid]:
                right = mid
        return left if (left < len(nums) and nums[left] == target) else -1
        