import os, sys

def my_function(x, y) :
    print (x,y)

class MyClass:
    def __init__(self, value):
        self.value=value

    def method(self):
        if self.value>0:
            print ("Positive")
        else:
            print ("Non-positive")

def another_function(  ):
    print("This is another function")