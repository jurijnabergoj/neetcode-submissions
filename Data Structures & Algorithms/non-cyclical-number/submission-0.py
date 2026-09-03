class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_of_squares(n):
            sum = 0
            while n > 0:
                d = n % 10
                sum += d ** 2
                n = n // 10
            return sum

        
        def isHappyHelper(n, stack):
            if n == 1:
                return True

            if n in stack:
                return False
        
            re = sum_of_squares(n)
            stack.append(n)
            return isHappyHelper(re, stack)
        
        return isHappyHelper(n, [])
