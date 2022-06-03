from color import addColor, shiftTransformation, readColor

from PIL import Image
import random
import os

#this function scales the overlay appropriatly and saves the overlay
def preprocessOverlay(width, height, filePath):
    overlays = []
    fileNames = []
    filelist=os.listdir(filePath)
    # Create list of hats
    for imageFile in filelist[:]: # filelist[:] makes a copy of filelist.
        img = Image.open(filePath+'/'+imageFile)
        overlays.append(img)
        fileNames.append(imageFile)
    return overlays, fileNames

def addHat(output_image, hats, hatNames, width, height, colorMap):
    
    #overlay random hat onto character
    index = random.randint(0, len(hats)-1)

    hat = hats[index]
    hatName = hatNames[index] 
    if hatName != 'bandana.png':
        print(hatName)
        resized = (int(width/4), int(height/4))
        hat = hat.resize(resized, resample=0)

        capWidth = int(hat.size[0])
        capHeight =  int(hat.size[1]) 
        #center the hat
        output_image.paste(hat, (int(int(width/2)-(capWidth/2)), 80), hat)
        # makes white pixels transparent
        # new_image = Image.new("RGBA", img.size, "WHITE")
    else :      

                
        hc = hat.copy()
        rgba = hc.convert("RGBA")
        hat_data = rgba.getdata()

        addColor(colorMap, hc, hat_data)

        resized = (int(width/2.6), int(height/2.6))
        hat = hc.resize(resized, resample=0)

        capWidth = int(hat.size[0])
        capHeight =  int(hat.size[1]) 
        #center the hat
        output_image.paste(hat, (int(int(width/2)-(capWidth/2)), 110), hat)
        # makes white pixels transparent
        # new_image = Image.new("RGBA", img.size, "WHITE")

    return output_image

def addPunk(output_image, punk, bwidth, bheight):
    #overlay random hat onto character

    punkWidth = int(punk.size[0])
    punkHeight =  int(punk.size[1]) 
    #center the hat
    output_image.paste(punk, (int(bwidth/2 - punkWidth/2), int((bheight/2)+40)), punk)
    # makes white pixels transparent
    # new_image = Image.new("RGBA", img.size, "WHITE")
    return output_image

def addSword(blank_image, swords, width, height):
    #overlay random sword onto character
    sword = random.choice(swords)
    #resize sword to be same size as punk
    resized = (int(width/2), int(height))
    sword = sword.resize(resized, resample=0)

    swordWidth = int(sword.size[0])
    swordHeight =  int(sword.size[1]) 

    #flip sword overlay to be upside down. THIS NEEDS TO BE IMPROVED
    sword = sword.rotate(180)

    #randomly apply rotation to sword
    # angle = np.random.random_integers(-20,20)
    output = sword.rotate(40)

    #center the sword
    blank_image.paste(output, (int(int(width/2)-int(swordWidth/1.5)), 30), output)

    # makes white pixels transparent
    # new_image = Image.new("RGBA", img.size, "WHITE")
    return blank_image

def addFace(output_image, face, image_width):
    
    face_image = face.copy()
    fwidth, fheight = face_image.size
    resized = (int(fwidth*1.1), int(fheight*1.1))
    face_image = face_image.resize(resized, resample=0)

    face = face_image.convert("RGBA")
    face_data = face.getdata()

    newData = []
    for item in face_data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:  # finding black colour by its RGB value
            newData.append((0, 0, 0, 0))
        else : 
            newData.append((item[0], item[1], item[2]))
    face_image.putdata(newData)

    faceWidth = int(face_image.size[0])
    faceHeight =  int(face_image.size[1]) 
    #center the hat
    output_image.paste(face_image, (int(image_width/2 - faceWidth/2), 50), face_image)
    # makes white pixels transparent
    # new_image = Image.new("RGBA", img.size, "WHITE")
    return output_image

def addBackGround(blank_image, bgs, width, height):
    #overlay random sword onto character
    bg = random.choice(bgs)
    #resize sword to be same size as punk
    resized = (int(width), int(height))
    bg = bg.resize(resized, resample=0)

    #center the sword
    blank_image.paste(bg, (0,0), bg)

    # makes white pixels transparent
    # new_image = Image.new("RGBA", img.size, "WHITE")
    return blank_image

