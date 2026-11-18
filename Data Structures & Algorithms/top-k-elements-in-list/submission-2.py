from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        buckets = defaultdict(list)

        for num, count in counts.items():
            buckets[count].append(num)
        
        ans = []
        for i in range(len(nums), -1, -1):
            ans.extend(buckets[i])

            if len(ans) >= k:
                return ans


        return ans[:k]
