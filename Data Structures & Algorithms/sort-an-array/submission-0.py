class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        # recursion
        left = self.sortArray(left)
        right = self.sortArray(right)
        #merging
        n , m = 0,0
        res = []
        while n < len(left) and m < len(right):
            if left[n] < right[m]:
                res.append(left[n])
                n += 1
            else:
                res.append(right[m])
                m += 1

        while n < len(left):
            res.append(left[n])
            n += 1
        while m < len(right):
            res.append(right[m])
            m += 1

        return res
        