import collections
import heapq

class Solution:

    def solve(self, meetings):
        meetings = sorted(meetings, key=lambda x: x[0])
        queue = []
        _max = 0
        for meeting in meetings:
            while len(queue) > 0:
                end = queue[0]
                if end < meeting[0]:
                    heapq.heappop(queue)
                else:
                    break
            heapq.heappush(queue, meeting[1])
            _max = max(_max, len(queue))
        return _max


if __name__ == '__main__':
    from utils.judge import Judge
    Judge.judge(Solution())
