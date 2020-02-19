

import requests
import xmltodict

from pyewts import pyewts
converter = pyewts()

def getMetadataDict(RID):
    bdrc_metadata_url = f'https://www.tbrc.org/xmldoc?rid={RID}'
    xml = requests.get(bdrc_metadata_url).content.decode('utf-8')
    metadataDict = xmltodict.parse(xml)
    return metadataDict

test = getMetadataDict('W23702')

volumeData = test['w:work']['w:volumeMap']['w:volume']

list = [[volumeData[x]['@imagegroup'],volumeData[x]['@num']] for x in range(len(volumeData))]

print(list)