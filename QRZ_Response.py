import os
import xml.etree.ElementTree as ET

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "qrz.xml")
#print('This is the full path: '+ xml_file)

tree = ET.parse(xml_file)
root = tree.getroot()
for child in root:
    #print(child)
    for element in child:
       # print(element.tag,)# ":", element.text)
        if element.tag == '{http://xmldata.qrz.com}fname':
           fname = element.text

        if element.tag == '{http://xmldata.qrz.com}name':
            lname= element.text
        if element.tag == '{http://xmldata.qrz.com}country':
            country= element.text
        if element.tag == '{http://xmldata.qrz.com}addr2':
            addr2 = element.text
        if element.tag == '{http://xmldata.qrz.com}state':
            state = element.text
        if element.tag == '{http://xmldata.qrz.com}call':
            call = element.text
        else:pass
#print(fname+ " " + lname)
