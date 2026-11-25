class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        que = deque([])
        res = []
        left = 0

        for right in range(len(nums)):

            while que and que[-1] < nums[right]:
                que.pop()

            que.append(nums[right])

            if right-left+1 == k:

                res.append(que[0])

                if nums[left] == que[0]:
                    que.popleft()

                left += 1

        return res