class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c_dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in c_dict:
                return [c_dict[comp], i]
            c_dict[nums[i]] = i
           
            