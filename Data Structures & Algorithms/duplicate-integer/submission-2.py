class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique_vals = set(nums)

        if len(nums) != len(unique_vals):
            return True

        return False