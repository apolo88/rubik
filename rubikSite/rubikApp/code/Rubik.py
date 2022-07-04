import sys
from random import randrange

class Rubik:
    
    #Dimension of the Rubik Cube
    dim = None

    #Properties to store the cube, one matrix per layer and references to pieces
    layersMap = None
    cornersMap = None
    oppositeColourMap = None
    oppositeCornersMap = None
    solved = None

    def __init__(self):
        self.oppositeColourMap = {'G':'B','B':'G','Y':'W','W':'Y','O':'R','R':'O'}
        self.oppositeCornersMap = {'FUL':'FDL','FUR':'FDR','FDL':'FUL','FDR':'FUR','BUL':'BDL','BUR':'BDR','BDL':'BUL','BDR':'BUR'}
        self.solved = False

    #Create and fill the rubik
    def initCube(self):
        pass
    
    #Movement methods
    def moveFront(self):
        pass

    def moveFrontP(self):
        pass

    def moveBack(self):
        pass

    def moveBackP(self):
        pass
    
    def moveUp(self):
        pass

    def moveUpP(self):
        pass
    
    def moveDown(self):
        pass
        
    def moveDownP(self):
        pass
    
    def moveLeft(self):
        pass

    def moveLeftP(self):
        pass

    def moveRight(self):
        pass        

    def moveRightP(self):
        pass


    #Disorder Method
    def disorder(self, complexity):
        
        numOfMovements = None
        if complexity == 'Simple':
            numOfMovements = 10
        elif complexity == 'Medium':
            numOfMovements = 25
        elif complexity == 'Hard':
            numOfMovements = 50

        for i in range(numOfMovements):
            randNumber = randrange(13)
            if randNumber == 1:
                self.moveFront()
            elif randNumber == 2:
                self.moveFrontP()
            elif randNumber == 3:
                self.moveBack()
            elif randNumber == 4:
                self.moveBackP()
            elif randNumber == 5:
                self.moveUp()
            elif randNumber == 6:
                self.moveUpP()
            elif randNumber == 7:
                self.moveDown()
            elif randNumber == 8:
                self.moveDownP()
            elif randNumber == 9:
                self.moveLeft()
            elif randNumber == 10:
                self.moveLeftP()
            elif randNumber == 11:
                self.moveRight()
            elif randNumber == 12:
                self.moveRightP()


    #Solve Method
    def solve(self, mode):
        print('Solve will come soon')
        pass

    #Output Methods
    def printCube(self):
        self.printCubeFront()
        print('\n')
        self.printCubeBack()

    def printCubeFront(self):
        pass
    
    def printCubeBack(self):
        pass