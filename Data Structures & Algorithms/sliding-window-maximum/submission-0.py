class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        max_lst = []

        while i < len(nums) and (i+k) <= len(nums):
            max_num = max(nums[i:i+k])
            i += 1
            max_lst.append(max_num)
        return max_lst
                