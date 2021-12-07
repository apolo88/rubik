import sys
from Rubik import *

class Corner:

    pieceId = None
    coordsByLayer = None
    test = None

    def __init__(self, pieceId, coordsByLayer):
        self.pieceId = pieceId
        self.coordsByLayer = coordsByLayer

    def getColour(self, layersMap, layer):
        xCoord = self.coordsByLayer[layer][0]
        yCoord = self.coordsByLayer[layer][1]
        return layersMap[layer][xCoord][yCoord]

    def getColoursSet(self, layersMap):
        coloursSet = set()
        for layer in self.coordsByLayer:
            coloursSet.add(self.getColour(layersMap, layer))

        return coloursSet


class Rubik2x2(Rubik):

    def __init__(self):
        super().__init__()
        self.initCube()

    #Create and fill the rubik
    def initCube(self):
        self.dim = 2
        self.layersMap = {}
        self.layersMap['F'] = [['G' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['B'] = [['B' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['U'] = [['Y' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['D'] = [['W' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['L'] = [['R' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['R'] = [['O' for y in range(self.dim)] for x in range(self.dim)]

        self.piecesMap = {}
        self.piecesMap['FUL'] = Corner('FUL', {'F' : [0,0], 'U': [1,0], 'L': [0,1]})
        self.piecesMap['FUR'] = Corner('FUR', {'F' : [0,1], 'U': [1,1], 'R': [0,0]})
        self.piecesMap['FDL'] = Corner('FDL', {'F' : [1,0], 'D': [0,0], 'L': [1,1]})
        self.piecesMap['FDR'] = Corner('FDR', {'F' : [1,1], 'D': [0,1], 'R': [1,0]})
        self.piecesMap['BUL'] = Corner('BUL', {'B' : [0,1], 'U': [0,0], 'L': [0,0]})
        self.piecesMap['BUR'] = Corner('BUR', {'B' : [0,0], 'U': [0,1], 'R': [0,1]})
        self.piecesMap['BDL'] = Corner('BDL', {'B' : [1,1], 'D': [1,0], 'L': [1,0]})
        self.piecesMap['BDR'] = Corner('BDR', {'B' : [1,0], 'D': [1,1], 'R': [1,1]})

    ####################
    ### MOVEMENT METHODS
    ####################
    def moveFront(self):
        #Rotation of front layer
        aux = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = aux
        aux = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = aux


    def moveFrontP(self):
        #Rotation of front layer
        aux = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = aux
        aux = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = aux

    
    def moveBack(self):
        #Rotation of back layer
        aux = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = aux
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = aux


    def moveBackP(self):
        #Rotation of back layer
        aux = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = aux
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = aux


    def moveUp(self):
        #Rotation of up layer
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = aux

        #Rotation of mid half layers
        aux = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = aux
        aux = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = aux


    def moveUpP(self):
        #Rotation of up layer
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = aux
        aux = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = aux

    
    def moveDown(self):
        #Rotation of down layer
        aux = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = aux

        #Rotation of mid half layers
        aux = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = aux
        aux = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = aux
        

    def moveDownP(self):
        #Rotation of down layer
        aux = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = aux
        aux = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = aux

        
    def moveLeft(self):
        #Rotation of left layer
        aux = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = aux
        aux = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = aux


    def moveLeftP(self):
        #Rotation of left layer
        aux = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['F'][0][0]  
        self.layersMap['F'][0][0] = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = aux
        aux = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = aux


    def moveRight(self):
        #Rotation of right layer
        aux = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = aux
        aux = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = aux


    def moveRightP(self):
        #Rotation of right layer
        aux = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = self.layersMap['B'][0][0]  
        self.layersMap['B'][0][0] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = aux
        aux = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = aux
    

    ####################
    ### SOLUTION METHODS
    ####################
    def solve(self, mode):

        #Solve down floor
        self.solveDownFloor()

        #Match one top corner
        numOfPlacedTopPieces = self.prepareToSolveTopFloor()

        print('numOfCoincidencesOut: ' + str(numOfPlacedTopPieces))
        self.printCube()
        sys.stdin.read(1)

        if numOfPlacedTopPieces == 1:

            print('rotate corners')

            #Position rest of the corners
            self.rotateCorners()
        
        print('rotate each corner')
        sys.stdin.read(1)

        #Rotate top corners
        self.rotateEachCorner()

        #Final Alignment cube
        self.centerCube()

        print('final after center')
        self.printCube()
        sys.stdin.read(1)


    def solveDownFloor(self):
        
        #Iterate 3 times to position the 3 pieces
        for i in range(3):

            #print('Start solve debug pos: ' + str(i))
            #sys.stdin.read(1)

            #Identify first position in down layer and get colours
            firstCornerDown = self.piecesMap['FDL']
            downColour = firstCornerDown.getColour(self.layersMap, 'D')
            frontColour = firstCornerDown.getColour(self.layersMap, 'F')
            
            #print('downColour: ' + downColour)
            #print('frontColour: ' + frontColour)
            #sys.stdin.read(1)

            #Find piece that should go on the right sending colours to be find and exclusion of the current piece
            pieceIdFound = self.findPiece(set([downColour, frontColour]), set(['FDL']))
            
            #print('pieceIdFound: ' + pieceIdFound)
            #sys.stdin.read(1)
            
            cornerPiece = self.piecesMap[pieceIdFound]

            #Place piece on correct position
            self.placeCornerToDown(cornerPiece, downColour)

            #rotate cube vertical
            self.fullRotateVertical()

            print('print after rotate: ' + pieceIdFound)
            self.printCube()
            sys.stdin.read(1)


    def findPiece(self, colours, exceptions) -> str:
        for pieceId in self.piecesMap.keys():
            
            #print('pieceId: ' + pieceId)
            #sys.stdin.read(1)
            
            if not pieceId in exceptions:
                piece = self.piecesMap[pieceId]

                #print('piece Id: ' + piece.pieceId)
                #sys.stdin.read(1)

                pieceColoursSet = piece.getColoursSet(self.layersMap)

                #print('pieceColoursSet: ' + str(pieceColoursSet))
                #print('colours: ' + str(colours))
                #sys.stdin.read(1)

                if colours.issubset(pieceColoursSet):

                    #print('return piece Id: ' + pieceId)
                    #sys.stdin.read(1)

                    return pieceId


    def placeCornerToDown(self, piece, targetColour):

        #print('pieceId: ' + piece.pieceId)
        #sys.stdin.read(1)

        #Take the piece to FUR
        if piece.pieceId == 'FUL':
            self.moveUpP()
        elif piece.pieceId == 'FUR':
            pass #Target Position
        elif piece.pieceId == 'FDL':
            pass #Already Matched position
        elif piece.pieceId == 'FDR':
            if piece.getColour(self.layersMap, 'D') == targetColour:
                return #The piece is already in the correct position and rotation
            else:
                self.moveCornerAlgo()
        elif piece.pieceId == 'BUL':
            self.moveUp()
            self.moveUp()
        elif piece.pieceId == 'BUR':
            self.moveUp()
        elif piece.pieceId == 'BDL':
            self.moveBack()
            self.moveBack()
            self.moveRightP()
        elif piece.pieceId == 'BDR':
            self.moveRightP()
            self.moveRightP()

        #print('status before corner algo')
        #self.printCube()
        #sys.stdin.read(1)

        #Update piece instance after movements
        piece = self.piecesMap['FUR']

        #Take the piece to the floor:
        if piece.getColour(self.layersMap, 'F') == targetColour:
            self.moveCornerAlgo()
        elif piece.getColour(self.layersMap, 'U') == targetColour:
            for i in range(3):
                self.moveCornerAlgo()
        elif piece.getColour(self.layersMap, 'R') == targetColour:
            for i in range(5):
                self.moveCornerAlgo()

        #print('status after corner algo')
        #self.printCube()
        #sys.stdin.read(1)


    def moveCornerAlgo(self):
        self.moveUp()
        self.moveRight()
        self.moveUpP()
        self.moveRightP()


    def prepareToSolveTopFloor(self) -> int:
        expectedTopColour = self.getExpectedTopColour()

        print('expectedTopColour: ' + expectedTopColour)
        sys.stdin.read(1)

        numOfCoincidences = 0
        topPositions = ['FUL','FUR','BUL','BUR']
        
        iterationsWith2 = 0
        while True:
            for position in topPositions:
                topColourSet = self.piecesMap[position].getColoursSet(self.layersMap)
                topColourSet.remove(expectedTopColour);
                downColourSet = self.piecesMap[self.oppositeCornersMap[position]].getColoursSet(self.layersMap)

                if topColourSet.issubset(downColourSet):
                    numOfCoincidences = numOfCoincidences + 1

            print('numOfCoincidencesIn: ' + str(numOfCoincidences))
            sys.stdin.read(1)

            if numOfCoincidences != 1 and numOfCoincidences != 4:
                if numOfCoincidences == 2:
                    iterationsWith2 = iterationsWith2 + 1
                    if iterationsWith2 > 2:
                        iterationsWith2 = 0

                        self.moveLeftP()
                        self.moveUp()
                        self.moveRight()
                        self.moveUpP()
                        self.moveLeft()
                        self.moveUp()
                        self.moveRightP()
                        self.moveUpP()                        

                self.moveUp()
                numOfCoincidences = 0
            else:
                break

        return numOfCoincidences


    def getExpectedTopColour(self):
        return self.oppositeColourMap[self.layersMap['D'][0][0]]

    def getExpectedFrontColour(self):
        return self.oppositeColourMap[self.layersMap['B'][1][1]]

    def rotateCorners(self):
        expectedTopColour = self.getExpectedTopColour()
        rotateClockSide = None

        print('rotate corners in')

        while True:
            topColourSet = self.piecesMap['FUR'].getColoursSet(self.layersMap)
            topColourSet.remove(expectedTopColour);
            downColourSet = self.piecesMap[self.oppositeCornersMap['FUR']].getColoursSet(self.layersMap)

            print('que paso')

            if not topColourSet.issubset(downColourSet):
                print('rotate looking match corner');
                self.printCube()
                sys.stdin.read(1)
                
                self.fullRotateVertical()
                continue
            else:
                print('else rotate')
                topColourSet = self.piecesMap['FUL'].getColoursSet(self.layersMap)
                topColourSet.remove(expectedTopColour);
                downColourSet = self.piecesMap[self.oppositeCornersMap['BUL']].getColoursSet(self.layersMap)

                print('topColourset: ' + str(topColourSet))
                print('downColourset: ' + str(downColourSet))
                if topColourSet.issubset(downColourSet):
                    rotateClockSide = True
                else:
                    rotateClockSide = False
                
                break
        
        print('rotateClockSide: ' + str(rotateClockSide));
        self.printCube()
        sys.stdin.read(1)

        if rotateClockSide:
            self.moveLeftP()
            self.moveUp()
            self.moveRight()
            self.moveUpP()
            self.moveLeft()
            self.moveUp()
            self.moveRightP()
            self.moveUpP()
        else:
            self.fullRotateVertical()
            self.moveRight()
            self.moveUpP()
            self.moveLeftP()
            self.moveUp()
            self.moveRightP()
            self.moveUpP()
            self.moveLeft()
            self.moveUp()

        print('rotateCornersEnd');
        self.printCube()
        sys.stdin.read(1)


    def rotateEachCorner(self):
        expectedTopColour = self.getExpectedTopColour()
        for i in range(4):
            topColour = self.layersMap['U'][1][1]

            print('topColour: ' + topColour);
            print('expectedTopColour: ' + expectedTopColour);
            
            if topColour != expectedTopColour:
                frontColour = self.layersMap['F'][0][1]
                if frontColour == expectedTopColour:
                    print('rotate clockside');
                    self.rotateCornerClockSide()
                else:
                    print('rotate anticlockside');
                    self.rotateCornerAntiClockSide()
            
            print('cube after rotate corner individually')
            self.printCube()
            sys.stdin.read(1)

            self.moveUp()

            print('cube after move up')
            self.printCube()
            sys.stdin.read(1)


    def rotateCornerClockSide(self):
        for i in range(2):
            self.moveRightP()
            self.moveDown()
            self.moveRight()
            self.moveDownP()


    def rotateCornerAntiClockSide(self):
        for i in range(2):
            self.moveDown()
            self.moveRightP()
            self.moveDownP()
            self.moveRight()


    def centerCube(self):
        expectedFrontColour = self.getExpectedFrontColour()
        while True:
            frontColour = self.layersMap['F'][0][0]
            if frontColour != expectedFrontColour:
                self.moveUp()
            else:
                break
        

    ##################
    ### OUTPUT METHODS
    ##################
    def printCubeFront(self):
        result = 'FRONT'
        result += '\n'
        result += '\n'

        result += ' ' + self.layersMap['U'][0][0]
        result += self.layersMap['U'][0][1]
        result += '\n'
        result += self.layersMap['U'][1][0]
        result += self.layersMap['U'][1][1]
        result += ' ' + self.layersMap['R'][0][1]
        result += '\n'

        result += self.layersMap['F'][0][0]
        result += self.layersMap['F'][0][1]
        result += self.layersMap['R'][0][0]
        result += self.layersMap['R'][1][1]
        result += '\n'
        result += self.layersMap['F'][1][0]
        result += self.layersMap['F'][1][1]
        result += self.layersMap['R'][1][0]

        print(result)

    
    def printCubeBack(self):
        result = 'BACK'
        result += '\n'
        result += '\n'

        result += self.layersMap['B'][0][0]
        result += self.layersMap['B'][0][1]
        result += self.layersMap['L'][0][0]
        result += '\n'
        result += self.layersMap['B'][1][0]
        result += self.layersMap['B'][1][1]
        result += self.layersMap['L'][1][0]
        result += self.layersMap['L'][0][1]
        result += '\n'

        result += self.layersMap['D'][1][1]
        result += self.layersMap['D'][1][0]
        result += ' ' + self.layersMap['L'][1][1]
        result += '\n'

        result += ' ' + self.layersMap['D'][0][1]
        result += self.layersMap['D'][0][0]

        print(result)