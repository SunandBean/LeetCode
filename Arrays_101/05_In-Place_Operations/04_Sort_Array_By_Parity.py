class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        list_odd = []
        
        for idx, num in enumerate(nums):
            if num % 2 != 0:
                list_odd.append(idx)
        
        for idx, num in enumerate(list_odd):
            odd = nums.pop(num - idx)
            nums.append(odd)
                
        return nums