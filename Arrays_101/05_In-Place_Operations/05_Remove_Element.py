# Same with 03_Deleting_Items_From_an_Array/Remove_Element.py

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                idx = nums.index(val)
                del nums[idx]
            except:
                break
            
        return len(nums)