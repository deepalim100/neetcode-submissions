class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left , right = 0, len(nums) - 1
        i = 0
        res = []
        nums = sorted(nums)
        # print(nums)
        def sum(i, l, r, nums):
            range = []
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # print(nums[i],nums[l],nums[r], total)
                if total == 0:
                    range.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
            return range
        while i < len(nums)-2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            left = i + 1
            r = sum(i, left, right, nums)
            if r is not None:
                res.extend(r)
            i += 1
        return res

