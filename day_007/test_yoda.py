from yoda import Yoda
from unittest import mock
from io import StringIO

# https://open.kattis.com/problems/yoda/file/statement/samples.zip

def test_1():
    # doOneCase()
    doOneCase_withfiles('testdata/yoda.1.in', 'testdata/yoda.1.ans')

def test_2():
    doOneCase_withfiles('testdata/yoda.2.in', 'testdata/yoda.2.ans')

def test_3():
    doOneCase_withfiles('testdata/yoda.3.in', 'testdata/yoda.3.ans')

@mock.patch('sys.stdout', new_callable=StringIO)
def doOneCase(mock_stdout):
    user_input = [
        '300',
        '500'
    ]
    expected_output = [
        '0',
        '500'
    ]
    with mock.patch('builtins.input', side_effect=user_input):
        obj = Yoda()
        obj.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'

@mock.patch('sys.stdout', new_callable=StringIO)
def doOneCase_withfiles(inFile, outFile, mock_stdout):
    user_input = open(inFile, 'r').read().split('\n')[:-1]
    expected_output = open(outFile, 'r').read().split('\n')[:-1]
    with mock.patch('builtins.input', side_effect=user_input):
        obj = Yoda()
        obj.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'
