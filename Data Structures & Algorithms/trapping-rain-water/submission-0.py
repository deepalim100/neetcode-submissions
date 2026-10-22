class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max , water_res = 0,0,0
        l, r = 0, len(height) - 1
        while l < r:
            water = 0
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if height[l] < height[r]:
                water = left_max - height[l]
                l += 1
            else:
                water = right_max - height[r]
                r -= 1
            water_res += water
        return water_res