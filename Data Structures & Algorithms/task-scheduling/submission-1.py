from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        counts = [-v for v in freq.values()]
        heapq.heapify(counts)

        q = deque()

        time = 0
        while counts or q:
            time += 1

            if counts:

                cnt = 1 + heapq.heappop(counts)

                if cnt:

                    q.append([cnt, time+n])

            if q and q[0][1] == time:
                heapq.heappush(counts, q.popleft()[0])

        return time

        