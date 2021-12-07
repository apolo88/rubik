import sys
from Rubik import *

class Corner:

    pieceId = None
    coordsByLayer = None

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
            coloursSet.append(self.getColour(layersMap, layer))

        return coloursSet



class Rubik2x2(Rubik):
    

    def __init__(self):
        self.dim = 2

    #Create and fill the rubik
    def initCube(self):
        self.layersMap['F'] = [['G' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['B'] = [['B' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['U'] = [['Y' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['D'] = [['W' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['L'] = [['R' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['R'] = [['O' for y in range(self.dim)] for x in range(self.dim)]

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
        aux = self.front[0][0]
        self.front[0][0] = self.front[1][0]
        self.front[1][0] = self.front[1][1]
        self.front[1][1] = self.front[0][1]
        self.front[0][1] = aux

        #Rotation of mid half layers
        aux = self.up[1][0]
        self.up[1][0] = self.left[1][1]
        self.left[1][1] = self.down[0][1]
        self.down[0][1] = self.right[0][0]
        self.right[0][0] = aux
        aux = self.up[1][1]
        self.up[1][1] = self.left[0][1]
        self.left[0][1] = self.down[0][0]
        self.down[0][0] = self.right[1][0]
        self.right[1][0] = aux


    def moveFrontP(self):
        #Rotation of front layer
        aux = self.front[0][0]
        self.front[0][0] = self.front[0][1]
        self.front[0][1] = self.front[1][1]
        self.front[1][1] = self.front[1][0]
        self.front[1][0] = aux

        #Rotation of mid half layers
        aux = self.up[1][0]
        self.up[1][0] = self.right[0][0]
        self.right[0][0] = self.down[0][1]
        self.down[0][1] = self.left[1][1]
        self.left[1][1] = aux
        aux = self.up[1][1]
        self.up[1][1] = self.right[1][0]
        self.right[1][0] = self.down[0][0]
        self.down[0][0] = self.left[0][1]
        self.left[0][1] = aux

    
    def moveBack(self):
        #Rotation of back layer
        aux = self.back[0][0]
        self.back[0][0] = self.back[1][0]
        self.back[1][0] = self.back[1][1]
        self.back[1][1] = self.back[0][1]
        self.back[0][1] = aux

        #Rotation of mid half layers
        aux = self.up[0][1]
        self.up[0][1] = self.right[1][1]
        self.right[1][1] = self.down[1][0]
        self.down[1][0] = self.left[0][0]
        self.left[0][0] = aux
        aux = self.up[0][0]
        self.up[0][0] = self.right[0][1]
        self.right[0][1] = self.down[1][1]
        self.down[1][1] = self.left[1][0]
        self.left[1][0] = aux


    def moveBackP(self):
        #Rotation of back layer
        aux = self.back[0][0]
        self.back[0][0] = self.back[0][1]
        self.back[0][1] = self.back[1][1]
        self.back[1][1] = self.back[1][0]
        self.back[1][0] = aux

        #Rotation of mid half layers
        aux = self.up[0][1]
        self.up[0][1] = self.left[0][0]
        self.left[0][0] = self.down[1][0]
        self.down[1][0] = self.right[1][1]
        self.right[1][1] = aux
        aux = self.up[0][0]
        self.up[0][0] = self.left[1][0]
        self.left[1][0] = self.down[1][1]
        self.down[1][1] = self.right[0][1]
        self.right[0][1] = aux


    def moveUp(self):
        #Rotation of up layer
        aux = self.up[0][0]
        self.up[0][0] = self.up[1][0]
        self.up[1][0] = self.up[1][1]
        self.up[1][1] = self.up[0][1]
        self.up[0][1] = aux

        #Rotation of mid half layers
        aux = self.front[0][0]
        self.front[0][0] = self.right[0][0]
        self.right[0][0] = self.back[0][0]
        self.back[0][0] = self.left[0][0]
        self.left[0][0] = aux
        aux = self.front[0][1]
        self.front[0][1] = self.right[0][1]
        self.right[0][1] = self.back[0][1]
        self.back[0][1] = self.left[0][1]
        self.left[0][1] = aux


    def moveUpP(self):
        #Rotation of up layer
        aux = self.up[0][0]
        self.up[0][0] = self.up[0][1]
        self.up[0][1] = self.up[1][1]
        self.up[1][1] = self.up[1][0]
        self.up[1][0] = aux

        #Rotation of mid half layers
        aux = self.front[0][0]
        self.front[0][0] = self.left[0][0]
        self.left[0][0] = self.back[0][0]
        self.back[0][0] = self.right[0][0]
        self.right[0][0] = aux
        aux = self.front[0][1]
        self.front[0][1] = self.left[0][1]
        self.left[0][1] = self.back[0][1]
        self.back[0][1] = self.right[0][1]
        self.right[0][1] = aux

    
    def moveDown(self):
        #Rotation of down layer
        aux = self.down[0][0]
        self.down[0][0] = self.down[1][0]
        self.down[1][0] = self.down[1][1]
        self.down[1][1] = self.down[0][1]
        self.down[0][1] = aux

        #Rotation of mid half layers
        aux = self.front[1][0]
        self.front[1][0] = self.left[1][0]
        self.left[1][0] = self.back[1][0]
        self.back[1][0] = self.right[1][0]
        self.right[1][0] = aux
        aux = self.front[1][1]
        self.front[1][1] = self.left[1][1]
        self.left[1][1] = self.back[1][1]
        self.back[1][1] = self.right[1][1]
        self.right[1][1] = aux
        

    def moveDownP(self):
        #Rotation of down layer
        aux = self.down[0][0]
        self.down[0][0] = self.down[0][1]
        self.down[0][1] = self.down[1][1]
        self.down[1][1] = self.down[1][0]
        self.down[1][0] = aux

        #Rotation of mid half layers
        aux = self.front[1][0]
        self.front[1][0] = self.right[1][0]
        self.right[1][0] = self.back[1][0]
        self.back[1][0] = self.left[1][0]
        self.left[1][0] = aux
        aux = self.front[1][1]
        self.front[1][1] = self.right[1][1]
        self.right[1][1] = self.back[1][1]
        self.back[1][1] = self.left[1][1]
        self.left[1][1] = aux

        
    def moveLeft(self):
        #Rotation of left layer
        aux = self.left[0][0]
        self.left[0][0] = self.left[1][0]
        self.left[1][0] = self.left[1][1]
        self.left[1][1] = self.left[0][1]
        self.left[0][1] = aux

        #Rotation of mid half layers
        aux = self.up[0][0]
        self.up[0][0] = self.back[1][1]
        self.back[1][1] = self.down[0][0]
        self.down[0][0] = self.front[0][0]
        self.front[0][0] = aux
        aux = self.up[1][0]
        self.up[1][0] = self.back[0][1]
        self.back[0][1] = self.down[1][0]
        self.down[1][0] = self.front[1][0]
        self.front[1][0] = aux


    def moveLeftP(self):
        #Rotation of left layer
        aux = self.left[0][0]
        self.left[0][0] = self.left[0][1]
        self.left[0][1] = self.left[1][1]
        self.left[1][1] = self.left[1][0]
        self.left[1][0] = aux

        #Rotation of mid half layers
        aux = self.up[0][0]
        self.up[0][0] = self.front[0][0]  
        self.front[0][0] = self.down[0][0]
        self.down[0][0] = self.back[1][1]
        self.back[1][1] = aux
        aux = self.up[1][0]
        self.up[1][0] = self.front[1][0]
        self.front[1][0] = self.down[1][0]
        self.down[1][0] = self.back[0][1]
        self.back[0][1] = aux


    def moveRight(self):
        #Rotation of right layer
        aux = self.right[0][0]
        self.right[0][0] = self.right[1][0]
        self.right[1][0] = self.right[1][1]
        self.right[1][1] = self.right[0][1]
        self.right[0][1] = aux

        #Rotation of mid half layers
        aux = self.up[1][1]
        self.up[1][1] = self.front[1][1]
        self.front[1][1] = self.down[1][1]
        self.down[1][1] = self.back[0][0]
        self.back[0][0] = aux
        aux = self.up[0][1]
        self.up[0][1] = self.front[0][1]
        self.front[0][1] = self.down[0][1]
        self.down[0][1] = self.back[1][0]
        self.back[1][0] = aux


    def moveRightP(self):
        #Rotation of right layer
        aux = self.right[0][0]
        self.right[0][0] = self.right[0][1]
        self.right[0][1] = self.right[1][1]
        self.right[1][1] = self.right[1][0]
        self.right[1][0] = aux

        #Rotation of mid half layers
        aux = self.up[1][1]
        self.up[1][1] = self.back[0][0]  
        self.back[0][0] = self.down[1][1]
        self.down[1][1] = self.front[1][1]
        self.front[1][1] = aux
        aux = self.up[0][1]
        self.up[0][1] = self.back[1][0]
        self.back[1][0] = self.down[0][1]
        self.down[0][1] = self.front[0][1]
        self.front[0][1] = aux
    

    ####################
    ### SOLUTION METHODS
    ####################
    def solve(self, mode):

        #Solve down floor
        self.solveDownFloor()

        #Match one top corner

        #Position rest of the corners

        #Rotate top corners

        #Final Alignment cube


    def solveDownFloor(self):
        
        excludedPieceIds = set()
        
        #Iterate 3 times to position the 3 pieces
        for i in range(3):
            #Identify first position in down layer and get colours
            firstCornerDown = self.piecesMap['FDL']
            excludedPieceIds.append(firstCornerDown)
            downColour = firstCornerDown.getColour(self.layersMap, 'D')
            frontColour = firstCornerDown.getColour(self.layersMap, 'F')
            
            #Find piece that should go on the right sending colours to be find and exclusion of the current piece
            pieceIdFound = self.findPiece(set(downColor, frontColour), excludedPieceIds)
            cornerPiece = self.piecesMap[pieceIdFound]

            #Place piece on correct position
            self.placeCornerToDown(cornerPiece, downColour)

            #rotate cube vertical
            self.fullRotateVertical()


    def findPiece(self, colours, exceptions) -> str:
        for pieceId, piece in piecesMap:
            if not pieceId in exceptions:
                pieceColoursSet = piece.getColoursSet()
                if colours in pieceColoursSet:
                    return pieceId


    def placeCornerToDown(self, piece, targetColour):

        #Take Piece to FUR
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
                self.moveRight()
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

        #Take the piece to the floor:
        if piece.getColour(self.layersMap, 'F') == targetColour:
            self.moveCornerAlgo()
        elif piece.getColour(self.layersMap, 'U') == targetColour:
            for i in range(3):
                self.moveCornerAlgo()
        elif piece.getColour(self.layersMap, 'R') == targetColour:
            for i in range(5):
                self.moveCornerAlgo()
       
            
    def moveCornerAlgo(self):
        self.moveUp()
        self.moveRight()
        self.moveUpP()
        self.moveRightP()

    ##################
    ### OUTPUT METHODS
    ##################
    def printCubeFront(self):
        result = 'FRONT'
        result += '\n'
        result += '\n'

        result += ' ' + self.up[0][0]
        result += self.up[0][1]
        result += '\n'
        result += self.up[1][0]
        result += self.up[1][1]
        result += ' ' + self.right[0][1]
        result += '\n'

        result += self.front[0][0]
        result += self.front[0][1]
        result += self.right[0][0]
        result += self.right[1][1]
        result += '\n'
        result += self.front[1][0]
        result += self.front[1][1]
        result += self.right[1][0]

        print(result)

    
    def printCubeBack(self):
        result = 'BACK'
        result += '\n'
        result += '\n'

        result += self.back[0][0]
        result += self.back[0][1]
        result += self.left[0][0]
        result += '\n'
        result += self.back[1][0]
        result += self.back[1][1]
        result += self.left[1][0]
        result += self.left[0][1]
        result += '\n'

        result += self.down[1][1]
        result += self.down[1][0]
        result += ' ' + self.left[1][1]
        result += '\n'

        result += ' ' + self.down[0][1]
        result += self.down[0][0]

        print(result)