class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_list = []
        for idx, num in enumerate(nums):
            square_list.append(num**2)
        return sorted(square_list)
        