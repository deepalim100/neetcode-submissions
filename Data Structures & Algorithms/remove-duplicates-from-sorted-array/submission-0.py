class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r, n = 0, 1, len(nums)
        while r < n:
            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]
                r += 1
        return l+1
        