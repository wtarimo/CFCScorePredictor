"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
Registrar Class: Manages a database of users
11/30/2012
"""
from User import *

class Registrar(object):
    """Implements a registrar class that manages user accounts"""
    def __init__(self,users=[]):
        self.users = users
        self.userCount = len(self.users)
        self.importUsers()

    def register(self,new_user):
        """Registers a new user to the registry"""
        for user in self.users:
            if user.username == new_user.username:
                return False #username already exists in the database
        self.users.append(new_user)
        self.userCount+=1
        return True

    def authenticate(self,username,password):
        """Authenticates user credentials"""
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return False #Wrong password or username
    
    def getUser(self,username):
        """Returns a user whose username is the parameter"""
        for user in self.users:
            if user.username == username:
                return user
        return False
            
    def getStandings(self):
        """Returns a list of name,points,accuracy sorted by points in descending order"""
        standings = []
        for user in self.users:
            if user.user_type != 'admin':
                standings.append([user.username,user.points,user.accuracy])
        return sorted(standings,key=lambda x: x[1],reverse=True)

    def importUsers(self):
        """Loads user accounts from users.txt in an instance of the registrar"""
        lines = open("users.txt")
        while True:
            line = lines.readline()[:-1]
            if line=="": break
            fields = line.split("|")
            user = User(fields[0],fields[1],fields[2],fields[3],int(fields[4]),float(fields[5]))
            self.register(user)

    def exportUsers(self):
        """Saves all user user accounts to users.txt"""
        out = open("users.txt","w")
        users = [u.name+"|"+u.username+"|"+u.password+"|"+u.user_type+"|"+str(u.points)+"|"+str(u.accuracy) for u in self.users]
        out.writelines("%s\n" % user for user in users)
        out.close()
        
            

    
