from unittest import mock
from io import StringIO

def setup_function(function):
    print("setting up test function %s" % function)

@mock.patch('sys.stdout', new_callable=StringIO)
def test_short(mock_stdout):
    user_input = [
        '11 15'
    ]
    expected_output = [
        '19'
    ]
    with mock.patch('builtins.input', side_effect=user_input):
        __import__('r2')
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'

