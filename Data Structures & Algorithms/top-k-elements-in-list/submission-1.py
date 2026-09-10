from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = Counter(nums)
        result = []
        for _ in range(k):
            max_num = max(num_dict, key= num_dict.get)
            result.append(max_num)
            del num_dict[max_num]
        return result