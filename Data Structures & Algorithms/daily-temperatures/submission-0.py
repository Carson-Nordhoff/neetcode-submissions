class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        ans = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:

                prev = stack.pop()
                length = i-prev[1]

                ans[prev[1]] = length

            stack.append((temp, i))

        return ans
                

            
        