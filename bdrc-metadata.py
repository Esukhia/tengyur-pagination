import requests
import xmltodict

from pyewts import pyewts
converter = pyewts()

def getMetadataDict(RID):
    # returns metadata for an RID as an ordered dict
    bdrc_metadata_url = f'https://www.tbrc.org/xmldoc?rid={RID}'
    xml = requests.get(bdrc_metadata_url).content.decode('utf-8')
    metadataDict = xmltodict.parse(xml, process_namespaces=False)

    return metadataDict

def getVolumeMap(RID):
    # returns a volumeMap as ['imagegroup', volume]
    test = getMetadataDict(RID)
    root = 'work'
    child1 = 'volumeMap'
    child2 = 'volume'
    volume = test[f'w:{root}'][f'w:{child1}'][f'w:{child2}']
    # populate list
    volumeMap = [[volume[x]['@imagegroup'],int(volume[x]['@num'])] for x in range(len(volume))]

    return volumeMap

def getTitles(RID):
    # returns a volumeMap as ['name', 'language', 'encoding']
    test = getMetadataDict(RID)
    root = 'work'
    child1 = 'title'
    titles = test[f'w:{root}'][f'w:{child1}']
    # print(titles)
    # populate list
    titleList = [[titles[x]['#text'], titles[x]['@lang'], titles[x]['@encoding']] for x in range(len(titles))]

    return titleList
