import os
import xml.etree.ElementTree as ET

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "data\\auth.xml")
#print('This is the full path: '+ xml_file)

tree = ET.parse(xml_file)
root = tree.getroot()

for child in root:
    #print(child)
    for element in child:
        #print(element.tag, ":", element.text)
        if element.tag == '{http://xmldata.qrz.com}Key':
            authKey = element.text
            #print(element.text)

