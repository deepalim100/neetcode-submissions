class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r = 0, 0
        c_t , min_length = 0, float('inf')

        while r < len(nums):
            c_t += nums[r]
            while c_t >= target:
                min_length = min(min_length, r - l + 1)
                c_t -= nums[l]
                l += 1
                
            
            r += 1
        return min_length if min_length != float('inf') else 0
        