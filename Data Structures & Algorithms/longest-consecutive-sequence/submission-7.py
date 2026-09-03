class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)

        no_dups = set(nums)

        sequence_lengths = []

        for num in no_dups:
            
            if num-1 not in no_dups:

                count = 1
                while num+1 in no_dups:
                    count += 1
                    num += 1
                sequence_lengths.append(count)
     
        return max(sequence_lengths)