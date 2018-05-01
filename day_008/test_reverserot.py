from reverserot import Reverserot
from unittest import mock
from io import StringIO

def test_1():
    doOneCase_withfiles('testdata/rot.in', 'testdata/rot.ans')

@mock.patch('sys.stdout', new_callable=StringIO)
def doOneCase_withfiles(inFile, outFile, mock_stdout):
    user_input = open(inFile, 'r').read().split('\n')[:-1]
    expected_output = open(outFile, 'r').read().split('\n')[:-1]
    with mock.patch('builtins.input', side_effect=user_input):
        obj = Reverserot()
        obj.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'
