"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
Fixture Class: Implements a soccer game fixture
11/30/2012
"""

class Fixture(object):
    """Implements a soccer game fixture"""
    
    def __init__(self,game,opponent="",time="",venue="",result=[],cfcScorers=[],oppositionScorers=[]):
        self.game = game
        self.opponent = opponent
        self.time = time
        self.venue = venue
        self.result = [] if result=='[]' else [int(x) for x in result[1:-1].split(", ")]
        self.cfcScorers = [] if cfcScorers=='[]' else [int(x) for x in cfcScorers[1:-1].split(", ")]
        self.oppositionScorers = [] if oppositionScorers=='[]' else [int(x) for x in oppositionScorers[1:-1].split(", ")]
        

    def updateResults(self,result,cfcScorers,oppositionScorers):
        """Sets the result of the fixture"""
        self.result = result
        self.cfcScorers = cfcScorers
        self.oppositionScorers = oppositionScorers
        return self
        
            
