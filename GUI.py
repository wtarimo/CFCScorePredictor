"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
This module manages instances of games
11/11/2012
"""

from Game import *




def userInputBox(win):
    """Creates and diplays graphical fields for user signing and registration"""

    Text(Point(55,50), "Full Name:").draw(win)
    rName = Entry(Point(245,50),30); rName.draw(win)
    Text(Point(55,75), "Username:").draw(win)
    rUsername = Entry(Point(200,75),20); rUsername.draw(win)
    Text(Point(56,100), "Password:").draw(win)
    rPassword1 = Entry(Point(200,100),20); rPassword1.draw(win)
    Text(Point(56,125), "Password:").draw(win)
    rPassword2 = Entry(Point(200,125),20); rPassword2.draw(win)

    Text(Point(55,225), "Username:").draw(win)
    lUsername = Entry(Point(200,225),20); lUsername.draw(win)
    Text(Point(56,250), "Password:").draw(win)
    lPassword = Entry(Point(200,250),20); lPassword.draw(win)

    rButton = Buttons(win,Point(230,160),120,25,"REGISTER"); rButton.Activate()
    lButton = Buttons(win,Point(230,285),120,25,"LOGIN"); lButton.Activate()

def fixtureInputBox(win):
    """Creates and diplays graphical fields for fixture input"""
    Text(Point(113,50), "Game #:").draw(win)
    fgame = Entry(Point(240,50),20); fgame.draw(win)
    Text(Point(103,75), "Opponent:").draw(win)
    fopponent = Entry(Point(240,75),20); fopponent.draw(win)
    Text(Point(118,100), "Time:").draw(win)
    ftime = Entry(Point(240,100),20); ftime.draw(win)
    Text(Point(116,125), "Venue:").draw(win)
    fvenue = Entry(Point(240,125),20); fvenue.draw(win)
    Text(Point(116,150), "Result:").draw(win)
    fresult = Entry(Point(240,150),20); fresult.draw(win)
    Text(Point(100,175), "cfcScorers:").draw(win)
    fcfcScorers = Entry(Point(240,175),20); fcfcScorers.draw(win)
    Text(Point(75,200), "OppositionScorers:").draw(win)
    foppositionScorers = Entry(Point(240,200),20); foppositionScorers.draw(win)
    
    submitFButton = Buttons(win,Point(230,235),150,25,"SUBMIT FIXTURE"); submitFButton.Activate()

    Text(Point(113,300), "Game #:").draw(win)
    ugame = Entry(Point(240,300),20); ugame.draw(win)
    Text(Point(116,325), "Result:").draw(win)
    uresult = Entry(Point(240,325),20); uresult.draw(win)
    Text(Point(100,350), "cfcScorers:").draw(win)
    ucfcScorers = Entry(Point(240,350),20); ucfcScorers.draw(win)
    Text(Point(75,375), "OppositionScorers:").draw(win)
    uoppositionScorers = Entry(Point(240,375),20); uoppositionScorers.draw(win)
    
    updateFButton = Buttons(win,Point(230,415),150,25,"UPDATE RESULTS"); updateFButton.Activate()

def predictionInputBox(win):
    """Creates and diplays graphical fields for prediction input"""
    Text(Point(111,50), "Game #:").draw(win)
    game = Entry(Point(240,50),20); game.draw(win)
    Text(Point(116,80), "Result:").draw(win)
    result = Entry(Point(240,80),20); result.draw(win)
    Text(Point(107,110), "Scoreline:").draw(win)
    scoreline = Entry(Point(240,110),20); scoreline.draw(win)
    Text(Point(100,140), "cfcScorers:").draw(win)
    cfcScorers = Entry(Point(240,140),20); cfcScorers.draw(win)
    Text(Point(75,170), "OppositionScorers:").draw(win)
    oppositionScorers = Entry(Point(240,170),20); oppositionScorers.draw(win)
    
    submitRButton = Buttons(win,Point(230,235),170,25,"SUBMIT RESULT"); submitRButton.Activate()

def displayStandings(win,standings):
    """Displays the game standings on user points"""
    text = Text(Point(725,40),"GAME STANDINGS"); text.setFill('grey'); text.setStyle('bold');text.setSize(20); text.draw(win)
    #standings = registry.getStandings()
    if len(standings)>10: standings=standings[:10]
    Text(Point(700,70), " _________Name:__________     _Points:_ _Accuracy:_").draw(win)
    (x,y) = (600,95)
    for i in range(3):
        y = 95
        x = [600,780,850][i]
        for record in standings:
            Text(Point(x,y),record[i]).draw(win)
            y+=20

def displaySchedule(win,fixtures,game):
    """Displays the schedule for the 5 recent fixtures by game #"""
    text = Text(Point(730,325),"FIXTURE SCHEDULE"); text.setFill('grey'); text.setStyle('bold');text.setSize(20); text.draw(win)
    #fixtures = schedule.fixtures
    if len(fixtures)>5: fixtures = fixtures[:5]
    fixtures = [[str(f.game),f.opponent.split()[0],f.time,str(f.result),str(f.cfcScorers),str(f.oppositionScorers)] for f in fixtures]
    Text(Point(710,350), "Game#: __Opponent:__  ____Time:____  _Result_ _cfcScorers_ _oppScorers_").draw(win)
    (x,y) = (470,375)
    for i in range(6):
        y = 375
        x = [465,545,665,755,830,940][i]
        for record in fixtures:
            text = Text(Point(x,y),record[i])
            if i==0 and int(record[0])>game: text = Text(Point(x,y),record[0]+" Future")
            elif i==0 and int(record[0])==game: text = Text(Point(x,y),record[0]+" Next")
            elif i==0 and int(record[0])<game: text = Text(Point(x,y),record[0]+" Played")
            text.setFill('blue') if int(record[0])>game else text.setFill('red')
            if int(record[0])==game: text.setFill('green4')
            text.setSize(10); text.draw(win)
            y+=20
            
def displayPredictions(win,pDB,username,game):
    """Diplays predictions sumbmitted by the user"""
    text = Text(Point(730,505),"YOUR PREDICTIONS"); text.setFill('grey'); text.setStyle('bold');text.setSize(20); text.draw(win)
    predictions = pDB.getPredictions(username)
    if len(predictions)>5: predictions = predictions[:5]
    predictions = [[str(p.game),str(p.result),str(p.scoreline),str(p.cfcScorers),str(p.oppositionScorers),str(p.points)] for p in predictions]
    Text(Point(700,530), "_Game#:_ _Result:_  _Scoreline:_ _cfcScorers_ _oppScorers_ _Points:_").draw(win)
    for i in range(6):
        y = 555
        x = [475,550,640,740,830,920][i]
        for record in predictions:
            text = Text(Point(x,y),record[i])
            text.setFill('blue') if int(record[0])>game else text.setFill('red')
            if int(record[0])==game: text.setFill('green4')
            text.setSize(11); text.draw(win)
            y+=20

def displayOutput(win,text):
    """Displays info to the user at the bottom left windows"""
    text = text.split(",")
    x,y = 215,485
    for record in text:
            text = Text(Point(x,y),record); text.setFill('grey2')
            text.setSize(11); text.draw(win)
            y+=25 
    
    

