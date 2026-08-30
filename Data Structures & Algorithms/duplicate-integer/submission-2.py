class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for n in nums:
            if n in num_dict.keys():
                return True
            else:
                num_dict[n] = 1
        return False