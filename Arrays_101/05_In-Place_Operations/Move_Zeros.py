class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        checker_all_number = 0
        checker_non_zero = 0
        length_nums = len(nums)
        
        while checker_all_number < length_nums:
            if nums[checker_all_number]:
                nums[checker_non_zero], nums[checker_all_number] = nums[checker_all_number], nums[checker_non_zero]
                checker_non_zero += 1
            checker_all_number += 1