"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
User Class: Implements a user class
11/30/2012
"""

class User(object):
    """Implements user account class"""
    def __init__(self,name,username,password,user_type="user",points=0,accuracy=0.0):
        self.name = name
        self.username = username
        self.user_type = user_type
        self.password = password
        self.points = points
        self.accuracy = accuracy

    def updatePoints(self,points):
        """Increments user's accumulative points"""
        self.points+=points

    def updateAccuracy(self,accuracy):
        """Sets user's accurary to a new average"""
        if self.accuracy==0.0:
            self.accuracy = accuracy
        else:
            self.accuracy = int((self.accuracy+accuracy)/2.0)
        
