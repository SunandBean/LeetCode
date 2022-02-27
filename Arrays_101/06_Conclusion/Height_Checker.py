class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        counter_diff = 0
        
        for h1, h2 in zip(heights, sorted_heights):
            if h1 != h2:
                counter_diff += 1
        
        return counter_diff