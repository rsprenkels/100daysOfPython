import tennisScore

def test_straightGameA():

    tc = tennisScore.TennisScore()
    assert tc.showScore() == 'love - love'

    tc.scoresPoint('A')
    assert tc.showScore() == 'fifteen - love'
    
    tc.scoresPoint('A')
    assert tc.showScore() == 'thirty - love'
    
    tc.scoresPoint('A')
    assert tc.showScore() == 'fourty - love'
    
    tc.scoresPoint('A')
    assert tc.showScore() == 'advantage player A'
    
    tc.scoresPoint('A')
    assert tc.showScore() == 'game player A'
    

def test_straightGameB():

    tc = tennisScore.TennisScore()
    assert tc.showScore() == 'love - love'

    tc.scoresPoint('B')
    assert tc.showScore() == 'love - fifteen'
    
    tc.scoresPoint('B')
    assert tc.showScore() == 'love - thirty'
    
    tc.scoresPoint('B')
    assert tc.showScore() == 'love - fourty'
    
    tc.scoresPoint('B')
    assert tc.showScore() == 'advantage player B'
    
    tc.scoresPoint('B')
    assert tc.showScore() == 'game player B'
    
def test_deuce():
    tc = tennisScore.TennisScore()
    tc.scoresPoint('B')
    tc.scoresPoint('B')
    tc.scoresPoint('B')
    tc.scoresPoint('A')
    tc.scoresPoint('A')
    tc.scoresPoint('A')
    assert tc.showScore() == 'deuce'

def test_deuce_advantage_deuce():
    tc = tennisScore.TennisScore()
    tc.scoresPoint('B')
    tc.scoresPoint('B')
    tc.scoresPoint('B')
    tc.scoresPoint('A')
    tc.scoresPoint('A')
    tc.scoresPoint('A')
    assert tc.showScore() == 'deuce'
    tc.scoresPoint('A')
    assert tc.showScore() == 'advantage player A'
    tc.scoresPoint('B')
    assert tc.showScore() == 'deuce'
    tc.scoresPoint('B')
    assert tc.showScore() == 'advantage player B'
    tc.scoresPoint('A')
    assert tc.showScore() == 'deuce'
    tc.scoresPoint('B')
    assert tc.showScore() == 'advantage player B'
    tc.scoresPoint('B')
    assert tc.showScore() == 'game player B'
