class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        count_max = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
                
            if count >= count_max:
                count_max = count
        return count_max
        