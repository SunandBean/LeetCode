class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_arr = len(arr)
        list_zero = []
        for idx, num in enumerate(arr):
            if num == 0:
                list_zero.append(idx + len(list_zero))
                
        for idx in list_zero:
            arr.insert(idx, 0)
            
        del arr[len_arr:]
        
        