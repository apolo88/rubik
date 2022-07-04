from django.shortcuts import render
#from .code.Rubik import *
from .code.Rubik2x2 import *
from .code.Rubik3x3 import *
from django.core.cache import cache

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={},
    )


def clearCache(request):
    """
    Función vista para la página inicio del sitio.
    """
    cache.set('2x2Cube', None)
    cache.set('2x2Step', None)
    cache.set('3x3Cube', None)
    cache.set('3x3Step', None)

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'clearcache.html',
        context={},
    )


def twoByTwo(request):
    
    colorsMap = {'G':'green', 'B':'blue', 'Y':'yellow', 'W':'white', 'R':'red', 'O':'orange'}

    rubikInstance = cache.get('2x2Cube')
    print('cache')
    print(rubikInstance)

    if rubikInstance is  None:
        rubikInstance = Rubik2x2()
        rubikInstance.initCube()
        #rubikInstance.disorder('Simple')
        cache.set('2x2Cube', rubikInstance)
    elif not rubikInstance.isSolved():
        rubikStep = cache.get('2x2Step')
        if rubikStep is  None:
            rubikStep = 1
        elif rubikStep <= 4:
            rubikStep += 1

        cache.set('2x2Step', rubikStep)
        print('Step')
        print(rubikStep)
        #rubikInstance.solveByStep(rubikStep)
        cache.set('2x2Cube', rubikInstance)
    
    cubeObject = rubikInstance.getCube()

    contextObject = {}
    
    #Front
    contextObject['F00'] = colorsMap[cubeObject['F'][0][0]]
    contextObject['F01'] = colorsMap[cubeObject['F'][0][1]]
    contextObject['F10'] = colorsMap[cubeObject['F'][1][0]]
    contextObject['F11'] = colorsMap[cubeObject['F'][1][1]]

    #Back
    contextObject['B00'] = colorsMap[cubeObject['B'][0][0]]
    contextObject['B01'] = colorsMap[cubeObject['B'][0][1]]
    contextObject['B10'] = colorsMap[cubeObject['B'][1][0]]
    contextObject['B11'] = colorsMap[cubeObject['B'][1][1]]

    #Left
    contextObject['L00'] = colorsMap[cubeObject['L'][0][0]]
    contextObject['L01'] = colorsMap[cubeObject['L'][0][1]]
    contextObject['L10'] = colorsMap[cubeObject['L'][1][0]]
    contextObject['L11'] = colorsMap[cubeObject['L'][1][1]]

    #Right
    contextObject['R00'] = colorsMap[cubeObject['R'][0][0]]
    contextObject['R01'] = colorsMap[cubeObject['R'][0][1]]
    contextObject['R10'] = colorsMap[cubeObject['R'][1][0]]
    contextObject['R11'] = colorsMap[cubeObject['R'][1][1]]

    #Down
    contextObject['D00'] = colorsMap[cubeObject['D'][0][0]]
    contextObject['D01'] = colorsMap[cubeObject['D'][0][1]]
    contextObject['D10'] = colorsMap[cubeObject['D'][1][0]]
    contextObject['D11'] = colorsMap[cubeObject['D'][1][1]]

    #Up
    contextObject['U00'] = colorsMap[cubeObject['U'][0][0]]
    contextObject['U01'] = colorsMap[cubeObject['U'][0][1]]
    contextObject['U10'] = colorsMap[cubeObject['U'][1][0]]
    contextObject['U11'] = colorsMap[cubeObject['U'][1][1]]


    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index2x2.html',
        context = contextObject,
    )


def threeByThree(request):
    
    colorsMap = {'G':'green', 'B':'blue', 'Y':'yellow', 'W':'white', 'R':'red', 'O':'orange'}

    #rubikInstance = cache.get('3x3Cube')
    #print('cache')
    #print(rubikInstance)

    #if rubikInstance is  None:
    rubikInstance = Rubik3x3()
    rubikInstance.initCube()
    '''rubikInstance.moveUp()
    rubikInstance.moveUp()
    rubikInstance.moveUp()
    rubikInstance.moveUpP()
    rubikInstance.moveDown()
    rubikInstance.moveDown()
    rubikInstance.moveDown()
    rubikInstance.moveDownP()
    rubikInstance.moveRight()
    rubikInstance.moveRight()
    rubikInstance.moveRight()
    rubikInstance.moveRightP()
    rubikInstance.moveLeft()
    rubikInstance.moveLeft()
    rubikInstance.moveLeft()
    rubikInstance.moveLeftP()
    rubikInstance.moveFront()
    rubikInstance.moveFront()
    rubikInstance.moveFront()
    rubikInstance.moveFrontP()
    rubikInstance.moveBack()
    rubikInstance.moveBack()
    rubikInstance.moveBack()
    rubikInstance.moveBackP()'''
    
    
    '''rubikInstance.moveCenterVertical()
    rubikInstance.moveCenterVertical()
    rubikInstance.moveCenterVertical()
    rubikInstance.moveCenterVerticalP()
    rubikInstance.moveCenterHorizontal()
    rubikInstance.moveCenterHorizontal()
    rubikInstance.moveCenterHorizontal()
    rubikInstance.moveCenterHorizontalP()
    rubikInstance.moveCenterProfund()
    rubikInstance.moveCenterProfund()
    rubikInstance.moveCenterProfund()
    rubikInstance.moveCenterProfundP()'''

    #rubikInstance.fullRotateVertical()
    #rubikInstance.fullRotateVerticalP()
    #rubikInstance.fullRotateHorizontal()
    #rubikInstance.fullRotateHorizontalP()
    #rubikInstance.fullRotateProfund()
    #rubikInstance.fullRotateProfundP()
    
    rubikInstance.disorder('Simple')
    rubikInstance.solve()
        #cache.set('3x3Cube', rubikInstance)
    '''elif not rubikInstance.isSolved():
        rubikStep = cache.get('3x3Step')
        if rubikStep is  None:
            rubikStep = 1
        elif rubikStep <= 4:
            rubikStep += 1

        cache.set('2x2Step', rubikStep)
        print('Step')
        print(rubikStep)
        rubikInstance.solveByStep(rubikStep)
        cache.set('2x2Cube', rubikInstance)'''
    
    cubeObject = rubikInstance.getCube()

    contextObject = {}
    
    #Front
    contextObject['F00'] = colorsMap[cubeObject['F'][0][0]]
    contextObject['F01'] = colorsMap[cubeObject['F'][0][1]]
    contextObject['F02'] = colorsMap[cubeObject['F'][0][2]]
    contextObject['F10'] = colorsMap[cubeObject['F'][1][0]]
    contextObject['F11'] = colorsMap[cubeObject['F'][1][1]]
    contextObject['F12'] = colorsMap[cubeObject['F'][1][2]]
    contextObject['F20'] = colorsMap[cubeObject['F'][2][0]]
    contextObject['F21'] = colorsMap[cubeObject['F'][2][1]]
    contextObject['F22'] = colorsMap[cubeObject['F'][2][2]]

    #Back
    contextObject['B00'] = colorsMap[cubeObject['B'][0][0]]
    contextObject['B01'] = colorsMap[cubeObject['B'][0][1]]
    contextObject['B02'] = colorsMap[cubeObject['B'][0][2]]
    contextObject['B10'] = colorsMap[cubeObject['B'][1][0]]
    contextObject['B11'] = colorsMap[cubeObject['B'][1][1]]
    contextObject['B12'] = colorsMap[cubeObject['B'][1][2]]
    contextObject['B20'] = colorsMap[cubeObject['B'][2][0]]
    contextObject['B21'] = colorsMap[cubeObject['B'][2][1]]
    contextObject['B22'] = colorsMap[cubeObject['B'][2][2]]

    #Left
    contextObject['L00'] = colorsMap[cubeObject['L'][0][0]]
    contextObject['L01'] = colorsMap[cubeObject['L'][0][1]]
    contextObject['L02'] = colorsMap[cubeObject['L'][0][2]]
    contextObject['L10'] = colorsMap[cubeObject['L'][1][0]]
    contextObject['L11'] = colorsMap[cubeObject['L'][1][1]]
    contextObject['L12'] = colorsMap[cubeObject['L'][1][2]]
    contextObject['L20'] = colorsMap[cubeObject['L'][2][0]]
    contextObject['L21'] = colorsMap[cubeObject['L'][2][1]]
    contextObject['L22'] = colorsMap[cubeObject['L'][2][2]]

    #Right
    contextObject['R00'] = colorsMap[cubeObject['R'][0][0]]
    contextObject['R01'] = colorsMap[cubeObject['R'][0][1]]
    contextObject['R02'] = colorsMap[cubeObject['R'][0][2]]
    contextObject['R10'] = colorsMap[cubeObject['R'][1][0]]
    contextObject['R11'] = colorsMap[cubeObject['R'][1][1]]
    contextObject['R12'] = colorsMap[cubeObject['R'][1][2]]
    contextObject['R20'] = colorsMap[cubeObject['R'][2][0]]
    contextObject['R21'] = colorsMap[cubeObject['R'][2][1]]
    contextObject['R22'] = colorsMap[cubeObject['R'][2][2]]

    #Down
    contextObject['D00'] = colorsMap[cubeObject['D'][0][0]]
    contextObject['D01'] = colorsMap[cubeObject['D'][0][1]]
    contextObject['D02'] = colorsMap[cubeObject['D'][0][2]]
    contextObject['D10'] = colorsMap[cubeObject['D'][1][0]]
    contextObject['D11'] = colorsMap[cubeObject['D'][1][1]]
    contextObject['D12'] = colorsMap[cubeObject['D'][1][2]]
    contextObject['D20'] = colorsMap[cubeObject['D'][2][0]]
    contextObject['D21'] = colorsMap[cubeObject['D'][2][1]]
    contextObject['D22'] = colorsMap[cubeObject['D'][2][2]]

    #Up
    contextObject['U00'] = colorsMap[cubeObject['U'][0][0]]
    contextObject['U01'] = colorsMap[cubeObject['U'][0][1]]
    contextObject['U02'] = colorsMap[cubeObject['U'][0][2]]
    contextObject['U10'] = colorsMap[cubeObject['U'][1][0]]
    contextObject['U11'] = colorsMap[cubeObject['U'][1][1]]
    contextObject['U12'] = colorsMap[cubeObject['U'][1][2]]
    contextObject['U20'] = colorsMap[cubeObject['U'][2][0]]
    contextObject['U21'] = colorsMap[cubeObject['U'][2][1]]
    contextObject['U22'] = colorsMap[cubeObject['U'][2][2]]


    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index3x3.html',
        context = contextObject,
    )