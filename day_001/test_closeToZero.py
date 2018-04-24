import closeToZero

def test1():
    '''one value'''
    myCloseToZero = closeToZero.CloseToZero()
    assert myCloseToZero.answer([1]) == 1
    assert myCloseToZero.answer([2]) == 2
    assert myCloseToZero.answer([-1]) == -1
    assert myCloseToZero.answer([-2]) == -2

def test2():
    '''two values'''
    myCloseToZero = closeToZero.CloseToZero()
    assert myCloseToZero.answer([1,1]) == 1
    assert myCloseToZero.answer([1,-1]) == 1
    assert myCloseToZero.answer([-1,1]) == 1
    assert myCloseToZero.answer([-1,-1]) == -1

    assert myCloseToZero.answer([1,2]) == 1
    assert myCloseToZero.answer([1,-2]) == 1
    assert myCloseToZero.answer([-1,2]) == -1
    assert myCloseToZero.answer([-1,-2]) == -1
    
    assert myCloseToZero.answer([2,1]) == 1
    assert myCloseToZero.answer([2,-1]) == -1
    assert myCloseToZero.answer([-2,1]) == 1
    assert myCloseToZero.answer([-2,-1]) == -1

def test3():
    '''three values'''
    myCloseToZero = closeToZero.CloseToZero()
    assert myCloseToZero.answer([1,2,3]) == 1
    assert myCloseToZero.answer([1,-2,3]) == 1

    