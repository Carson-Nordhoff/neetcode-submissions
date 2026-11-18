from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = defaultdict(int)
        max_len = 0

        left = 0
        n = len(s)

        for i in range(n):
            counts[s[i]] += 1

            #the sum of the counts
            #not including the highest current count
            #must be less then or equal to k
            while sum(counts.values()) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, i-left+1)

        return max_len



        
        