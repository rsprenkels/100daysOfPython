from addNumbers import AddNumbers
from unittest import mock
from io import StringIO

def setup_function(function):
    print("setting up test function %s" % function)

@mock.patch('sys.stdout', new_callable=StringIO)
def test_short(mock_stdout):
    user_input = [
        '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
        '2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222'
    ]
    expected_output = [
        '3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333'
    ]
    with mock.patch('builtins.input', side_effect=user_input):
        an = AddNumbers()
        an.add()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'

