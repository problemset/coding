import os
import inspect
import json


class Judge:
    @staticmethod
    def judge(solution, path=None):
        if path is None:
            path = os.path.dirname(os.path.realpath(inspect.stack()[1].filename))
        with open(os.path.join(path, 'tests.json')) as f:
            failed = False
            for pair in json.load(f):
                _out = solution.solve(*pair['in'])
                if pair['out'] != _out:
                    print('Failed for case %s, expected result %s, real result %s.' %
                          (json.dumps(pair['in']), json.dumps(pair['out']), json.dumps(_out)))
                    failed = True
                    break
            if not failed:
                print("Accepted")
