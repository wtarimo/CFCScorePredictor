CFCScorePredictor
=================

A Python based game for soccer scores prediction for Chelsea FC!

This game allows Chelsea FC fans on campus to predict results for Chelsea FC games. 
On each Chelsea match, participating fans can predict the game result (win, loss or tie), 
the score-line, and goal scorers from both teams. 
Fans will be ranked according to cumulative prediction points, 
accuracy % can be used to break a tie in points. 
A manager or admin will always post fixtures and game results together with l
etting the system calculate points for each submitted prediction on the game results. 
This idea suits a website with database, however I’m going to create a Python 
implementation of it with local text files for information storage and retrieval. 

General Rules:

1.Predictions can be made for all upcoming Chelsea FC games in the Barclays Premier League, 
  UEFA Champions League, FA Cup and Carling Cup in the season.
2.* Prediction stops 5 minutes before game kick-off, the admin or manager handles this part.
3.Predictions are for the normal 90 minutes soccer game, scores from extra time are not included. 
4.Points: Correct result - 1pt, Exact score-line - 5pts, Each correct goal scorer - 1pt 
5.The upcoming fixture is displayed in green, past fixtures in red, and future fixtures in blue

Design:

1. Data storage text files for user accounts, predictions and fixture schedule
2. Game class - creates and manages instances of a game.
   Prediction class - creates and implements prediction instances of a soccer game.
   PredictionDatabase class - manages and manipulates predictions
   User class - creates and implements instances user accounts
   Registrar class - manages and manipulates user accounts
   Fixture class - creates and implements a game fixture/event
   Schedule class - manages and manipulates fixtures
   Button class - implements and minipulates graphical buttons

3. GUI - This game is entirely played in nice and simple graphical interface.
   Throughout the game, a user or admin is provided with appropriate buttons, input fields and
   displayed information areas, covering all the actions and instructions of a game play.

HowToPlay:

The game interface is filled with dynamic information on the game state, all the displayed information
is customized for session user and also updated after each user action.
1. Launch the game by running play.py
2. REGISTRATION/LOGIN: When the game starts the user can login to an existing account
  or create a new account. Only regular accounts can be created through the interface. Admins are pre-registered.
3. SUBMIT/UPDATE A PREDICTION: A regular user is only allowed to submit new predictions or update existing ones.
4. SUBMIT FIXTURE/UPDATE RESULTS: If a user an admin/manager, options for submitting fixtures, results and set 
  next fixture number are given.
5. Input formats: Input instructions and feedback are given on each page. 
   For fields that require lists, make sure to enter input with square brackets with items comma-separated with spaces
   between items. Examples: [], [1, 2], [1, 2, 4, 10]