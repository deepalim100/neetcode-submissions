class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r=0, n-1
        res = 0
        while l < r:
            res = numbers[l] + numbers[r]
            if res < target:
                l += 1
            elif res > target:
                r -= 1
            elif res == target and l < r:
                return [l+1,r+1] 
        