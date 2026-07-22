class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        result = []
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_count += 1

        result = [0]*n
        if zero_count > 1:
            return result
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = product
            else:
                if zero_count == 0:
                    num = int(product / nums[i])
                    result[i] = num
                else:
                    result[i] = 0
        return result
        
        