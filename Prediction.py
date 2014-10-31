"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
Prediction Class: Implements instances of predictions for a soccer game
11/30/2012
"""

class Prediction(object):
    """Implements a prediction class for a CFC match, all attributes are relative to CFC"""
    
    def __init__(self,user,game,result,scoreline=[],cfcScorers=[],oppositionScorers=[],points=0):
        self.user = user
        self.game = game
        self.result =  int(result)
        self.cfcScorers = [] if cfcScorers=='[]' else [int(x) for x in cfcScorers[1:-1].split(", ")]
        self.oppositionScorers = [] if oppositionScorers=='[]' else [int(x) for x in oppositionScorers[1:-1].split(", ")]
        self.scoreline = [] if scoreline=='[]' else [int(x) for x in scoreline[1:-1].split(", ")]
        self.points = points

    def updatePoints(self,points):
        """Sets the number of points earned by the prediction"""
        self.points = points
        
    def calculatePoints(self,game_result):
        """Calculates the number of points and accuracy from the given result"""
        totalPoints = 1 + 5 + sum(game_result.result) #correct result=1pt, correct scoreline=5pts,1pt per scorer
        points = 0
        cfcScorers = game_result.cfcScorers
        oppositionScorers = game_result.oppositionScorers
        if game_result.result[0]>game_result.result[1]: result = 1
        elif game_result.result[0]==game_result.result[1]: result = 0
        else: result = -1

        if ((self.scoreline[0]==game_result.result[0]) and (self.scoreline[1]==game_result.result[1])):
            points+=5
        if self.result==result:
            points +=1
        for scorer in self.cfcScorers:
            if scorer in cfcScorers:
                points+=1
                cfcScorers.remove(scorer)
        for scorer in self.oppositionScorers:
            if scorer in oppositionScorers:
                points+=1
                oppositionScorers.remove(scorer)
        
        accuracy = int((points*100.0)/totalPoints)
        #print points,accuracy
        self.points = points
        return points,accuracy
            
