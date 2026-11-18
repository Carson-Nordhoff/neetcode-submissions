class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        left = 0

        max_len = 0
        substr = set()

        for i in range(n):

            while s[i] in substr:
                substr.remove(s[left])
                left += 1

            max_len = max(max_len, i-left+1)
            substr.add(s[i])

        return max_len

        