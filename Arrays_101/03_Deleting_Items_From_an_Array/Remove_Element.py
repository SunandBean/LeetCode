class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                idx = nums.index(val)
                del nums[idx]
            except:
                break
            
        return len(nums)