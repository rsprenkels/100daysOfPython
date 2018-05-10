import qsort, another_sort


def test_qsort():
    hidden = 'secretB'
    s = qsort.Qsort()
    assert s.sort([1, 4, 2]) == [1, 2, 4]


def test_longer():
    s = qsort.Qsort()
    assert s.sort([1, 4, 2, 9, 3, 7, 6]) == [1, 2, 3, 4, 6, 7, 9]


def test_as():
    s = another_sort.AnotherSort()
    assert s.sort([1, 4, 211, 2, 9, 3, 7, 6]) == [1, 2, 3, 4, 6, 7, 9, 211]
