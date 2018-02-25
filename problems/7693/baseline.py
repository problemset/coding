class Solution:

    def cal(self, x, a, b, c):
        return x**2 * a + x * b + c

    def solve(self, nums, a, b, c):
        ret = []
        if len(nums) == 0:
            return ret
        if a == 0:
            for x in nums:
                ret.append(self.cal(x, a, b, c))
            if b >= 0:
                return ret
            else:
                return list(reversed(ret))

        optimal = -b/(2*a)
        _delta = float('inf')
        _mid = None
        for i, x in enumerate(nums):
            if abs(x - optimal) < _delta:
                _mid = i
                _delta = abs(x - optimal)
        ret.append(self.cal(nums[_mid], a, b, c))
        _pre = _mid - 1
        _post = _mid + 1
        while _pre >= 0 or _post < len(nums):
            if _pre < 0:
                ret.append(self.cal(nums[_post], a, b, c))
                _post += 1
            elif _post >= len(nums):
                ret.append(self.cal(nums[_pre], a, b, c))
                _pre -= 1
            else:
                if abs(nums[_pre] - optimal) <= abs(nums[_post] - optimal):
                    ret.append(self.cal(nums[_pre], a, b, c))
                    _pre -= 1
                else:
                    ret.append(self.cal(nums[_post], a, b, c))
                    _post += 1
        if a < 0:
            ret.reverse()

        return ret


if __name__ == '__main__':
    from utils.judge import Judge
    Judge.judge(Solution())
