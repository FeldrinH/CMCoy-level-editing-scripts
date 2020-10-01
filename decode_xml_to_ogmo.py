import os
import xml.etree.ElementTree as ET

def decode_xml_to_ogmo():
    os.makedirs('levels', exist_ok=True)
    data = ET.parse('data.xml').getroot()

    for level in data.find('levels'):
        tiles = [row.split(',') for row in level.find('tileArray').text.split('|')]
        print(level.find('roomID').text)