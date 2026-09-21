from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1
        num_dict = dict(sorted(num_dict.items(),key=lambda x:x[1], reverse=True))
        # print(num_dict)
        res = []
        for key, val in num_dict.items():
            if k > 0:
                res.append(key)
                k -= 1
        return res