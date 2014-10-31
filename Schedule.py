"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
Schedule Class: Manages fixtures
11/30/2012
"""
from Fixture import *

class Schedule(object):
    """Implements a schedule class that manages game fixtures"""
    def __init__(self,fixtures=[],next_fixture=""):
        self.fixtures = fixtures
        self.fixtureCount = len(self.fixtures)
        self.nextFixture = next_fixture
        self.importFixtures()

    def addFixture(self,new_fixture):
        """Adds a fixture to the schedule"""
        for fixture in self.fixtures:
            if fixture.game == new_fixture.game:
                self.fixtureCount-=1
                self.fixtures.remove(fixture)
                break
        self.fixtures.append(new_fixture)
        self.fixtureCount+=1
        self.sortFixtures()

    def sortFixtures(self):
        """Sorts fixtures by game number in descending order"""
        self.fixtures = sorted(self.fixtures,key=lambda f: f.game,reverse=True)

    def updateFixture(self,game,result,cfcScorers,oppositionScorers):
        """Updates the results for the given game# in the schedule database"""
        fixture = self.getFixture(game)
        self.addFixture(Fixture(game,fixture.opponent,fixture.time,fixture.venue,result,cfcScorers,oppositionScorers))

    def getFixture(self,game):
        """Returns a fixture with the given game #"""
        for fixture in self.fixtures:
            if fixture.game == game:
                return fixture
        return False
        
    def setNext(self,game):
        """Sets the given game # as the next fixture"""
        self.nextFixture = game

    def getNext(self):
        """Returns the next game and current fixture for predictions"""
        return self.nextFixture
    
    def importFixtures(self):
        """Loads fixtures from fixtures.txt into the schedule"""
        self.fixtures = []
        lines = open("fixtures.txt")
        line = lines.readline()[:-1]
        self.nextFixture = int(line) if line else 0
        while True:
            line = lines.readline()[:-1]
            if line=="": break
            fields = line.split("|")
            fixture = Fixture(int(fields[0]),fields[1],fields[2],fields[3],fields[4],fields[5],fields[6])
            self.addFixture(fixture)

    def exportFixtures(self):
        """Saves all fixtures to fixtures.txt"""
        out = open("fixtures.txt","w")
        out.write("%s\n" % str(self.nextFixture))
        fixtures = [str(f.game)+"|"+f.opponent+"|"+f.time+"|"+f.venue+"|"+str(f.result)+"|"+str(f.cfcScorers)+"|"+str(f.oppositionScorers) for f in self.fixtures]
        out.writelines("%s\n" % fixture for fixture in fixtures)
        out.close()







