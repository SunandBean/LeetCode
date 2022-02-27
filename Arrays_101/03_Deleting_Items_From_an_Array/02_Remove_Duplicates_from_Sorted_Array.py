class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            while nums.count(num) != 1:
                nums.pop(nums.index(num))
        
        return len(nums)