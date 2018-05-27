class Solution:

    def solve(self, meetings):
        meetings = sorted(meetings, key=lambda x: x[0])
        _max = 0
        for meeting in meetings:
            if meeting[0] < _max:
                return False
            else:
                _max = max(_max, meeting[1])
        return True


if __name__ == '__main__':
    from utils.judge import Judge
    Judge.judge(Solution())
