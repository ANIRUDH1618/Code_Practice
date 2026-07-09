class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        area_max = 0

        while i != j:
            lenght = min(height[i], height[j])
            width = j - i

            if height[i] > height[j]:
                area = lenght * width
                if area > area_max:
                    area_max = area
                j -= 1
            
            else:
                area = lenght * width
                if area > area_max:
                    area_max = area
                i += 1
            
        return area_max

def min(a,b):
    if a > b:
        return b
    return a