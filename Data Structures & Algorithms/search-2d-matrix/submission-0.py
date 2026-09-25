class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(array):
            l, r = 0, len(array) - 1

            while l <= r:

                mid = (l+r) // 2

                if array[mid] == target:
                    return True
                elif array[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return False

        for arrays in matrix:
            if search(arrays):
                return True
            else:
                continue


        return False
