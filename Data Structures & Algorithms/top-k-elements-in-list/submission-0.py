class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_set = {}
        for i in nums:
            if i not in new_set:
                new_set[i] = 1
            else:
                new_set[i] += 1

        sorted_items = sorted(new_set.items(),key = lambda item : item[1], reverse=True)
        result = [item[0] for item in sorted_items[:k]]
        return result
        