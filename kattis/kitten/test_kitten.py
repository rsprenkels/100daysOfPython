from unittest import mock
from io import StringIO

class Kitten:
    def __init__(self):
        self.tree = {}

    def run(self):
        kittenBranch = int(input())
        while True:
            branch = list(map(int, input().split()))
            if (branch[0] == -1):
                break
            self.tree[branch[0]] = branch[1::]
        routeDown = [kittenBranch]
        while True:
            foundBranch, theBranch = self.getNextBranchDown(routeDown[-1])
            if (not foundBranch):
                break
            routeDown.append(theBranch)
        print(' '.join(str(x) for x in routeDown))
        
    def getNextBranchDown(self, fromThisBranch):
        for branch, reachableFrom in self.tree.items():
            if (fromThisBranch in reachableFrom):
                return [True, branch]
        return [False, -1]
            
@mock.patch('sys.stdout', new_callable=StringIO)
def test_1(mock_stdout):
    user_input = [
            '14',
            '25 24',
            '4 3 1 2',
            '13 9 4 11',
            '10 20 8 7',
            '32 10 21',
            '23 13 19 32 22',
            '19 12 5 14 17 30',
            '14 6 15 16',
            '30 18 31 29',
            '24 23 26',
            '26 27 28',
            '-1'
        ]
    expected_output = ['14 19 23 24 25']
    with mock.patch('builtins.input', side_effect=user_input):
        Kitten().run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'

if __name__ == '__main__':
    Kitten().run()
