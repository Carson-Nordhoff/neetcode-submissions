import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stack = [v for v in nums]
        self.k = k
        heapq.heapify(self.stack)

        while len(self.stack) > self.k:
            heapq.heappop(self.stack)

    def add(self, val: int) -> int:

        if len(self.stack) < self.k:
            heapq.heappush(self.stack, val)
            return self.stack[-self.k]

        if val > self.stack[0]:
            heapq.heappop(self.stack)
            heapq.heappush(self.stack, val)

        return self.stack[0]






        
