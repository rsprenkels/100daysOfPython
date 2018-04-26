
class TennisScore:

    def __init__(self):
        self.scorePlayerA = 0
        self.scorePlayerB = 0
        self.displayPoints = {
            0:"love",
            1:"fifteen",
            2:"thirty",
            3:"fourty",
            4:"advantage"
        }

    def showScore(self):
        if(self.scorePlayerA == 4):
            return 'advantage player A'
        elif(self.scorePlayerB == 4):
            return 'advantage player B'
        elif(self.scorePlayerA == 5):
            return 'game player A'
        elif(self.scorePlayerB == 5):
            return 'game player B'
        elif(self.scorePlayerA == 3 and self.scorePlayerB == 3):
            return 'deuce'
        else:
            return self.displayPoints[self.scorePlayerA] + ' - ' + self.displayPoints[self.scorePlayerB]

    def scoresPoint(self, player):
        if(player == 'A'):
            self.scorePlayerA += 1
        elif(player == 'B'):
            self.scorePlayerB += 1
            
        if (self.scorePlayerA == 4 and self.scorePlayerB == 4):
            self.scorePlayerA = 3
            self.scorePlayerB = 3
            