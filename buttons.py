"""
William Tarimo
COSI 157 - Final Project: CFC Score Predictor
Implements graphical buttons
11/11/2012
"""

from graphics import *

class Buttons:
    """Constructor takes in window, center point of button, its width and height and a button label as parameters"""
    def __init__(self, win, center, width, height, label):

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.Deactivate() #each created button is deactivated by default

    def getLabel(self):
        """Returns the label string of a button"""
        return self.label.getText()

    def Activate(self):
        """Sets a button active"""
        self.label.setFill('black')
        self.rect.setFill('green1')
        self.rect.setWidth(2)
        self.active = True

    def Deactivate(self):
        """Sets a button inactive"""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.rect.setFill('red1')
        self.active = False

    def Clicked(self, p):
        """This method returns true if button is active and p is inside"""
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax
