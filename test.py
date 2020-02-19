
def get_metadata(work_id):
    import requests
    import xml.etree.ElementTree as ET
    from pyewts import pyewts
    
    converter = pyewts()
    query_url = 'https://www.tbrc.org/xmldoc?rid={}'
    bdrc_metadata_url = query_url.format(work_id)
    r = requests.get(bdrc_metadata_url)
    root = ET.fromstring(r.content.decode('utf-8'))        
    title_tag = root[0]
    author_tag = root.find('{http://www.tbrc.org/models/work#}volumeMap')
    print(author_tag[0].attrib['imagegroup'])

    return metadata

m = get_metadata('W23703')
print(m)