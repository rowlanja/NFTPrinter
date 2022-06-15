import random
import json
from turtle import color
from types import NoneType

def readColor(width, height, input_image):
    colors = set()
    for i in range(width):
        for j in range(height):
            
            # getting the RGB pixel value.
            r, g, b, p = input_image.getpixel((i, j))

            colors.add(tuple([r,g,b]))
    return colors

def offsetTransformation(colors, mintCount): 
    transformations = []
    for mint in range(mintCount):
        map = dict()
        newR, newG, newB = random.sample(range(1, 20), 3)
        for color in colors:
            if color == (255,255,255) :
                print('white')
                continue
            r = color[0] + newR
            g = color[1] + newG
            b = color[2] + newB
            map[color] = (r,g,b)
        transformations.append(map)
    return transformations

def randomizedTransformation(colors, mintCount):
    transformations = []
    for mint in range(mintCount):
        map = dict()
        for color in colors:
            newR, newG, newB = random.sample(range(1, 255), 3)
            map[color] = (newR,newG,newB)
        transformations.append(map)
    return transformations

def addColor(colorMap, input_image, pixel_map):
    newData = []
    for item in pixel_map:
        transformation = colorMap.get(tuple([item[0],item[1],item[2]]))
        if item[0] == 255 and item[1] == 255 and item[2] == 255:  # finding black colour by its RGB value
            newData.append((0, 0, 0, 0))
        else:
            # Apply transformation  :
            if transformation != None:
                newData.append((transformation[0],transformation[1],transformation[2]))
            else : 
                newData.append((item[0], item[1], item[2]))
    input_image.putdata(newData)
    return newData


## lord forgive me for this code
def createTolerance(tup, tolerance, after, transformation):
    befores = []
    for x in range(len(tup)):
        tupX = tup[x]
        z = []
        r = range(tolerance+1)
        for x in r[1:]:
            if (tupX + x) < 255 : 
                a = tupX + x
            else :
                a = tupX
            z.append(a)
            if (tupX - x) > 0 : 
                a = tupX - x
            else :
                a = tupX
            z.append(a)
        befores.append(z)
    for a in befores[0]:
        for b in befores[1]:
            for c in befores[2]:
                transformation[(tuple((a,b,c)))] = after


def paletteTransformation():
    fileObject = open("color_palette.json", "r")
    jsonContent = fileObject.read()
    palette = json.loads(jsonContent)
    transformation = dict()
    for before, after in palette.items():
        before = tuple(map(int, before.split(',')))
        after = tuple(map(int, after.split(',')))
        transformation[tuple(before)] = tuple(after)
        createTolerance(before, 5, after, transformation )
    return transformation


def shiftTransformation(colors):
    for color in colors:
        d = dict()
        b = tuple(map(int, str(before).split(',')))
        tx = tuple(map(int, t.split(',')))
        rDiff = tx[0] - b[0]
        gDiff = tx[1] - b[1]
        bDiff = tx[2] - b[2]
        for color in colors:
            newR = color[0] + rDiff
            newG = color[1] + gDiff
            newB = color[2] + bDiff
            d[color] = (newR,newG,newB)
        transformations.append(d)
        return transformations
