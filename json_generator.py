import json
import os
from datetime import date

path = 'C:/nft/outputDir/img'

files = os.listdir(path)

ipfs = 'QmVXVMJgyfAkErneZGnDUqzC6hGFctXJVrRETyaqRc3LUK'

for f in files:
    filename = f[:len(f)-4]
    if f[len(f)-3:] == 'png':
        print('num : ', filename)
        with open('outputDir/json/'+str(filename)+'.json', 'w', encoding='utf-8') as f:
            data = {
                "name":str(filename),
                "symbol": "NJA",
                'description': "Official Ninja",
                "image": "ipfs://"+ipfs+'/'+str(filename)+'.png',
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
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("The json file is created")