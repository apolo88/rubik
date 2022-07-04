import sys
from .Rubik import *

class Piece:

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
            coloursSet.add(self.getColour(layersMap, layer))

        return coloursSet


class Rubik3x3(Rubik):

    edgesMap = None

    def __init__(self):
        super().__init__()
        self.initCube()

    #Create and fill the rubik
    def initCube(self):
        self.dim = 3
        self.layersMap = {}
        self.layersMap['F'] = [['G' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['B'] = [['B' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['U'] = [['Y' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['D'] = [['W' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['L'] = [['R' for y in range(self.dim)] for x in range(self.dim)]
        self.layersMap['R'] = [['O' for y in range(self.dim)] for x in range(self.dim)]

        self.cornersMap = {}
        #Load into the map corner pieces
        self.cornersMap['FUL'] = Piece('FUL', {'F' : [0,0], 'U': [2,0], 'L': [0,2]})
        self.cornersMap['FUR'] = Piece('FUR', {'F' : [0,2], 'U': [2,2], 'R': [0,0]})
        self.cornersMap['FDL'] = Piece('FDL', {'F' : [2,0], 'D': [0,0], 'L': [2,2]})
        self.cornersMap['FDR'] = Piece('FDR', {'F' : [2,2], 'D': [0,2], 'R': [2,0]})
        self.cornersMap['BUL'] = Piece('BUL', {'B' : [0,2], 'U': [0,0], 'L': [0,0]})
        self.cornersMap['BUR'] = Piece('BUR', {'B' : [0,0], 'U': [0,2], 'R': [0,2]})
        self.cornersMap['BDL'] = Piece('BDL', {'B' : [2,2], 'D': [2,0], 'L': [2,0]})
        self.cornersMap['BDR'] = Piece('BDR', {'B' : [2,0], 'D': [2,2], 'R': [2,2]})
        
        self.edgesMap = {}
        #Load into the map edge pieces
        self.edgesMap['FU'] = Piece('FU', {'F' : [0,1], 'U': [2,1]})
        self.edgesMap['FD'] = Piece('FD', {'F' : [2,1], 'D': [0,1]})
        self.edgesMap['FL'] = Piece('FL', {'F' : [1,0], 'L': [1,2]})
        self.edgesMap['FR'] = Piece('FR', {'F' : [1,2], 'R': [1,0]})
        self.edgesMap['BU'] = Piece('BU', {'B' : [0,1], 'U': [0,1]})
        self.edgesMap['BD'] = Piece('BD', {'B' : [2,1], 'D': [2,1]})
        self.edgesMap['BL'] = Piece('BL', {'B' : [1,2], 'L': [1,0]})
        self.edgesMap['BR'] = Piece('BR', {'B' : [1,0], 'R': [1,2]})
        self.edgesMap['UL'] = Piece('UL', {'U' : [1,0], 'L': [0,1]})
        self.edgesMap['DL'] = Piece('DL', {'D' : [1,0], 'L': [2,1]})
        self.edgesMap['UR'] = Piece('UR', {'U' : [1,2], 'R': [0,1]})
        self.edgesMap['DR'] = Piece('DR', {'D' : [1,2], 'R': [2,1]})


    ####################
    ### MOVEMENT METHODS
    ####################
    def moveFront(self):
        #Rotation of front layer
        aux = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = self.layersMap['F'][2][0]
        self.layersMap['F'][2][0] = self.layersMap['F'][2][2]
        self.layersMap['F'][2][2] = self.layersMap['F'][0][2]
        self.layersMap['F'][0][2] = aux
        aux = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = self.layersMap['F'][2][1]
        self.layersMap['F'][2][1] = self.layersMap['F'][1][2]
        self.layersMap['F'][1][2] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][2][0]
        self.layersMap['U'][2][0] = self.layersMap['L'][2][2]
        self.layersMap['L'][2][2] = self.layersMap['D'][0][2]
        self.layersMap['D'][0][2] = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = aux
        aux = self.layersMap['U'][2][2]
        self.layersMap['U'][2][2] = self.layersMap['L'][0][2]
        self.layersMap['L'][0][2] = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['R'][2][0]
        self.layersMap['R'][2][0] = aux
        aux = self.layersMap['U'][2][1]
        self.layersMap['U'][2][1] = self.layersMap['L'][1][2]
        self.layersMap['L'][1][2] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = aux


    def moveFrontP(self):
        #Rotation of front layer
        aux = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = self.layersMap['F'][0][2]
        self.layersMap['F'][0][2] = self.layersMap['F'][2][2]
        self.layersMap['F'][2][2] = self.layersMap['F'][2][0]
        self.layersMap['F'][2][0] = aux
        aux = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['F'][1][2]
        self.layersMap['F'][1][2] = self.layersMap['F'][2][1]
        self.layersMap['F'][2][1] = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][2][0]
        self.layersMap['U'][2][0] = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = self.layersMap['D'][0][2]
        self.layersMap['D'][0][2] = self.layersMap['L'][2][2]
        self.layersMap['L'][2][2] = aux
        aux = self.layersMap['U'][2][2]
        self.layersMap['U'][2][2] = self.layersMap['R'][2][0]
        self.layersMap['R'][2][0] = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['L'][0][2]
        self.layersMap['L'][0][2] = aux
        aux = self.layersMap['U'][2][1]
        self.layersMap['U'][2][1] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['L'][1][2]
        self.layersMap['L'][1][2] = aux

    
    def moveBack(self):
        #Rotation of back layer
        aux = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = self.layersMap['B'][2][0]
        self.layersMap['B'][2][0] = self.layersMap['B'][2][2]
        self.layersMap['B'][2][2] = self.layersMap['B'][0][2]
        self.layersMap['B'][0][2] = aux
        aux = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = self.layersMap['B'][2][1]
        self.layersMap['B'][2][1] = self.layersMap['B'][1][2]
        self.layersMap['B'][1][2] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][0][2]
        self.layersMap['U'][0][2] = self.layersMap['R'][2][2]
        self.layersMap['R'][2][2] = self.layersMap['D'][2][0]
        self.layersMap['D'][2][0] = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = aux
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['R'][0][2]
        self.layersMap['R'][0][2] = self.layersMap['D'][2][2]
        self.layersMap['D'][2][2] = self.layersMap['L'][2][0]
        self.layersMap['L'][2][0] = aux
        aux = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['R'][1][2]
        self.layersMap['R'][1][2] = self.layersMap['D'][2][1]
        self.layersMap['D'][2][1] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = aux


    def moveBackP(self):
        #Rotation of back layer
        aux = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = self.layersMap['B'][0][2]
        self.layersMap['B'][0][2] = self.layersMap['B'][2][2]
        self.layersMap['B'][2][2] = self.layersMap['B'][2][0]
        self.layersMap['B'][2][0] = aux
        aux = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['B'][1][2]
        self.layersMap['B'][1][2] = self.layersMap['B'][2][1]
        self.layersMap['B'][2][1] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][0][2]
        self.layersMap['U'][0][2] = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = self.layersMap['D'][2][0]
        self.layersMap['D'][2][0] = self.layersMap['R'][2][2]
        self.layersMap['R'][2][2] = aux
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['L'][2][0]
        self.layersMap['L'][2][0] = self.layersMap['D'][2][2]
        self.layersMap['D'][2][2] = self.layersMap['R'][0][2]
        self.layersMap['R'][0][2] = aux
        aux = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = self.layersMap['D'][2][1]
        self.layersMap['D'][2][1] = self.layersMap['R'][1][2]
        self.layersMap['R'][1][2] = aux


    def moveUp(self):
        #Rotation of up layer
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['U'][2][0]
        self.layersMap['U'][2][0] = self.layersMap['U'][2][2]
        self.layersMap['U'][2][2] = self.layersMap['U'][0][2]
        self.layersMap['U'][0][2] = aux
        aux = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['U'][2][1]
        self.layersMap['U'][2][1] = self.layersMap['U'][1][2]
        self.layersMap['U'][1][2] = aux

        #Rotation of mid half layers
        aux = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = aux
        aux = self.layersMap['F'][0][2]
        self.layersMap['F'][0][2] = self.layersMap['R'][0][2]
        self.layersMap['R'][0][2] = self.layersMap['B'][0][2]
        self.layersMap['B'][0][2] = self.layersMap['L'][0][2]
        self.layersMap['L'][0][2] = aux
        aux = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = aux


    def moveUpP(self):
        #Rotation of up layer
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['U'][0][2]
        self.layersMap['U'][0][2] = self.layersMap['U'][2][2]
        self.layersMap['U'][2][2] = self.layersMap['U'][2][0]
        self.layersMap['U'][2][0] = aux
        aux = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['U'][1][2]
        self.layersMap['U'][1][2] = self.layersMap['U'][2][1]
        self.layersMap['U'][2][1] = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = aux
        aux = self.layersMap['F'][0][2]
        self.layersMap['F'][0][2] = self.layersMap['L'][0][2]
        self.layersMap['L'][0][2] = self.layersMap['B'][0][2]
        self.layersMap['B'][0][2] = self.layersMap['R'][0][2]
        self.layersMap['R'][0][2] = aux
        aux = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = aux

    
    def moveDown(self):
        #Rotation of down layer
        aux = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['D'][2][0]
        self.layersMap['D'][2][0] = self.layersMap['D'][2][2]
        self.layersMap['D'][2][2] = self.layersMap['D'][0][2]
        self.layersMap['D'][0][2] = aux
        aux = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['D'][2][1]
        self.layersMap['D'][2][1] = self.layersMap['D'][1][2]
        self.layersMap['D'][1][2] = aux

        #Rotation of mid half layers
        aux = self.layersMap['F'][2][0]
        self.layersMap['F'][2][0] = self.layersMap['L'][2][0]
        self.layersMap['L'][2][0] = self.layersMap['B'][2][0]
        self.layersMap['B'][2][0] = self.layersMap['R'][2][0]
        self.layersMap['R'][2][0] = aux
        aux = self.layersMap['F'][2][2]
        self.layersMap['F'][2][2] = self.layersMap['L'][2][2]
        self.layersMap['L'][2][2] = self.layersMap['B'][2][2]
        self.layersMap['B'][2][2] = self.layersMap['R'][2][2]
        self.layersMap['R'][2][2] = aux
        aux = self.layersMap['F'][2][1]
        self.layersMap['F'][2][1] = self.layersMap['L'][2][1]
        self.layersMap['L'][2][1] = self.layersMap['B'][2][1]
        self.layersMap['B'][2][1] = self.layersMap['R'][2][1]
        self.layersMap['R'][2][1] = aux
        

    def moveDownP(self):
        #Rotation of down layer
        aux = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['D'][0][2]
        self.layersMap['D'][0][2] = self.layersMap['D'][2][2]
        self.layersMap['D'][2][2] = self.layersMap['D'][2][0]
        self.layersMap['D'][2][0] = aux
        aux = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['D'][1][2]
        self.layersMap['D'][1][2] = self.layersMap['D'][2][1]
        self.layersMap['D'][2][1] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['F'][2][0]
        self.layersMap['F'][2][0] = self.layersMap['R'][2][0]
        self.layersMap['R'][2][0] = self.layersMap['B'][2][0]
        self.layersMap['B'][2][0] = self.layersMap['L'][2][0]
        self.layersMap['L'][2][0] = aux
        aux = self.layersMap['F'][2][2]
        self.layersMap['F'][2][2] = self.layersMap['R'][2][2]
        self.layersMap['R'][2][2] = self.layersMap['B'][2][2]
        self.layersMap['B'][2][2] = self.layersMap['L'][2][2]
        self.layersMap['L'][2][2] = aux
        aux = self.layersMap['F'][2][1]
        self.layersMap['F'][2][1] = self.layersMap['R'][2][1]
        self.layersMap['R'][2][1] = self.layersMap['B'][2][1]
        self.layersMap['B'][2][1] = self.layersMap['L'][2][1]
        self.layersMap['L'][2][1] = aux

        
    def moveLeft(self):
        #Rotation of left layer
        aux = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = self.layersMap['L'][2][0]
        self.layersMap['L'][2][0] = self.layersMap['L'][2][2]
        self.layersMap['L'][2][2] = self.layersMap['L'][0][2]
        self.layersMap['L'][0][2] = aux
        aux = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = self.layersMap['L'][2][1]
        self.layersMap['L'][2][1] = self.layersMap['L'][1][2]
        self.layersMap['L'][1][2] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['B'][2][2]
        self.layersMap['B'][2][2] = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['F'][0][0]
        self.layersMap['F'][0][0] = aux
        aux = self.layersMap['U'][2][0]
        self.layersMap['U'][2][0] = self.layersMap['B'][0][2]
        self.layersMap['B'][0][2] = self.layersMap['D'][2][0]
        self.layersMap['D'][2][0] = self.layersMap['F'][2][0]
        self.layersMap['F'][2][0] = aux
        aux = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['B'][1][2]
        self.layersMap['B'][1][2] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = aux


    def moveLeftP(self):
        #Rotation of left layer
        aux = self.layersMap['L'][0][0]
        self.layersMap['L'][0][0] = self.layersMap['L'][0][2]
        self.layersMap['L'][0][2] = self.layersMap['L'][2][2]
        self.layersMap['L'][2][2] = self.layersMap['L'][2][0]
        self.layersMap['L'][2][0] = aux
        aux = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = self.layersMap['L'][1][2]
        self.layersMap['L'][1][2] = self.layersMap['L'][2][1]
        self.layersMap['L'][2][1] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][0][0]
        self.layersMap['U'][0][0] = self.layersMap['F'][0][0]  
        self.layersMap['F'][0][0] = self.layersMap['D'][0][0]
        self.layersMap['D'][0][0] = self.layersMap['B'][2][2]
        self.layersMap['B'][2][2] = aux
        aux = self.layersMap['U'][2][0]
        self.layersMap['U'][2][0] = self.layersMap['F'][2][0]
        self.layersMap['F'][2][0] = self.layersMap['D'][2][0]
        self.layersMap['D'][2][0] = self.layersMap['B'][0][2]
        self.layersMap['B'][0][2] = aux
        aux = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['B'][1][2]
        self.layersMap['B'][1][2] = aux


    def moveRight(self):
        #Rotation of right layer
        aux = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = self.layersMap['R'][2][0]
        self.layersMap['R'][2][0] = self.layersMap['R'][2][2]
        self.layersMap['R'][2][2] = self.layersMap['R'][0][2]
        self.layersMap['R'][0][2] = aux
        aux = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = self.layersMap['R'][2][1]
        self.layersMap['R'][2][1] = self.layersMap['R'][1][2]
        self.layersMap['R'][1][2] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][2][2]
        self.layersMap['U'][2][2] = self.layersMap['F'][2][2]
        self.layersMap['F'][2][2] = self.layersMap['D'][2][2]
        self.layersMap['D'][2][2] = self.layersMap['B'][0][0]
        self.layersMap['B'][0][0] = aux
        aux = self.layersMap['U'][0][2]
        self.layersMap['U'][0][2] = self.layersMap['F'][0][2]
        self.layersMap['F'][0][2] = self.layersMap['D'][0][2]
        self.layersMap['D'][0][2] = self.layersMap['B'][2][0]
        self.layersMap['B'][2][0] = aux
        aux = self.layersMap['U'][1][2]
        self.layersMap['U'][1][2] = self.layersMap['F'][1][2]
        self.layersMap['F'][1][2] = self.layersMap['D'][1][2]
        self.layersMap['D'][1][2] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = aux


    def moveRightP(self):
        #Rotation of right layer
        aux = self.layersMap['R'][0][0]
        self.layersMap['R'][0][0] = self.layersMap['R'][0][2]
        self.layersMap['R'][0][2] = self.layersMap['R'][2][2]
        self.layersMap['R'][2][2] = self.layersMap['R'][2][0]
        self.layersMap['R'][2][0] = aux
        aux = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = self.layersMap['R'][1][2]
        self.layersMap['R'][1][2] = self.layersMap['R'][2][1]
        self.layersMap['R'][2][1] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = aux

        #Rotation of mid half layers
        aux = self.layersMap['U'][2][2]
        self.layersMap['U'][2][2] = self.layersMap['B'][0][0]  
        self.layersMap['B'][0][0] = self.layersMap['D'][2][2]
        self.layersMap['D'][2][2] = self.layersMap['F'][2][2]
        self.layersMap['F'][2][2] = aux
        aux = self.layersMap['U'][0][2]
        self.layersMap['U'][0][2] = self.layersMap['B'][2][0]
        self.layersMap['B'][2][0] = self.layersMap['D'][0][2]
        self.layersMap['D'][0][2] = self.layersMap['F'][0][2]
        self.layersMap['F'][0][2] = aux
        aux = self.layersMap['U'][1][2]
        self.layersMap['U'][1][2] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = self.layersMap['D'][1][2]
        self.layersMap['D'][1][2] = self.layersMap['F'][1][2]
        self.layersMap['F'][1][2] = aux
    

    def moveCenterVertical(self):
        #Rotation of center layers
        aux = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = aux
        
        #Rotation of edge layers
        aux = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = aux
        aux = self.layersMap['F'][1][2]
        self.layersMap['F'][1][2] = self.layersMap['R'][1][2]
        self.layersMap['R'][1][2] = self.layersMap['B'][1][2]
        self.layersMap['B'][1][2] = self.layersMap['L'][1][2]
        self.layersMap['L'][1][2] = aux

    
    def moveCenterVerticalP(self):
        #Rotation of center layers
        aux = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = aux
        
        #Rotation of edge layers
        aux = self.layersMap['F'][1][0]
        self.layersMap['F'][1][0] = self.layersMap['L'][1][0]
        self.layersMap['L'][1][0] = self.layersMap['B'][1][0]
        self.layersMap['B'][1][0] = self.layersMap['R'][1][0]
        self.layersMap['R'][1][0] = aux
        aux = self.layersMap['F'][1][2]
        self.layersMap['F'][1][2] = self.layersMap['L'][1][2]
        self.layersMap['L'][1][2] = self.layersMap['B'][1][2]
        self.layersMap['B'][1][2] = self.layersMap['R'][1][2]
        self.layersMap['R'][1][2] = aux

    
    def moveCenterHorizontal(self):
        #Rotation of center layers
        aux = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = aux
        
        #Rotation of edge layers
        aux = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = self.layersMap['B'][2][1]
        self.layersMap['B'][2][1] = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = aux
        aux = self.layersMap['F'][2][1]
        self.layersMap['F'][2][1] = self.layersMap['D'][2][1]
        self.layersMap['D'][2][1] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['U'][2][1]
        self.layersMap['U'][2][1] = aux

    
    def moveCenterHorizontalP(self):
        #Rotation of center layers
        aux = self.layersMap['F'][1][1]
        self.layersMap['F'][1][1] = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = self.layersMap['B'][1][1]
        self.layersMap['B'][1][1] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = aux
        
        #Rotation of edge layers
        aux = self.layersMap['F'][0][1]
        self.layersMap['F'][0][1] = self.layersMap['U'][0][1]
        self.layersMap['U'][0][1] = self.layersMap['B'][2][1]
        self.layersMap['B'][2][1] = self.layersMap['D'][0][1]
        self.layersMap['D'][0][1] = aux
        aux = self.layersMap['F'][2][1]
        self.layersMap['F'][2][1] = self.layersMap['U'][2][1]
        self.layersMap['U'][2][1] = self.layersMap['B'][0][1]
        self.layersMap['B'][0][1] = self.layersMap['D'][2][1]
        self.layersMap['D'][2][1] = aux

    
    def moveCenterProfund(self):
        #Rotation of center layers
        aux = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = aux
        
        #Rotation of edge layers
        aux = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['L'][2][1]
        self.layersMap['L'][2][1] = self.layersMap['D'][1][2]
        self.layersMap['D'][1][2] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = aux
        aux = self.layersMap['U'][1][2]
        self.layersMap['U'][1][2] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['R'][2][1]
        self.layersMap['R'][2][1] = aux

    
    def moveCenterProfundP(self):
        #Rotation of center layers
        aux = self.layersMap['U'][1][1]
        self.layersMap['U'][1][1] = self.layersMap['R'][1][1]
        self.layersMap['R'][1][1] = self.layersMap['D'][1][1]
        self.layersMap['D'][1][1] = self.layersMap['L'][1][1]
        self.layersMap['L'][1][1] = aux
        
        #Rotation of edge layers
        aux = self.layersMap['U'][1][0]
        self.layersMap['U'][1][0] = self.layersMap['R'][2][1]
        self.layersMap['R'][2][1] = self.layersMap['D'][1][2]
        self.layersMap['D'][1][2] = self.layersMap['L'][0][1]
        self.layersMap['L'][0][1] = aux
        aux = self.layersMap['U'][1][2]
        self.layersMap['U'][1][2] = self.layersMap['R'][0][1]
        self.layersMap['R'][0][1] = self.layersMap['D'][1][0]
        self.layersMap['D'][1][0] = self.layersMap['L'][2][1]
        self.layersMap['L'][2][1] = aux


    def fullRotateVertical(self):
        self.moveUp()
        self.moveCenterVertical()
        self.moveDownP()

    def fullRotateVerticalP(self):
        self.moveUpP()
        self.moveCenterVerticalP()
        self.moveDown()

    def fullRotateHorizontal(self):
        self.moveRight()
        self.moveCenterHorizontal()
        self.moveLeftP()

    def fullRotateHorizontalP(self):
        self.moveRightP()
        self.moveCenterHorizontalP()
        self.moveLeft()

    def fullRotateProfund(self):
        self.moveFront()
        self.moveCenterProfund()
        self.moveBackP()

    def fullRotateProfundP(self):
        self.moveFrontP()
        self.moveCenterProfundP()
        self.moveBack()


    ####################
    ### SOLUTION METHODS
    ####################
    '''def solveByStep(self, step):
        if step == 1:
            #Solve down floor
            self.solveDownFloor()

        elif step == 2:
            #Match one top corner
            numOfPlacedTopPieces = self.prepareToSolveTopFloor()

            if numOfPlacedTopPieces == 1:
                #Position rest of the corners
                self.rotateCorners()
        
        elif step == 3:
            #Rotate top corners
            self.rotateEachCorner()

        elif step == 4:
            #Final Alignment cube
            self.centerCube()

            #Set the cube as solved
            self.solved = True'''

    
    def solve(self):
        #Solve down cross
        self.solveDownCross()

        #Solve down corners
        self.solveDownCorners()

        #Solve middle layer
        self.solveMiddleLayer()

        #Solve up cross
        self.solveUpCross()

        #Allign up cross
        self.allignUpCross()

        #Allign up corners
        self.allignUpCorners()

        #Rotate up corners
        self.rotateUpIndividualCorners()

        #Set the cube as solved
        self.solved = True


    def solveDownCross(self):
        downColour = self.layersMap['D'][1][1]
        
        #Iterate 4 times to position the 4 edge pieces of the floor
        for i in range(4):
            frontColour = self.layersMap['F'][1][1]

            #Find edge piece
            pieceIdFound = self.findEdge(set([downColour, frontColour]), set())
            edgePiece = self.edgesMap[pieceIdFound]

            #Place edge on the correct place
            self.placeEdgeToDown(edgePiece, downColour)

            #rotate cube vertical
            self.fullRotateVertical()


    def placeEdgeToDown(self, piece, targetColour):
        #Take the piece to FU
        if piece.pieceId == 'FD':
            if piece.getColour(self.layersMap, 'D') == targetColour:
                return #The piece is already in the correct position and rotation
            else:
                self.moveFront()
                self.moveFront()
        elif piece.pieceId == 'FU':
            pass #Target Position
        elif piece.pieceId == 'BD':
            self.moveBack()
            self.moveBack()
            self.moveUp()
            self.moveUp()
        elif piece.pieceId == 'BU':
            self.moveUp()
            self.moveUp()
        elif piece.pieceId == 'DL':
            self.moveLeft()
            self.moveLeft()
            self.moveUpP()
        elif piece.pieceId == 'DR':
            self.moveRight()
            self.moveRight()
            self.moveUp()
        elif piece.pieceId == 'UL':
            self.moveUpP()
        elif piece.pieceId == 'UR':
            self.moveUp()
        elif piece.pieceId == 'FR':
            self.moveRight()
            self.moveUp()
            self.moveRightP()
        elif piece.pieceId == 'FL':
            self.moveLeftP()
            self.moveUpP()
            self.moveLeft()
        elif piece.pieceId == 'BL':
            self.moveLeft()
            self.moveUpP()
            self.moveLeftP()
        elif piece.pieceId == 'BR':
            self.moveRightP()
            self.moveUp()
            self.moveRight()

        #Update piece instance after movements
        piece = self.edgesMap['FU']

        if piece.getColour(self.layersMap, 'U') == targetColour:
            self.moveFront()
            self.moveFront()
        else:
            self.moveUpP()
            self.moveRightP()
            self.moveFront()
            self.moveRight()


    def solveDownCorners(self):
        downColour = self.layersMap['D'][1][1]
        
        #Iterate 4 times to position the 4 corners
        for i in range(4):
            frontColour = self.layersMap['F'][1][1]
            rightColour = self.layersMap['R'][1][1]

            #Find corner piece
            pieceIdFound = self.findCorner(set([downColour, frontColour, rightColour]), set())
            cornerPiece = self.cornersMap[pieceIdFound]

            #Place corner on the correct place
            self.placeCornerToDown(cornerPiece, downColour)

            #rotate cube vertical
            self.fullRotateVertical()


    def placeCornerToDown(self, piece, targetColour):
        #Take the piece to FUR
        if piece.pieceId == 'FUL':
            self.moveUpP()
        elif piece.pieceId == 'FUR':
            pass #Target Position
        elif piece.pieceId == 'FDL':
            self.moveLeftP()
            self.moveUpP()
            self.moveLeft()
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
            self.moveLeft()
            self.moveUpP()
            self.moveLeftP()
            self.moveUpP()
            self.moveUpP()
        elif piece.pieceId == 'BDR':
            self.moveRightP()
            self.moveUp()
            self.moveRight()
            self.moveUp()

        #Update piece instance after movements
        piece = self.cornersMap['FUR']

        #Take the piece to the floor:
        if piece.getColour(self.layersMap, 'F') == targetColour:
            self.moveCornerAlgo()
        elif piece.getColour(self.layersMap, 'U') == targetColour:
            for i in range(3):
                self.moveCornerAlgo()
        elif piece.getColour(self.layersMap, 'R') == targetColour:
            for i in range(5):
                self.moveCornerAlgo()


    def solveMiddleLayer(self):
        #Iterate 4 times to position the 4 corners
        for i in range(4):
            frontColour = self.layersMap['F'][1][1]
            rightColour = self.layersMap['R'][1][1]

            #Look edge piece in middle layer
            pieceIdFound = self.findEdge(set([frontColour, rightColour]), set(['FD','BD','DR','DL','FU','BU','UR','UL']))
            if pieceIdFound != None:
                edgePiece = self.edgesMap[pieceIdFound]

                #Place edge on the up layer
                self.placeMiddleEdgeToUp(edgePiece, frontColour)

            #Find edge piece in up layer
            pieceIdFound = self.findEdge(set([frontColour, rightColour]), set(['FD','BD','DR','DL','FR','FL','BR','BL']))
            if pieceIdFound != None:
                edgePiece = self.edgesMap[pieceIdFound]

                #Place edge on the up layer
                self.placeEdgeToMiddle(edgePiece, frontColour)

            #rotate cube vertical
            self.fullRotateVertical()


    def placeMiddleEdgeToUp(self, piece, targetColour):
        #Look the edge in middle layer, if found move it to up layer
        if piece.pieceId == 'FR':
            if piece.getColour(self.layersMap, 'F') == targetColour:
                return #The piece is already in the correct position and rotation
            else:
                self.moveMiddleEdgeAlgo()
        elif piece.pieceId == 'FL':
            self.fullRotateVerticalP()
            self.moveMiddleEdgeAlgo()
            self.fullRotateVertical()
        elif piece.pieceId == 'BR':
            self.fullRotateVertical()
            self.moveMiddleEdgeAlgo()
            self.fullRotateVerticalP()
        elif piece.pieceId == 'BL':
            self.fullRotateVertical()
            self.fullRotateVertical()
            self.moveMiddleEdgeAlgo()
            self.fullRotateVertical()
            self.fullRotateVertical()
        
    
    def placeEdgeToMiddle(self, piece, targetColour):
        #Look the edge in up layer and place it in the front
        if piece.pieceId == 'FU':
            if piece.getColour(self.layersMap, 'F') == targetColour:
                pass
        elif piece.pieceId == 'UL':
            self.moveUpP()
        elif piece.pieceId == 'UR':
            self.moveUp()
        elif piece.pieceId == 'BU':
            self.moveUp()
            self.moveUp()

        #Depending if the front colour is already matching checks which algorithm to apply
        if self.layersMap['F'][0][1] == targetColour:
            self.moveMiddleEdgeAlgo()
        else:
            self.moveUpP()
            self.moveMiddleEdgeAlgoP()


    def solveUpCross(self):
        upColour = self.layersMap['U'][1][1]
        
        #Count number of target colour coincidences in the top
        upColourCoincidences = self.getUpColourEdgeCoincidences(upColour)

        if upColourCoincidences == 0:
            self.upCrossAllignedAlgo()
            self.upCrossNotAllignedAlgo()
        elif upColourCoincidences == 2:
            if self.upPiecesAlligned(upColour):
                self.upCrossAllignedAlgo()
            else:
                self.upCrossNotAllignedAlgo()


    def getUpColourEdgeCoincidences(self, targetColour):
        coincidences = 0
        if self.layersMap['U'][0][1] == targetColour:
            coincidences += 1
        if self.layersMap['U'][2][1] == targetColour:
            coincidences += 1
        if self.layersMap['U'][1][0] == targetColour:
            coincidences += 1
        if self.layersMap['U'][1][2] == targetColour:
            coincidences += 1

        return coincidences


    def getUpColourEdgeFullCoincidences(self):
        coincidences = 0
        if self.layersMap['F'][0][1] == self.layersMap['F'][1][1]:
            coincidences += 1
        if self.layersMap['R'][0][1] == self.layersMap['R'][1][1]:
            coincidences += 1
        if self.layersMap['L'][0][1] == self.layersMap['L'][1][1]:
            coincidences += 1
        if self.layersMap['B'][0][1] == self.layersMap['B'][1][1]:
            coincidences += 1
        
        return coincidences


    def upPiecesAlligned(self, targetColour):
        return (self.layersMap['U'][0][1] == targetColour and self.layersMap['U'][2][1] == targetColour) or (self.layersMap['U'][1][0] == targetColour and self.layersMap['U'][1][2] == targetColour)


    def upCrossAllignedAlgo(self):
        upColour = self.layersMap['U'][1][1]

        if self.layersMap['U'][2][1] != upColour:
            self.moveUp()

        self.moveRightP()
        self.moveFrontP()
        self.moveUpP()
        self.moveFront()
        self.moveUp()
        self.moveRight()

    
    def upCrossNotAllignedAlgo(self):
        upColour = self.layersMap['U'][1][1]
        
        #rotate until place the two coincidences in the back left corner
        while self.layersMap['U'][1][0] != upColour or self.layersMap['U'][0][1] != upColour:
            self.moveUp()

        self.moveRightP()
        self.moveUpP()
        self.moveFrontP()
        self.moveUp()
        self.moveFront()
        self.moveRight()


    def allignUpCross(self):
        #Checks if it is already alligned
        if self.getUpColourEdgeFullCoincidences() == 4:
            return #Nothing to do
        
        #If not alligned rotate until finds two coincidences
        while self.getUpColourEdgeFullCoincidences() != 2:
            self.moveUp()

            if self.getUpColourEdgeFullCoincidences() == 4:
                return #Nothing to do


        #Rotate full cube until is well placed to execute next algorithm
        while self.getUpColourEdgeFullCoincidences() != 4:
            if self.layersMap['F'][0][1] == self.layersMap['F'][1][1]:
                if self.layersMap['B'][0][1] == self.layersMap['B'][1][1]:
                    self.fullAllignUpCross()
                    #Allign again until finds two coincidences
                    while self.getUpColourEdgeFullCoincidences() != 2:
                        self.moveUp()
                elif self.layersMap['R'][0][1] == self.layersMap['R'][1][1]:
                    self.fullAllignUpCross()

            self.fullRotateVertical()


    def fullAllignUpCross(self):
        self.moveRightP()
        self.moveUpP()
        self.moveRight()
        self.moveUpP()
        self.moveRightP()
        self.moveUpP()
        self.moveUpP()
        self.moveRight()
        self.moveUpP()


    def allignUpCorners(self):
        #Match one top corner
        numOfPlacedUpCorners = self.getNumOfPlacedUpCorners()

        if numOfPlacedUpCorners == 4:
            return #Already well placed all corners
        elif numOfPlacedUpCorners == 0:
            self.rotateCorners(True)
            numOfPlacedUpCorners = self.getNumOfPlacedUpCorners()

        if numOfPlacedUpCorners == 1:
            while not set([self.layersMap['F'][1][1],self.layersMap['R'][1][1]]).issubset(self.cornersMap['FUR'].getColoursSet(self.layersMap)):
                self.fullRotateVertical()

            if set([self.layersMap['L'][1][1],self.layersMap['B'][1][1]]).issubset(self.cornersMap['FUL'].getColoursSet(self.layersMap)):
                self.rotateCorners(True)
            else:
                self.rotateCorners(False)


    def rotateCorners(self, rotateClockSide):
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


    def getNumOfPlacedUpCorners(self):
        coincidences = 0
        if set([self.layersMap['F'][1][1],self.layersMap['R'][1][1]]).issubset(self.cornersMap['FUR'].getColoursSet(self.layersMap)):
            coincidences += 1
        if set([self.layersMap['F'][1][1],self.layersMap['L'][1][1]]).issubset(self.cornersMap['FUL'].getColoursSet(self.layersMap)):
            coincidences += 1
        if set([self.layersMap['B'][1][1],self.layersMap['R'][1][1]]).issubset(self.cornersMap['BUR'].getColoursSet(self.layersMap)):
            coincidences += 1
        if set([self.layersMap['B'][1][1],self.layersMap['L'][1][1]]).issubset(self.cornersMap['BUL'].getColoursSet(self.layersMap)):
            coincidences += 1

        return coincidences


    def rotateUpIndividualCorners(self):
        upColour = self.layersMap['U'][1][1]
        for i in range(4):
            currentColour = self.layersMap['U'][2][2]
            
            if currentColour != upColour:
                frontColour = self.layersMap['F'][0][2]
                if frontColour == upColour:
                    self.rotateCornerClockSide()
                else:
                    self.rotateCornerAntiClockSide()

            self.moveUp()


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


    def findEdge(self, colours, exceptions) -> str:
        for pieceId in self.edgesMap.keys():
            if not pieceId in exceptions:
                piece = self.edgesMap[pieceId]
                pieceColoursSet = piece.getColoursSet(self.layersMap)
                if colours.issubset(pieceColoursSet):
                    return pieceId
        
        return None

    
    def findCorner(self, colours, exceptions) -> str:
        for pieceId in self.cornersMap.keys():
            if not pieceId in exceptions:
                piece = self.cornersMap[pieceId]
                pieceColoursSet = piece.getColoursSet(self.layersMap)
                if colours.issubset(pieceColoursSet):
                    return pieceId

        return None


    def moveMiddleEdgeAlgo(self):
        self.moveCornerAlgo()
        self.fullRotateVertical()
        self.moveCornerAlgoP()
        self.fullRotateVerticalP()

    
    def moveMiddleEdgeAlgoP(self):
        self.fullRotateVertical()
        self.moveCornerAlgoP()
        self.fullRotateVerticalP()
        self.moveCornerAlgo()


    def moveCornerAlgo(self):
        self.moveUp()
        self.moveRight()
        self.moveUpP()
        self.moveRightP()

    
    def moveCornerAlgoP(self):
        self.moveUpP()
        self.moveLeftP()
        self.moveUp()
        self.moveLeft()


    ##################
    ### OUTPUT METHODS
    ##################
    def getCube(self):
        return self.layersMap


    '''def getCubeFront(self):
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

        return result


    def printCubeFront(self):
        print(self.getCubeFront())


    def getCubeBack(self):
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

        return result


    def printCubeBack(self):
        print(self.getCubeBack())'''

    
    def isSolved(self):
        return self.solved