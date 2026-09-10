from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in num_dict.items():
            bucket[val].append(key)
        result = []
        for i in range(len(bucket)-1,-1,-1):
            if bucket[i]:
                for j in bucket[i]:
                    result.append(j)
                    if len(result) == k:
                        return result 