class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        multiple_zeros = False
        one_zero = False

        ans = [0]*len(nums)
        tot = 1

        for num in nums:
            if num == 0 and one_zero:
                return [0]*len(nums)

            if num == 0:
                one_zero = True
                continue

            tot = tot * num

        for i, num in enumerate(nums):
            if num == 0:
                ans[i] = tot
                continue
            if one_zero:
                ans[i] = 0
            else:
                ans[i] = tot // num

        return ans