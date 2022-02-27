class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums_set = set(nums)
        nums_list = sorted(list(nums_set))
        if len(nums_list) < 3:
            return max(nums_list)
        
        return nums_list[-3]
        