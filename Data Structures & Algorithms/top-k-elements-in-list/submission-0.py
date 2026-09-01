import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        sorted_freq = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))

        freq_list = list(sorted_freq)

        ans = []

        for i in range(k):
            ans.append(freq_list[i])

        return ans