class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        num_zeros = 0
        for x in nums:
            if x != 0:
                prod *= x
            else:
                num_zeros += 1
        result = []
        for x in nums:
            if x != 0:
                if num_zeros > 0:
                    result.append(0)
                else:
                    result.append(int(prod / x))
            else:
                if num_zeros == 1:
                    result.append(prod)
                else:
                    result.append(0)
        return result
