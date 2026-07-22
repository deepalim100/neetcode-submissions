class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        longest_streak = 0

        for num in new_set:
            current_streak = 1
            if num - 1 not in new_set:
                current_num = num
                while current_num + 1 in new_set:
                    current_num += 1
                    current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak
        