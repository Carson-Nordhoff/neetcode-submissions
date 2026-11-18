class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        nums.sort()

        for i in range(len(nums)):

            if i != 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:

                sum_ = nums[l] + nums[r]

                if sum_ == -nums[i]:
                    ans.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
                
                elif sum_ > -nums[i]:
                    r -= 1

                else: 
                    l += 1

        print(ans)

        return [[a, b, c] for a, b, c in ans]
        