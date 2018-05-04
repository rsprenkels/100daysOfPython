from tarifa import Tarifa
from unittest import mock
from io import StringIO

def test_1():
    doOneCase_withfiles('testdata/tarifa.1.in', 'testdata/tarifa.1.ans')

def test_2():
    doOneCase_withfiles('testdata/tarifa.2.in', 'testdata/tarifa.2.ans')

def test_3():
    doOneCase_withfiles('testdata/tarifa.3.in', 'testdata/tarifa.3.ans')

@mock.patch('sys.stdout', new_callable=StringIO)
def doOneCase_withfiles(inFile, outFile, mock_stdout):
    user_input = open(inFile, 'r').read().split('\n')[:-1]
    expected_output = open(outFile, 'r').read().split('\n')[:-1]
    with mock.patch('builtins.input', side_effect=user_input):
        obj = Tarifa()
        obj.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'
