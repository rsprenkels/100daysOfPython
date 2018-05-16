from ceiling import Ostgotska, Tree, Node
from unittest import mock
from io import StringIO
import pytest

def test_node():
    n = Node(22)
    assert n.value == 22

def test_tree():
    t = Tree()
    assert t.getShape() == ''
    t.insert(5)
    assert t.getShape() == 'R'
    t.insert(7)
    assert t.getShape() == 'RrR'
    t.insert(6)
    assert t.getShape() == 'RrRlR'

def test_4():
    t = Tree()
    t.insert(3)
    t.insert(1)
    t.insert(2)
    t.insert(4000)
    print("[{}]".format(t.getShape()))


# @pytest.mark.skip(reason="first test nodes")
def test_1():
    doOneCase_withfiles('testdata/1.in', 'testdata/1.ans')

# @pytest.mark.skip(reason="first test nodes")
def test_2():
    doOneCase_withfiles('testdata/2.in', 'testdata/2.ans')

@mock.patch('sys.stdout', new_callable=StringIO)
def doOneCase_withfiles(inFile, outFile, mock_stdout):
    user_input = open(inFile, 'r').read().split('\n')[:-1]
    expected_output = open(outFile, 'r').read().split('\n')[:-1]
    with mock.patch('builtins.input', side_effect=user_input):
        obj = Ostgotska()
        obj.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'
