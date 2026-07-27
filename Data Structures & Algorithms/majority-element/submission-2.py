from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = Counter(nums)
        return ele.most_common(1)[0][0]

        