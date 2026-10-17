class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        k = target
        def sum_helper(i,j,l,r,k):
            range = []
            total = 0
            while l < r:
                total = nums[i] + nums[j] + nums[l] + nums[r]
                if total == k:
                    range.append([nums[i],nums[j],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total > k:
                    r -= 1
                elif total < k:
                    l += 1
            return range
        i , l, r = 0, 0, len(nums) - 1
        res = []
        while i < len(nums) - 3:
            j = i + 1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            while j < len(nums) - 2:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                l = j+1
                r_sum = sum_helper(i,j,l,r,k)
                res.extend(r_sum)
                j += 1
            i += 1
        return res
        