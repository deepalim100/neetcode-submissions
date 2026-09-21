from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for i in nums:
            num_dict[i]= num_dict.get(i,0) + 1
        buckets= [[] for _ in range(len(nums)+1)]
        for key, val in num_dict.items():
            buckets[val].append(key)
        res = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num) 
                if len(res)==k:
                    return res