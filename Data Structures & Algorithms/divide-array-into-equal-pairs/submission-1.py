class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_dict = {}
        for i in nums:
            num_dict[i] = num_dict.get(i,0) + 1
        n = len(nums) // 2
        res = []
        for k,v in num_dict.items():
            if v%2 != 0:
                return False
        return True
        