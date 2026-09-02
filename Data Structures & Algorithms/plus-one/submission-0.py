class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        increment = True

        for i in range(len(digits) - 1, -1, -1):
            if increment:
                if digits[i] == 9:
                    digits[i] = 0
                    increment = True
                else:
                    digits[i] += 1
                    increment = False
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
