class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complements = {}

        for index, number in enumerate(nums):

            complement = target - nums[index]

            if nums[index] in complements:
                return [complements[nums[index]], index]

            complements[complement] = index

        return 0