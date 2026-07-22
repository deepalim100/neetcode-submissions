class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans, n , j= [0 for i in range(2*len(nums))], len(nums), 0
        for i in range(2*n):
            # print(f'value of ans : {ans}, and i : {i}, n : {n}')
            if i < n:
                ans[i] = nums[i]
            elif i >= n and j < n:
                ans[i] = nums[j]
                j += 1
        return ans
        