class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        nums_range = list(range(1, length+1, 1))
        nums.sort()
        
        idx_sorted = 0
        idx_range = 0
        
        list_disappear = []
        
        while idx_sorted < length and idx_range < length:
            num_sorted = nums[idx_sorted]
            num_range = nums_range[idx_range]
            
            if num_range < num_sorted :
                idx_range += 1
                list_disappear.append(num_range)
            elif num_range > num_sorted :
                idx_sorted += 1
                if idx_sorted == length:
                    for num_remained in nums_range[idx_range:]:
                        list_disappear.append(num_remained)
            else:
                idx_sorted += 1
                idx_range += 1
                if idx_sorted == length and idx_range != length:
                    for num_remained in nums_range[idx_range:]:
                        list_disappear.append(num_remained)
                
        return list_disappear