"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
Game Class: Implements an instance of the game
11/11/2012
"""
from Registrar import *
from Schedule import *
from PredictionsDatabase import *
from graphics import *
from buttons import Buttons
from collections import *

class Game(object):
    """Implements an instances of the game"""
    def __init__(self,win):
        self.user = None
        self.registry=Registrar()
        self.pDB=PredictionsDatabase()
        self.schedule = Schedule()
        self.win = win

    def quitGame(self):
        """Saves game data into files"""
        self.registry.exportUsers()
        self.pDB.exportPredictions()

    def userInputBox(self):
        """Creates and diplays graphical fields for user signing and registration"""
        Text(Point(55,50), "Full Name:").draw(self.win)
        rName = Entry(Point(245,50),30); rName.draw(self.win)
        Text(Point(55,75), "Username:").draw(self.win)
        rUsername = Entry(Point(200,75),20); rUsername.draw(self.win)
        Text(Point(56,100), "Password:").draw(self.win)
        rPassword1 = Entry(Point(200,100),20); rPassword1.draw(self.win)
        Text(Point(56,125), "Password:").draw(self.win)
        rPassword2 = Entry(Point(200,125),20); rPassword2.draw(self.win)

        Text(Point(55,225), "Username:").draw(self.win)
        lUsername = Entry(Point(200,225),20); lUsername.draw(self.win)
        Text(Point(56,250), "Password:").draw(self.win)
        lPassword = Entry(Point(200,250),20); lPassword.draw(self.win)

        rButton = Buttons(self.win,Point(210,160),120,25,"REGISTER"); rButton.Activate()
        lButton = Buttons(self.win,Point(210,285),120,25,"LOGIN"); lButton.Activate()

        return rName,rUsername,rPassword1,rPassword2,lUsername,lPassword,rButton,lButton

    def fixtureInputBox(self):
        """Creates and diplays graphical fields for fixture input"""
        Text(Point(110,40), "Game #:").draw(self.win)
        fgame = Entry(Point(168,40),4); fgame.draw(self.win)
        Text(Point(233,40), "Result:").draw(self.win)
        fresult = Entry(Point(296,40),7); fresult.setText("[]"); fresult.draw(self.win)
        Text(Point(103,65), "Opponent:").draw(self.win)
        fopponent = Entry(Point(240,65),20); fopponent.draw(self.win)
        Text(Point(118,90), "Time:").draw(self.win)
        ftime = Entry(Point(240,90),20); ftime.draw(self.win)
        Text(Point(116,115), "Venue:").draw(self.win)
        fvenue = Entry(Point(240,115),20); fvenue.draw(self.win)
        Text(Point(100,140), "cfcScorers:").draw(self.win)
        fcfcScorers = Entry(Point(240,140),20); fcfcScorers.setText("[]"); fcfcScorers.draw(self.win)
        Text(Point(75,165), "OppositionScorers:").draw(self.win)
        foppositionScorers = Entry(Point(240,165),20); foppositionScorers.setText("[]"); foppositionScorers.draw(self.win)
        
        submitFButton = Buttons(self.win,Point(230,210),150,25,"SUBMIT FIXTURE"); submitFButton.Activate()

        Text(Point(110,255), "Game #:").draw(self.win)
        ugame = Entry(Point(168,255),4); ugame.draw(self.win)
        Text(Point(233,255), "Result:").draw(self.win)
        uresult = Entry(Point(296,255),7); uresult.setText("[]"); uresult.draw(self.win)
        Text(Point(100,280), "cfcScorers:").draw(self.win)
        ucfcScorers = Entry(Point(240,280),20); ucfcScorers.setText("[]"); ucfcScorers.draw(self.win)
        Text(Point(75,305), "OppositionScorers:").draw(self.win)
        uoppositionScorers = Entry(Point(240,305),20); uoppositionScorers.setText("[]"); uoppositionScorers.draw(self.win)
        
        updateFButton = Buttons(self.win,Point(230,350),150,25,"UPDATE RESULTS"); updateFButton.Activate()

        Text(Point(80,410), "Next Game #:").draw(self.win)
        nGame = Entry(Point(162,410),5); nGame.draw(self.win)
        nextButton = Buttons(self.win,Point(310,410),150,25,"UPDATE GAME#"); nextButton.Activate()

        return nGame,nextButton,fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,\
               uresult,ucfcScorers,uoppositionScorers,submitFButton,updateFButton

    def clearInputBox(self,items=[]):
        """Clears the inputBox"""
        for item in items: item.undraw()
        inputWin = Rectangle(Point(7,7),Point(420,440)); inputWin.setOutline('white'); inputWin.setFill('white'); inputWin.draw(self.win)

    def predictionInputBox(self):
        """Creates and diplays graphical fields for prediction input"""
        Text(Point(111,50), "Game #:").draw(self.win)
        game = Entry(Point(240,50),20); game.draw(self.win)
        Text(Point(116,80), "Result:").draw(self.win)
        result = Entry(Point(240,80),20); result.setText("1, 0 or -1"); result.draw(self.win)
        Text(Point(107,110), "Scoreline:").draw(self.win)
        scoreline = Entry(Point(240,110),20); scoreline.setText("[a, b]"); scoreline.draw(self.win)
        Text(Point(100,140), "cfcScorers:").draw(self.win)
        cfcScorers = Entry(Point(240,140),20); cfcScorers.setText("[]"); cfcScorers.draw(self.win)
        Text(Point(75,170), "OppositionScorers:").draw(self.win)
        oppositionScorers = Entry(Point(240,170),20); oppositionScorers.setText("[]"); oppositionScorers.draw(self.win)
        
        submitPButton = Buttons(self.win,Point(230,235),170,25,"SUBMIT/UPDATE"); submitPButton.Activate()
        return game,result,scoreline,cfcScorers,oppositionScorers,submitPButton
    
    def displayStandings(self):
        """Displays the game standings on user points"""
        standingsWin = Rectangle(Point(430,5),Point(995,295)); standingsWin.setFill('white'); standingsWin.draw(self.win)
        text = Text(Point(725,40),"GAME STANDINGS"); text.setFill('grey'); text.setStyle('bold');text.setSize(20); text.draw(self.win)
        standings = self.registry.getStandings()
        if len(standings)>10: standings=standings[:10]
        Text(Point(700,70), " _______userName:________     _Points:_ _Accuracy:_").draw(self.win)
        (x,y) = (600,95)
        for i in range(3):
            y = 95
            x = [600,780,850][i]
            for record in standings:
                Text(Point(x,y),record[i]).draw(self.win)
                y+=20

    def displaySchedule(self):
        """Displays the schedule for the 5 recent fixtures by game #"""
        scheduleWin = Rectangle(Point(430,300),Point(995,475)); scheduleWin.setFill('white'); scheduleWin.draw(self.win)
        text = Text(Point(730,325),"FIXTURE SCHEDULE"); text.setFill('grey'); text.setStyle('bold');text.setSize(20); text.draw(self.win)
        fixtures = self.schedule.fixtures
        game = self.schedule.nextFixture
        if len(fixtures)>5: fixtures = fixtures[:5]
        fixtures = [[str(f.game),f.opponent.split()[0],f.time,str(f.result),str(f.cfcScorers),str(f.oppositionScorers)] for f in fixtures]
        Text(Point(710,350), "Game#: __Opponent:__  ____Time:____  _Result_ _cfcScorers_ _oppScorers_").draw(self.win)
        (x,y) = (470,375)
        for i in range(6):
            y = 375
            x = [465,545,665,755,840,940][i]
            for record in fixtures:
                text = Text(Point(x,y),record[i])
                if i==0 and int(record[0])>game: text = Text(Point(x,y),record[0]+" Future")
                elif i==0 and int(record[0])==game: text = Text(Point(x,y),record[0]+" UpNext")
                elif i==0 and int(record[0])<game: text = Text(Point(x,y),record[0]+" Played")
                text.setFill('blue') if int(record[0])>game else text.setFill('red')
                if int(record[0])==game: text.setFill('green4')
                text.setSize(10); text.draw(self.win)
                y+=20
                
    def displayPredictions(self):
        """Diplays predictions sumbmitted by the user"""
        predictionWin = Rectangle(Point(430,480),Point(995,645)); predictionWin.setFill('white'); predictionWin.draw(self.win)
        #text = Text(Point(730,505),"YOUR PREDICTIONS"); text.setFill('grey'); text.setStyle('bold');text.setSize(20); text.draw(self.win)
        if self.user and self.user.user_type == 'user':
            predictions = self.pDB.getPredictions(self.user.username)
            if predictions:
                text = Text(Point(730,505),"YOUR PREDICTIONS"); text.setFill('grey'); text.setStyle('bold');text.setSize(20); text.draw(self.win)
                game = self.schedule.nextFixture
                if len(predictions)>5: predictions = predictions[:5]
                predictions = [[str(p.game),str(p.result),str(p.scoreline),str(p.cfcScorers),str(p.oppositionScorers),str(p.points)] for p in predictions]
                Text(Point(700,530), "_Game#:_ _Result:_  _Scoreline:_ _cfcScorers_ _oppScorers_ _Points:_").draw(self.win)
                for i in range(6):
                    y = 550
                    x = [475,550,640,740,830,920][i]
                    for record in predictions:
                        text = Text(Point(x,y),record[i])
                        text.setFill('blue') if int(record[0])>game else text.setFill('red')
                        if int(record[0])==game: text.setFill('green4')
                        text.setSize(11); text.draw(self.win)
                        y+=20
            else: self.displayPredictionsSummary()
        else: self.displayPredictionsSummary()

        
    def displayPredictionsSummary(self):
        """Displays the predictions statistics and trends on the next game"""
        game = self.schedule.nextFixture
        text = Text(Point(725,505),"PREDICTIONS SUMMARY ON GAME# "+str(game)); text.setFill('grey'); text.setStyle('bold');text.setSize(20); text.draw(self.win)
        game_predictions = [p for p in self.pDB.predictions if p.game==game]
        cfcScorers = [p.cfcScorers for p in game_predictions]
        cfcScorers = Counter([x for sublist in cfcScorers for x in sublist])
        oppositionScorers = [p.oppositionScorers for p in game_predictions]
        oppositionScorers = Counter([x for sublist in oppositionScorers for x in sublist])
        scorelines = Counter([str(p.scoreline) for p in game_predictions])
        top_cfcScorers, cfcScorers_count = cfcScorers.most_common(5), sum(cfcScorers.values())
        top_oppositionScorers, oppositionScorers_count = oppositionScorers.most_common(5), sum(oppositionScorers.values())
        top_scorelines, scorelines_count = scorelines.most_common(5), sum(scorelines.values())

        Text(Point(710,530), "CFC Scorers").draw(self.win)
        x,y = 710,550
        for i in range(len(top_cfcScorers)):
            Text(Point(x,y),str(top_cfcScorers[i][0]) +" : "+ str(int((top_cfcScorers[i][1]*100.0)/cfcScorers_count))+"%").draw(self.win)
            y+=20

        Text(Point(560,530), "Scorelines").draw(self.win)
        x,y = 560,550
        for i in range(len(top_scorelines)):
            Text(Point(x,y),str(top_scorelines[i][0]) +" : "+ str(int((top_scorelines[i][1]*100.0)/scorelines_count))+"%").draw(self.win)
            y+=20
            
        Text(Point(860,530), "Opposition Scorers").draw(self.win)
        x,y = 860,550
        for i in range(len(top_oppositionScorers)):
            Text(Point(x,y),str(top_oppositionScorers[i][0]) +" : "+ str(int((top_oppositionScorers[i][1]*100.0)/oppositionScorers_count))+"%").draw(self.win)
            y+=20

    def displayOutput(self,text,color):
        """Displays info to the user at the bottom left windows"""
        outputWin = Rectangle(Point(7,457),Point(423,578)); outputWin.setOutline('white'); outputWin.setFill('white'); outputWin.draw(self.win)
        text = text.split(";")
        x,y = 215,485
        for record in text:
            text = Text(Point(x,y),record); text.setFill(color); text.setFace('arial');
            text.setSize(11); text.setStyle('bold italic'); text.draw(self.win)
            y+=25 

    
