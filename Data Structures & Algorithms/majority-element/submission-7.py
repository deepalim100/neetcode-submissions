from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, 0
        for i in nums:
            
            if count == 0:
                candidate = i
                count += 1
            elif candidate == i:
                count += 1
            elif candidate != i:
                count -= 1
            print(candidate, count)
        return candidate

        