import xml.etree.ElementTree as ET
import pyperclip

section = 'levels'
target = 'enemyArray'

root = ET.parse('cm2.xml').getroot()

outstr = ''
for world in root.find(section):
    elem = world.find(target)
    if elem.text != None:
        outstr += elem.text.replace('|', '\n').replace(',', '\t') + '\n'

pyperclip.copy(outstr)
print(target + " copied to clipboard")