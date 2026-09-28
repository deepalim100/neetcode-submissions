class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set= set(nums)
        total = 0
        for num in nums:
            current = num
            max_len = 1
            if num -1 not in num_set:
                while current + 1 in num_set:
                    max_len += 1
                    current += 1
            total = max(max_len, total)
        return total


        