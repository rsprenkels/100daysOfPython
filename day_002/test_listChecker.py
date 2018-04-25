import listChecker

def test_emptyList(): 
    assert listChecker.ListChecker().isConsistent() == True

def test_listOneElement():
    assert listChecker.ListChecker().isConsistent(['1234']) == True

def test_notConsistent():
    assert listChecker.ListChecker().isConsistent(
        ['1234',
         '12345']
    ) == False

def test_Consistent():
    assert listChecker.ListChecker().isConsistent(
        ['1234',
         '12888']
    ) == True


def test_Consistent_longerList_OK():
    assert listChecker.ListChecker().isConsistent(
        ['1234',
         '12888',
         '9876',
         '1212']
    ) == True

def test_Consistent_longerList_NOTOK():
    assert listChecker.ListChecker().isConsistent(
        ['1234',
         '12888',
         '9876',
         '1288']
    ) == False
    
def test_notConsistent():
    assert listChecker.ListChecker().isConsistent(
        ['12 34',
         '12345']
    ) == False    
