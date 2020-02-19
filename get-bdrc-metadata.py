

import requests
import xmltodict

from pyewts import pyewts
converter = pyewts()

def getMetadataDict(RID):
    bdrc_metadata_url = f'https://www.tbrc.org/xmldoc?rid={RID}'
    xml = requests.get(bdrc_metadata_url).content.decode('utf-8')
    metadataDict = xmltodict.parse(xml, process_namespaces=False)
    # print(metadataDict)
    return metadataDict

test = getMetadataDict('W23702')

root = 'work'
child1 = 'volumeMap'
child2 = 'volume'

volumeData = test[f'w:{root}'][f'w:{child1}'][f'w:{child2}'][3]['@imagegroup']

print(volumeData)

# list = [[volumeData[x]['@imagegroup'],volumeData[x]['@num']] for x in range(len(volumeData))]

# print(list)

