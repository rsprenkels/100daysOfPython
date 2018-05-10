from wrapper import Wrapper


def test_wrapper():
    assert Wrapper().wrap("hoi", 4) == "hoi"


def test_longer():
    assert Wrapper().wrap("hier hoi", 4) == "hier\nhoi"


def test_b():
    assert Wrapper().wrap("h er hoi", 4) == "h er\nhoi"

def test_c():
    assert Wrapper().wrap("h er vier vijf", 4) == "h er\nvier\nvijf"


def test_d():
    assert Wrapper().wrap("aaaaa", 4) == "aaaa\na"


def test_e():
    assert Wrapper().wrap("aa aaa", 4) == "aa\naaa"


def test_f():
    assert Wrapper().wrap("a bb ccc dddd eeeee", 4) == "a bb\nccc\ndddd\neeee\ne"


def test_g():
    assert Wrapper().wrap(" 123456", 4) == "\n1234\n56"
