class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        if not arr:
            return []
            
        unique_sorted = sorted(set(arr))
        
        rank_map = {}
        for rank, val in enumerate(unique_sorted, 1):
            rank_map[val] = rank
            
        return [rank_map[num] for num in arr]