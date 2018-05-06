from unittest import mock
from io import StringIO

class Batterup:
    def run():
        numOfAtbats = int(input())
        atbats = map(int, input().split())
        validAtbats = 0
        battingTotal = 0
        for atbat in atbats:
            if (atbat >= 0):
                validAtbats += 1
                battingTotal += atbat
        print(battingTotal / validAtbats)

@mock.patch('sys.stdout', new_callable=StringIO)
def test_1(mock_stdout):
    user_input = [
            '3',
            '3 0 2'
        ]
    expected_output = ['1.6666666666666667']
    with mock.patch('builtins.input', side_effect=user_input):
        Batterup.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'

@mock.patch('sys.stdout', new_callable=StringIO)
def test_2(mock_stdout):
    user_input = [
            '3',
            '3 -1 5'
        ]
    expected_output = ['4.0']
    with mock.patch('builtins.input', side_effect=user_input):
        Batterup.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'

if __name__ == '__main__':
    Batterup.run()
