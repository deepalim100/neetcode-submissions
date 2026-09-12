from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = Counter(nums)
        return max(ele, key=ele.get)

        