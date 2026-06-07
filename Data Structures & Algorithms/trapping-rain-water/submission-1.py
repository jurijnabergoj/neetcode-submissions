class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])                
            
        for j in range(n - 2, -1, -1):
            max_right[j] = max(max_right[j + 1], height[j + 1])
        
        max_area = 0
        for i in range(len(height)):
            area = min(max_left[i], max_right[i]) - height[i]
            if area > 0:
                max_area += area 
        return max_area

        