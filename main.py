from color import readColor, offsetTransformation, randomizedTransformation, addColor, paletteTransformation, shiftTransformation
from overlay import preprocessOverlay, addHat, addPunk, addSword, addFace, addBackGround
import json
import os
from datetime import date
from PIL import Image
import random

nftCount = 100

path = 'C:/nft/outputDir/img'

files = os.listdir(path)
ipfs = 'QmQwG6MFz8rSqjXnGJ8cHYtviHQcZ78Td2SdpB7SEbrAkV'

def main(): 
    # Import an image from directory:
    punk = Image.open("inputDir/modelA2.png")


    # Extracting the width and height of the image:
    width, height = punk.size

    # Create a randomised rgb transformation list
    colors = readColor(width, height, punk)
    transformations = offsetTransformation(colors, nftCount)
    print(len(transformations))
    # transformations = paletteTransformation()
    # transformations = shiftTransformation(colors, "color_shift.json")
    loop = 0
    for mint in range(len(transformations)):

        blank_image = Image.new('RGB', (width*2, height*2), (0,0,0))
        bwidth, bheight = blank_image.size

        output_image = punk.copy()
        rgba = output_image.convert("RGBA")
        punk_data = rgba.getdata()

        addColor(transformations[mint], output_image, punk_data)

        # Saving the final output
        filename = "outputDir/img/"+str(loop)+".png"
        output_image.save(filename, format="png")
        loop+=1
        # print('minted : ', filename[10:])

main()