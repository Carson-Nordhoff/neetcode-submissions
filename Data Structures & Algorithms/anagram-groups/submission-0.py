from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:

            counts = [0]*256

            for char in word:
                counts[ord(char)] += 1
            
            key = []
            for ascii_val in range(256):
                if counts[ascii_val] > 0:
                    key.append(chr(ascii_val) * counts[ascii_val])

            str_key = "".join(key)

            anagrams[str_key].append(word)

        ans = []

        for sublist in anagrams.values():
            ans.append(sublist)

        return ans