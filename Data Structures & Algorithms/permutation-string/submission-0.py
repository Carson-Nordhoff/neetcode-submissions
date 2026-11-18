from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        k = len(s1)

        s1_Count = defaultdict(int)
        s2_Count = defaultdict(int)

        for i in range(k):
            s1_Count[s1[i]] += 1
            s2_Count[s2[i]] += 1

        if s1_Count == s2_Count:
            return True

        for i in range(k, len(s2)):

            s2_Count[s2[i]] += 1
            s2_Count[s2[i-k]] -= 1

            if s2_Count[s2[i-k]] <= 0:
                s2_Count.pop(s2[i-k])

            if s2_Count == s1_Count:
                return True

        return False
        