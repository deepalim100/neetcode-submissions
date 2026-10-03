class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        candidate = 1
        while candidate in num_set:
            candidate += 1
        return candidate