from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        for i in nums:
            if i not in num_dict:
                num_dict[i] = 1
            else:
                num_dict[i] += 1

        for k,v in num_dict.items():
            if v > len(nums)/2:
                return k

        