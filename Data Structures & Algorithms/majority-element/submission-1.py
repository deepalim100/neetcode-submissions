from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = Counter(nums)
        val_ele = max(list(ele.values()))
        max_ele = [key for key,val in ele.items() if val == val_ele]
        return max_ele[0]

        