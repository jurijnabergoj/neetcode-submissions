class Solution:
    def trap(self, height: List[int]) -> int:
        greater_left = {}
        greater_right = {}
        
        max_left = 0
        max_right = 0
        i = 0
        j = len(height) - 1
        while i <= len(height) and j >= 0:
            if i == 0 and j == len(height) - 1:
                i += 1
                j -= 1
                continue
            if height[i - 1] > max_left:
                max_left = height[i - 1]
            
            if height[j + 1] > max_right:
                max_right = height[j + 1]
            
            greater_left[i] = max_left
            greater_right[j] = max_right
            
            i += 1
            j -= 1
        
        max_area = 0
        for i in range(len(height)):
            left = greater_left[i] if i in greater_left else 0
            right = greater_right[i] if i in greater_right else 0
            if left != 0 and right != 0:
                area = min(left, right) - height[i]
                if area > 0:
                    max_area += area 
        return max_area

        