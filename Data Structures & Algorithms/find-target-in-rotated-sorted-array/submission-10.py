class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def min_index(array):
            l,r = 0, len(array)-1
            res, index = array[0], 0

            while l <= r :

                mid = (l+r) // 2
                
                if array[l] < array[r]:
                    if array[l] <= res:
                        index = l 
                        res = array[l]
                        break

                if array[mid] > array[r]:
                    l = mid + 1
                else:
                    if array[mid] <= res:
                        index = mid
                        res = array[mid]
                    r = mid - 1

            return index

        def binary_search(l,r):
            while l <= r:
                mid = (l+r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        mini = min_index(nums)
        bs1 = binary_search(0, mini-1)
        bs2 = binary_search(mini, len(nums) - 1)

        if bs1 == -1 and bs2 == -1:
            return -1
        elif bs1 != -1 and bs2 == -1:
            return bs1
        else:
            return bs2 
        