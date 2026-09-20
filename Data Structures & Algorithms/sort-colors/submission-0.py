class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        col_dict, j= {}, 0
        for i in nums:
            col_dict[i] = col_dict.get(i,0) + 1
        for k in [0,1,2]:
            v = col_dict.get(k,0)
            while v:
                nums[j] = k
                v -= 1
                j += 1
        return nums
    