"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
PredictionsDatabase Class: Implements and manages a database of user predictions
11/30/2012
"""
from Prediction import *

class PredictionsDatabase(object):
    """Implements and manages a database of user predictions"""
    def __init__(self,predictions=[]):
        self.predictions = predictions
        self.predictionCount = len(self.predictions)
        self.importPredictions()

    def submitPrediction(self,new_prediction):
        """Saves a new prediction or updates an existing one"""
        prediction = self.getPrediction(new_prediction.game,new_prediction.user)
        if prediction:
            prediction.result = new_prediction.result
            prediction.scoreline = new_prediction.scoreline
            prediction.cfcScorers = new_prediction.cfcScorers
            prediction.oppositionScorers = new_prediction.oppositionScorers 
        else:
            self.predictions.append(new_prediction)
            self.predictionCount+=1
        self.predictions = sorted(self.predictions,key=lambda p: p.game,reverse=True)

    def getPrediction(self,game,username):
        """Returns a prediction user's prediction on that game if it exists"""
        for prediction in self.predictions:
            if prediction.game==game and prediction.user==username: return prediction
        return False
                
    def getPredictions(self,username):
        """Returns all predictions by the user"""
        return [p for p in self.predictions if p.user == username]

    def applyResult(self,result,registry):
        """Calculates and updates points earned to all predictions made on a particular game
        based on the given fixture result"""
        for prediction in self.predictions:
            if prediction.game == result.game:
                points,accuracy = prediction.calculatePoints(result)
                prediction.updatePoints(points)
                registry.getUser(prediction.user).updatePoints(points)
                registry.getUser(prediction.user).updateAccuracy(accuracy)
                
    def importPredictions(self):
        """Loads submitted predictions from predictions.txt"""
        lines = open("predictions.txt")
        while True:
            line = lines.readline()[:-1]
            if line=="": break
            fields = line.split("|")
            prediction = Prediction(fields[0],int(fields[1]),int(fields[2]),fields[3],fields[4],fields[5],int(fields[6]))
            self.submitPrediction(prediction)

    def exportPredictions(self):
        """Exports predictions in the databse to predictions.txt"""
        out = open("predictions.txt","w")
        predictions = [p.user+"|"+str(p.game)+"|"+str(p.result)+"|"+str(p.scoreline)+"|"+str(p.cfcScorers)+"|"+str(p.oppositionScorers)+"|"+str(p.points) for p in self.predictions]
        out.writelines("%s\n" % prediction for prediction in predictions)
        out.close()
