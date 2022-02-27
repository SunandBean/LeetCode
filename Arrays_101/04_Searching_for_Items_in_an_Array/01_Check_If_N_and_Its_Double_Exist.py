class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for idx, num in enumerate(arr):
            try:
                if arr.index(2 * num) != idx :
                    return True
            except:
                continue
                
        return False