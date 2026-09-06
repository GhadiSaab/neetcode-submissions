class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = 0
        left = len(numbers) - 1
        while right < left:
            s = numbers[right] + numbers[left]
            if s < target:
                right += 1
            elif s > target:
                left -= 1
            else:
                return [right + 1, left + 1]

        
        
        