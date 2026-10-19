class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums = sorted(people)
        l , r = 0, len(nums) - 1
        total, k = 0, 0
        while l <= r:
            if l == r:
                k += 1
                break
            total = nums[l] + nums[r]
            if total <= limit:
                k += 1
                l += 1
                r -= 1
            elif total > limit:
                k += 1
                r -= 1
        return k

        