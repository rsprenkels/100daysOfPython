import anagram

def test_short():
    '''test a short anagram input'''
    generator = anagram.Anagram()
    assert generator.generate('A') == ['A']
    assert generator.generate('AB') == ['AB', 'BA']

def test_biro():
    '''test anagrams of biro'''
    generator = anagram.Anagram()
    assert generator.generate('biro') == [
        'biro', 'bior', 'brio', 'broi',
        'boir', 'bori', 'ibro', 'ibor',
        'irbo', 'irob', 'iobr', 'iorb',
        'rbio', 'rboi', 'ribo', 'riob',
        'robi', 'roib', 'obir', 'obri',
        'oibr', 'oirb', 'orbi', 'orib'
    ]
