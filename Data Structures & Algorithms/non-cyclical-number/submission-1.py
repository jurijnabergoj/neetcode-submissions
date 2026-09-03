class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_of_squares(n):
            sum = 0
            while n > 0:
                d = n % 10
                sum += d ** 2
                n = n // 10
            return sum

        stack = []
        while n != 1:
            if n in stack:
                return False
        
            re = sum_of_squares(n)
            stack.append(n)
            n = re
        
        return True