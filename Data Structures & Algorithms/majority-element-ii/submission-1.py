class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_dict, n = {}, len(nums)
        for i in nums:
            num_dict[i] = num_dict.get(i,0) + 1
        buckets = [[] for _ in range(len(nums)+1)]
        for k, v in num_dict.items():
            if v > n/3:
                buckets[v].append(k)
        res = []
        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                res.append(j)
        return res
        