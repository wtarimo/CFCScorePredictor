"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
This module manages instances of games
11/11/2012
"""

from Game import *
from graphics import *
from buttons import Buttons
from GUI import *



def main():
    """Creates and runs an instance of a game, together with graphical objects"""

    #_________Creates and initiates graphical objects___________#
    win = GraphWin("Chelsea FC, Score Prediction Game",1000,650)
    win.setBackground("grey")
    inputWin = Rectangle(Point(5,5),Point(425,450)); inputWin.setFill('white'); inputWin.draw(win)
    standingsWin = Rectangle(Point(430,5),Point(995,295)); standingsWin.setFill('white'); standingsWin.draw(win)
    scheduleWin = Rectangle(Point(430,300),Point(995,475)); scheduleWin.setFill('white'); scheduleWin.draw(win)
    predictionWin = Rectangle(Point(430,480),Point(995,645)); predictionWin.setFill('white'); predictionWin.draw(win)
    outputWin = Rectangle(Point(5,455),Point(425,610)); outputWin.setFill('white'); outputWin.draw(win)
    quitButton = Buttons(win,Point(100,615),120,50,"QUIT"); quitButton.Activate()
    submitFButton = Buttons(win,Point(1100,750),150,25,"SUBMIT FIXTURE")
    updateFButton = Buttons(win,Point(1100,750),150,25,"UPDATE RESULTS")
    submitPButton = Buttons(win,Point(1100,750),170,25,"SUBMIT/UPDATE")
    nextButton = Buttons(win,Point(1100,750),150,25,"UPDATE GAME#")
    nGame,rName,rUsername,rPassword1,rPassword2,lUsername,lPassword,game_num,result,scoreline,\
    cfcScorers,oppositionScorers,fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,\
    foppositionScorers,ugame,uresult,ucfcScorers,uoppositionScorers = [Text(Point(1100,750),"")]*23
    #__________________________________________________________#
    
    #_________Create and start an instance of a game___________#
    game = Game(win)
    rName,rUsername,rPassword1,rPassword2,lUsername,lPassword,rButton,lButton = game.userInputBox()
    game.displayStandings()
    game.displaySchedule()
    game.displayPredictions()
    game.displayOutput("REGISTER/LOGIN!; Hello!. Welcome to Chelsea FC Score Prediction Game!;\
    To get started:; Register a new account or Login to an existing account",'grey2')
    #__________________________________________________________#
    
    #____This section runs/loops-through an instance of a game using mouse clicks on buttons____#
    pt = win.getMouse() #Waits for the fist mouse click
    
    while not quitButton.Clicked(pt):

        #_______User Registration_______#
        if rButton.Clicked(pt):
            """Do user registration"""
            credentials = [rName.getText(),rUsername.getText(),rPassword1.getText()]
            user = User(rName.getText(),rUsername.getText(),rPassword1.getText())
            if any(item=='' for item in credentials):
                game.displayOutput("***ERROR!: Some fields are empty!; Please re-try!",'red')
            
            elif rPassword1.getText() != rPassword2.getText(): #Passwords don't match
                game.displayOutput("***ERROR!: Entered passwords don't match!; Please re-try!",'red')
            
            elif game.registry.register(user):
                game.clearInputBox([rName,rUsername,rPassword1,rPassword2,lUsername,lPassword])
                game.user = user
                text = "Welcome to the game %s" % game.user.name
                game.displayStandings()
                game.displayOutput(text,'green4')
                rButton.Deactivate()
                lButton.Deactivate()
                logoutButton = Buttons(win,Point(330,615),120,50,"LOGOUT"); logoutButton.Activate()
                if game.user.user_type == "admin":
                    """Submit new fixture"""
                    game.clearInputBox()
                    nGame,nextButton,fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,\
                       uresult,ucfcScorers,uoppositionScorers,submitFButton,updateFButton  = game.fixtureInputBox() 
                    game.displayOutput("SUBMIT FIXTURE/UPDATE RESULTS/SET NEXT FIXTURE; Time: format = dd/mm/yyyy 00:00;\
                    *Scorers: list. eg. [2, 3, 4]; Player# 0 if own-goal won",'grey2')

                else:
                    """Display prediction input fields and buttons"""
                    game.clearInputBox()
                    game_num,result,scoreline,cfcScorers,oppositionScorers,submitPButton = game.predictionInputBox()
            
                    game.displayOutput("SUBMIT/UPDATE A PREDICTION; Result:(win, tie or loss) enter integer 1, 0 or -1;\
                    Scoreline: enter list [#cfcGoals, #oppoGoals]; ;\
                    *Scorers: E.g [2, 3, 4], Player# 0 if own-goal won ",'grey2')

            else: #Username already exists
                game.displayOutput("***ERROR!: Username exists in registry!; Please re-try or login!",'red')
                
            pt = win.getMouse()

        #_______User Login________#
        elif lButton.Clicked(pt):
            """Register user"""
            credentials = [lUsername.getText(),lPassword.getText()]
            user = game.registry.authenticate(lUsername.getText(),lPassword.getText())
            if any(item=='' for item in credentials):
                game.displayOutput("***ERROR!: Some fields are empty!; Please re-try!",'red')
            elif user:
                game.clearInputBox([rName,rUsername,rPassword1,rPassword2,lUsername,lPassword])
                game.user = user
                text = "It's good to see you again,%s" % game.user.name
                game.displayOutput(text,'green4')
                game.displayPredictions()
                rButton.Deactivate()
                lButton.Deactivate()
                logoutButton = Buttons(win,Point(330,615),120,50,"LOGOUT"); logoutButton.Activate()
                if game.user.user_type == "admin":
                    """Submit new fixture"""
                    game.clearInputBox()
                    nGame,nextButton,fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,\
                       uresult,ucfcScorers,uoppositionScorers,submitFButton,updateFButton  = game.fixtureInputBox() 
                    game.displayOutput("SUBMIT FIXTURE/UPDATE RESULTS/SET NEXT FIXTURE; Time: format = dd/mm/yyyy 00:00;\
                    *Scorers: E.g [2, 3, 4], Player# 0 if own-goal won ",'grey2')

                else:
                    """Display prediction input fields and buttons"""
                    game.clearInputBox()
                    game_num,result,scoreline,cfcScorers,oppositionScorers,submitPButton = game.predictionInputBox()
            
                    game.displayOutput("SUBMIT/UPDATE A PREDICTION; Result:(win, tie or loss) enter integer 1, 0 or -1;\
                    Scoreline: enter list [#cfcGoals, #oppoGoals];*Scorers: E.g [2, 3, 4], Player# 0 for an own-goal won",'grey2')
                
            else:
                game.displayOutput("***ERROR!: Incorrect username or password!; Please re-try!",'red')
                
            pt = win.getMouse()

        #________User logout________#
        elif logoutButton.Clicked(pt):
            """Logs user out"""
            logoutButton.Deactivate()
            game.user = None
            game.clearInputBox([nGame,rName,rUsername,rPassword1,rPassword2,lUsername,lPassword,game_num,result,scoreline,cfcScorers,\
            oppositionScorers,fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,uresult,ucfcScorers,uoppositionScorers])
            updateFButton.Deactivate()
            submitFButton.Deactivate()
            nextButton.Deactivate()
            game.displayPredictions()
            game.displayOutput("REGISTER/LOGIN!; Hello!. Welcome to Chelsea FC Score Prediction Game!;\
            To get started:; Register a new account or Login to an existing account",'grey2')
            rName,rUsername,rPassword1,rPassword2,lUsername,lPassword,rButton,lButton = game.userInputBox()

            pt = win.getMouse()

        #_______Saves a new fixture to the schedule_______#
        elif submitFButton.Clicked(pt):
            """Process new prediction"""
            fields = [fgame.getText(),fopponent.getText(),ftime.getText(),fvenue.getText(),fresult.getText(),\
                      fcfcScorers.getText(),foppositionScorers.getText()]
            if any(item=='' for item in fields):
                game.displayOutput("***ERROR!: Some fields are empty!; Please re-try!",'red')
            else:
                fields = [eval(fgame.getText()),fopponent.getText(),ftime.getText(),fvenue.getText(),fresult.getText(),\
                      fcfcScorers.getText(),foppositionScorers.getText()]
                fixture = Fixture(fields[0],fields[1],fields[2],fields[3],fields[4],fields[5],fields[6])
                game.schedule.addFixture(fixture)
                game.clearInputBox([fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,\
               uresult,ucfcScorers,uoppositionScorers,nGame])
                text = "Fixture submitted for game number %s" % str(fields[0])
                game.displayOutput(text,'green4')
                game.schedule.exportFixtures()
                game.displaySchedule()
                logoutButton.Activate()
                nGame,nextButton,fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,\
                       uresult,ucfcScorers,oppositionScorers,submitFButton,updateFButton  = game.fixtureInputBox() 
                game.displayOutput(text,'green4')
                
            pt = win.getMouse()

        #_______Updates results for an existing fixture & applies the result to predictions________#
        elif updateFButton.Clicked(pt):
            """Process new result"""
            fields = [ugame.getText(),uresult.getText(),ucfcScorers.getText(),uoppositionScorers.getText()]
            if any(item=='' for item in fields): 
                game.displayOutput("***ERROR!: Some fields are empty!; Please re-try!",'red')

            elif game.schedule.getFixture(eval(fields[0])):
                game.schedule.importFixtures()
                fields = [ugame.getText(),uresult.getText(),ucfcScorers.getText(),uoppositionScorers.getText()]
                fixture = game.schedule.getFixture(eval(fields[0]))
                uFixture = Fixture(eval(fields[0]),fixture.opponent,fixture.time,fixture.venue,fields[1],fields[2],fields[3])
                game.schedule.addFixture(uFixture)

                game.clearInputBox([fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,\
               uresult,ucfcScorers,uoppositionScorers,nGame])
                
                text,color = "Fixture updated for game number %s" % fields[0],'green4'
                game.displayOutput(text,color)
                
                game.displaySchedule()
                game.schedule.exportFixtures()
                game.pDB.applyResult(game.schedule.getFixture(eval(fields[0])),game.registry)
                game.displayStandings()
                logoutButton.Activate()
                updateFButton.Deactivate()
                submitFButton.Deactivate()
                nGame,nextButton,fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,\
                       uresult,ucfcScorers,oppositionScorers,submitFButton,updateFButton  = game.fixtureInputBox() 
                game.displayOutput(text,color)
            else:
                text,color = "Could not locate a fixture with game number %s" % fields[0],'red'
                game.displayOutput(text,color)
                
            pt = win.getMouse()

        #______Sets next fixture in the schedule______#
        elif nextButton.Clicked(pt):
            """Process apply new next game #"""
            if nGame.getText()=='': 
                game.displayOutput("***ERROR!: Next Game # not entered!; Please re-try!",'red')

            else:
                game.schedule.importFixtures()
                game.schedule.setNext(eval(nGame.getText()))

                game.clearInputBox([fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,\
               uresult,ucfcScorers,uoppositionScorers,nGame])
                
                text,color = "Next fixture is set to %s" % nGame.getText(),'green4'
                game.displayOutput(text,color)
                
                game.displaySchedule()
                game.displayPredictions()
                game.schedule.exportFixtures()
                logoutButton.Activate()
                updateFButton.Deactivate()
                submitFButton.Deactivate()
                nextButton.Deactivate()
                nGame,nextButton,fgame,fopponent,ftime,fvenue,fresult,fcfcScorers,foppositionScorers,ugame,\
                       uresult,ucfcScorers,oppositionScorers,submitFButton,updateFButton  = game.fixtureInputBox() 
                game.displayOutput(text,color)
                
            pt = win.getMouse()

        #______Saves a new prediction to the database_______#
        elif submitPButton.Clicked(pt):
            """Process new prediction"""
            fields = [game_num.getText(),result.getText(),scoreline.getText(),cfcScorers.getText(),oppositionScorers.getText()]
            if any(item=='' for item in fields):
                game.displayOutput("***ERROR!: Some fields are empty!; Please re-try!",'red')
            else:
                fields = [eval(game_num.getText()),eval(result.getText()),scoreline.getText(),cfcScorers.getText(),oppositionScorers.getText()]
                prediction = Prediction(game.user.username,fields[0],fields[1],fields[2],fields[3],fields[4])
                game.pDB.submitPrediction(prediction)
                game.clearInputBox([game_num,result,scoreline,cfcScorers,oppositionScorers])
                text = "Prediction updated for game number %s" % str(fields[0])
                game.displayOutput(text,'green4')
                game.displayPredictions()
                submitPButton.Deactivate()
                logoutButton = Buttons(win,Point(330,615),120,50,"LOGOUT"); logoutButton.Activate()
                game_num,result,scoreline,cfcScorers,oppositionScorers,submitPButton = game.predictionInputBox()
            
                game.displayOutput(text,'green4')
            pt = win.getMouse()
            
    #_______Saves storage files and exists the game_____#    
    game.quitGame()
    win.close()

main()
