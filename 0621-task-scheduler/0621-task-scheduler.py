class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [cnt for cnt in count.values()]
        heapify_max(maxHeap)

        time = 0
        queue = deque()

        while maxHeap or queue:
            time += 1

            if maxHeap:
                cnt = heappop_max(maxHeap) - 1
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heappush_max(maxHeap, queue.popleft()[0])

        return time
                



