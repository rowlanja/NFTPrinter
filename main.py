from color import readColor, offsetTransformation, randomizedTransformation, addColor, paletteTransformation, shiftTransformation
from overlay import preprocessOverlay, addHat, addPunk, addSword, addFace, addBackGround
import json
import os
from datetime import date
from PIL import Image
import random
import random

nftCount = 20

path = 'C:/nft/outputDir/img'

files = os.listdir(path)

ipfs = 'QmVXVMJgyfAkErneZGnDUqzC6hGFctXJVrRETyaqRc3LUK'

def generateJson():
    for f in files:
        for x in range(1,5):
            
            if f[len(f)-3:] == 'png':
                nftName = f[:len(f)-4]

                defense = random.randint(0,10)
                strength = random.randint(0,10)
                luck = random.randint(0,10)
                with open('outputDir/json/'+str(nftName)+'.'+str(x)+'.json', 'w', encoding='utf-8') as reader:
                    data = {
                        "name":str(nftName),
                        "symbol": "NJA",
                        'description': "Official Ninja",
                        "image": "ipfs://"+ipfs+'/'+str(nftName)+'.png',
                        "edition": 1,
                        "date":1632433142769,
                        'attributes' : [
                        {
                            'trait_type': 'eyes',
                            'value': 'red'
                        },
                        {
                            'trait_type': 'sheen',
                            'value': 'golden'
                        },
                        {
                            'trait_type': 'strength',
                            'value': str(strength*x)
                        },
                        {
                            'trait_type': 'defense',
                            'value': str(defense*x)
                        },
                        {
                            'trait_type': 'luck',
                            'value': str(luck*x)
                        }
                        ],
                        "collection":{
                            "name":"Ninja Solana family season 1",
                            "family":"Ninjas"
                        },
                        "properties":
                            {
                            "files": [
                                {
                                "uri":"image.png",
                                "type":"image/png"
                                }
                            ],
                        "category":"image",
                        "creators":[
                                {
                                "address":"ASpGfTcm8cyG7pmxAEF65nxoaZYmJkdzEwZ2zy4CnmsL",
                                "share":100
                                }
                            ]
                        }
                    }
                    json.dump(data, reader, ensure_ascii=False, indent=4)
                    print("The json file is created")

def main(): 
    # Import an image from directory:
    punk = Image.open("inputDir/body.png")

    face = Image.open("inputDir/face.png")

    # Extracting the width and height of the image:
    width, height = punk.size
    
    hats, hatNames = preprocessOverlay(width, height, 'inputDir/hats')
    swords, swordNames = preprocessOverlay(width, height, 'inputDir/swords')
    backgrounds, bgNames = preprocessOverlay(width, height, 'inputDir/backgrounds')

    # Create a randomised rgb transformation list
    colors = readColor(width, height, punk)
    transformations = offsetTransformation(colors, nftCount)
    # transformations = paletteTransformation()
    # transformations = shiftTransformation(colors, "color_shift.json")
    loop = 0
    for mint in range(len(transformations)):

        blank_image = Image.new('RGB', (width*2, height*2), (0,0,0))
        bwidth, bheight = blank_image.size

        output_image = punk.copy()
        rgba = output_image.convert("RGBA")
        punk_data = rgba.getdata()

        # Start layering overlays
        #overlay random sword onto character
        background = random.choice(backgrounds)
        #resize sword to be same size as punk
        resized = (int(bwidth), int(bheight))
        background = background.resize(resized, resample=0)

        addColor(transformations[mint], output_image, punk_data)

        addSword(background, swords, bwidth, bheight)

        addPunk(background, output_image, bwidth, bheight)
        
        addFace(background, face, bwidth)

        addHat(background, hats, hatNames, bwidth, bheight, transformations[mint])

        # Saving the final output
        filename = "outputDir/img/"+str(loop)+".png"
        background.save(filename, format="png")
        loop+=1
        print('minted : ', filename[10:])

# main()
generateJson()