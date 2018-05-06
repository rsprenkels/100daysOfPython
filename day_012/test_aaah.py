from aaah import Aaah
from unittest import mock
from io import StringIO

@mock.patch('sys.stdout', new_callable=StringIO)
def test_1(mock_stdout):
    user_input      = ['ah', 'aaah'] 
    expected_output = ['no']
    with mock.patch('builtins.input', side_effect=user_input):
        Aaah.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'

@mock.patch('sys.stdout', new_callable=StringIO)
def test_2(mock_stdout):
    user_input      = ['aah', 'ah'] 
    expected_output = ['go']
    with mock.patch('builtins.input', side_effect=user_input):
        Aaah.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'
 
