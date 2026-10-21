class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0 , len(heights) - 1
        area, area_res = 0 ,0
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            area_res = max(area_res,area)
        return area_res
            