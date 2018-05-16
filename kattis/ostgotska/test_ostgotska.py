from ostgotska import Heartrate
from unittest import mock
from io import StringIO

def test_1():
    doOneCase(['dae ae ju traeligt va'],['dae ae ju traeligt va'])


def test_2():
    doOneCase(['haer talar vi rikssvenska'],['haer talar vi rikssvenska'])

# def test_2():
#    doOneCase_withfiles('testdata/2.in', 'testdata/2.ans')

@mock.patch('sys.stdout', new_callable=StringIO)
def doOneCase_withfiles(inFile, outFile, mock_stdout):
    user_input = open(inFile, 'r').read().split('\n')[:-1]
    expected_output = open(outFile, 'r').read().split('\n')[:-1]
    with mock.patch('builtins.input', side_effect=user_input):
        obj = Heartrate()
        obj.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'


@mock.patch('sys.stdout', new_callable=StringIO)
def doOneCase(user_input, expected_output, mock_stdout):
    with mock.patch('builtins.input', side_effect=user_input):
        obj = Heartrate()
        obj.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'
