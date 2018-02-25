class Solution:

    def solve(self, nums, k):
        n = len(nums)
        next_bloom = dict()
        last_bloom = dict()
        for i in range(n):
            next_bloom[i] = None
            last_bloom[i] = None

        for day, idx in enumerate(nums):
            idx -= 1

            if next_bloom[idx] is not None and next_bloom[idx] - idx == k + 1:
                return day + 1
            if last_bloom[idx] is not None and idx - last_bloom[idx] == k + 1:
                return day + 1

            for i in range(idx, -1, -1):
                if next_bloom[i] is not None and next_bloom[i] < idx:
                    break
                next_bloom[i] = idx
            for i in range(idx, n):
                if last_bloom[i] is not None and last_bloom[i] > idx:
                    break
                last_bloom[i] = idx
        return -1


if __name__ == '__main__':
    from utils.judge import Judge
    Judge.judge(Solution())
