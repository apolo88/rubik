from django.shortcuts import render
#from .code.Rubik import *
from .code.Rubik2x2 import *
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


def twoByTwo(request):
    
    colorsMap = {'G':'green', 'B':'blue', 'Y':'yellow', 'W':'white', 'R':'red', 'O':'orange'}

    rubikInstance = Rubik2x2()
    rubikInstance.initCube()
    rubikInstance.disorder('Simple')
    testVar = rubikInstance.getCubeFront()
    cubeObject = rubikInstance.getCube()
    #rubikInstance.printCubeFront()
    #testVar = 5

    contextObject = {}
    contextObject['color'] = 'black'
    contextObject['test_var'] = testVar
    
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