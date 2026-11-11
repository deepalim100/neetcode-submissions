class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r = 0, 1
        c_t , min_length = 0, float('inf')

        while l <= len(nums) and r <= len(nums):
            c_t = sum(nums[l:r])
            if c_t >= target:
                min_length = min(min_length, r - l)
                l += 1
            else:
                if r == len(nums):
                    break
                r += 1
        return min_length if min_length != float('inf') else 0
        