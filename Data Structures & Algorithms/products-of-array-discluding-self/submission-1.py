class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul , right_mul = 1,1
        leftmul_res, rightmul_res = [], []
        # left part 
        for i in range(len(nums)):
            left = left_mul
            left_mul *= nums[i]
            leftmul_res.append(left)
        # right part
        for i in range(len(nums)-1,-1,-1):
            right = right_mul
            right_mul *= nums[i]
            rightmul_res.append(right)

        rightmul_res.reverse()
        for i in range(len(nums)):
            leftmul_res[i] *= rightmul_res[i]
        return leftmul_res

        