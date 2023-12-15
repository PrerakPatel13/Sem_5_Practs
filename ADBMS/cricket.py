import xml.etree.ElementTree as et
import pandas as pd

name = []
ipl = []
description = []
p_id = []

tree = et.parse('cricket.xml')
root = tree.getroot()

for player in root.iter('player'):
    p_id.append(player.attrib['id'])
    name.append(player.find('name').text)
    ipl.append(player.find('ipl').text)
    description.append(player.find('description').text)

data = pd.DataFrame({'Jersey no': p_id, 'name': name, 'ipl': ipl, 'description': description})
print(data)
