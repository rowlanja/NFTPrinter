
from PIL import Image
import random
import numpy as np

mintCount = 10

def generateRGB(): 
    rgbTransformations = []
    for mint in range(mintCount):
        rgbBefore  = list(np.random.choice(range(256), size=3))
        rgbAfter  = list(np.random.choice(range(256), size=3))
        rgbTransformations.append([rgbBefore, rgbAfter])
    return rgbTransformations

def replaceColor(colorPair, width, height, input_image, pixel_map):
    rgbBefore = colorPair[0]
    rgbAfter = colorPair[1]
    for i in range(width):
        for j in range(height):
            
            # getting the RGB pixel value.
            r, g, b, p = input_image.getpixel((i, j))
            
            # Apply transformation  :
            if r < 10 and g < 10 and b < 10: 
                pixel_map[i, j] = (rgbAfter[0],rgbAfter[1],rgbAfter[2])
            # grayscale = (0.299*r + 0.587*g + 0.114*b)
    return pixel_map

def main(): 
    # Import an image from directory:
    input_image = Image.open("inputDir/BaseTemplate.png")

    # Extracting the width and height of the image:
    width, height = input_image.size
    
    # Create a randomised rgb transformation list
    transformations = generateRGB()

    for mint in range(mintCount):

        output_image = input_image.copy()
        # Access the pixel values 
        pixel_map = output_image.load()

        replaceColor(transformations[mint], width, height, output_image, pixel_map)
        # Saving the final output
        filename = "outputDir/Transformed"+str(random.randint(0,5000))+".png"
        output_image.save(filename, format="png")
        output_image.show(filename)
        print('minted : ', filename[10:])

main()