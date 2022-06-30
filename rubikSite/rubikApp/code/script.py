from Rubik import *
from Rubik2x2 import *
import sys


def main():
    
    #Initial Menu
    print('Welcome to Rubik! \n')
    dimOption = showDimMenu()
    rubikInstance = None

    #Checks the dimension for the cube
    if dimOption == '1':
        print('Rubik 2x2')
        rubikInstance = Rubik2x2()
    elif dimOption == '2':
        print('Rubik 3x3')
        rubikInstance = Rubik3x3()
    else:
        print('Incorrect Option')
        return
    
    print('\n')

    #Creates and initialize the cube
    #rubikInstance.initCube()

    modeOption = None
    while modeOption != '4':
        print('\n')
        modeOption = showModeMenu()

        #Manual
        if modeOption == '1':
            manualMode(rubikInstance)
        #Disorder
        elif modeOption == '2':
            disorderMode(rubikInstance)
        #Solve
        elif modeOption == '3':
            solveMode(rubikInstance)


##############
### SHOW MENUS
##############
def showMenu(description, menuOptions) -> str:
    menu = description + ': \n'
    i = 1
    for option in menuOptions:
        menu += str(i) + ' ' + option + '\n'
        i = i + 1

    return input(menu)

def showDimMenu() -> str:
    dims = ['2x2','3x3']
    return showMenu('Please select a dimension', dims)

def showModeMenu() -> str:
    modes = ['Manual','Disorder','Solve','Cancel']
    return showMenu('Please select a mode', modes)

def showMoveMenu() -> str:
    moves = ['F','F\'','B','B\'','U','U\'','D','D\'','L','L\'','R','R\'','Previous Menu']
    return showMenu('Please select a movement', moves)

def showDisorderMenu() -> str:
    disOptions = ['Simple','Medium','Hard','Previous Menu']
    return showMenu('Please select the disorder complexity', disOptions)

def showSolveMenu() -> str:
    solveOptions = ['Step by Step','Direct','Previous Menu']
    return showMenu('Please select the solve mode', solveOptions)

################
### MENU ACTIONS
################
def manualMode(rubikInstance) -> str:
    moveOption = None
    while moveOption != '13':
        print('\n')
        rubikInstance.printCube()
        sys.stdin.read(1)
        
        moveOption = showMoveMenu()
        # F
        if moveOption == '1':
            rubikInstance.moveFront()
        # F'
        elif moveOption == '2':
            rubikInstance.moveFrontP()
        # B
        elif moveOption == '3':
            rubikInstance.moveBack()
        # B'
        elif moveOption == '4':
            rubikInstance.moveBackP()
        # U
        elif moveOption == '5':
            rubikInstance.moveUp()
        # U'
        elif moveOption == '6':
            rubikInstance.moveUpP()
        # D
        elif moveOption == '7':
            rubikInstance.moveDown()
        # D'
        elif moveOption == '8':
            rubikInstance.moveDownP()
        # L
        elif moveOption == '9':
            rubikInstance.moveLeft()
        # L'
        elif moveOption == '10':
            rubikInstance.moveLeftP()
        # R
        elif moveOption == '11':
            rubikInstance.moveRight()
        # R'
        elif moveOption == '12':
            rubikInstance.moveRightP()


def disorderMode(rubikInstance) -> str:    
    print('\n')
    disorderOption = showDisorderMenu()
    # Simple
    if disorderOption == '1':
        rubikInstance.disorder('Simple')
    # Medium
    elif disorderOption == '2':
        rubikInstance.disorder('Medium')
    # Hard
    elif disorderOption == '3':
        rubikInstance.disorder('Hard')
    elif disorderOption == '4':
        return

    rubikInstance.printCube()


def solveMode(rubikInstance) -> str:    
    print('\n')
    solveOption = showSolveMenu()
    # Step by Step
    if solveOption == '1':
        rubikInstance.solve()
    # Direct
    elif solveOption == '2':
        rubikInstance.solve()
    # Previous Menu
    elif solveOption == '3':
        return

    #rubikInstance.printCube()
    

if __name__ == '__main__':
    main()