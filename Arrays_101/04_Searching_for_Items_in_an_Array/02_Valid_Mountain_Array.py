class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        idx_maximum = arr.index(max(arr))
        if idx_maximum == 0 or idx_maximum == len(arr)-1:
            return False
        if arr.count(max(arr)) != 1:
            return False
        
        for idx, num in enumerate(arr):
            if idx < idx_maximum:
                if arr[idx] >= arr[idx+1]:
                    return False
            
            elif idx > idx_maximum:
                if idx == len(arr)-1:
                    continue
                else:
                    if arr[idx] <= arr[idx+1]:
                        return False
            else:
                continue

                
        return True