class Solution:

    def is_valid(self, nums):
        if nums[0] > 2:
            return False
        if nums[0] == 2 and nums[1] > 4:
            return False
        if nums[2] > 5:
            return False
        return True

    def to_time(self, nums):
        nums = [str(x) for x in nums]
        return ''.join(nums[0:2]) + ':' + ''.join(nums[2:4])

    def solve(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = set()
        _input = []
        for c in time:
            if c != ':':
                digits.add(int(c))
                _input.append(int(c))
        digits = list(digits)
        digits.sort()
        for i in range(3, -1, -1):
            for c in digits:
                if c > _input[i]:
                    _tmp = _input[i]
                    _input[i] = c
                    if self.is_valid(_input):
                        return self.to_time(_input)
                    _input[i] = _tmp
                    break
        return self.to_time([digits[0]]*4)


if __name__ == '__main__':
    from utils.judge import Judge
    Judge.judge(Solution())
