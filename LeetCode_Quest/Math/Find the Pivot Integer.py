class Solution:
    def pivotInteger(self, n: int) -> int:
        numbers = range(1, n + 1)
    
        left_idx = 0
        right_idx = len(numbers) - 1
        
        left_sum = numbers[left_idx]
        right_sum = numbers[right_idx]
        
        while left_idx < right_idx:
            if left_sum < right_sum:
                left_idx += 1
                left_sum += numbers[left_idx]
            else:
                right_idx -= 1
                right_sum += numbers[right_idx]
                
        if left_sum == right_sum:
            return numbers[left_idx]  
        
        return -1