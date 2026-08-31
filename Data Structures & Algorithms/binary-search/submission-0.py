class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while right > left:
            if nums[left] > target or nums[right] < target:
                return -1
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left if nums[left] == target else -1