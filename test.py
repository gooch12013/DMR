import requests
from QRZLookup import authKey


callsign = input("CallSign to look up? \n")

QRZ_URL ="http://xmldata.qrz.com/xml/current/?s="+ authKey + ";callsign=" + callsign

#print(QRZ_URL)

response = requests.get(QRZ_URL)
with open('qrz.xml', 'wb') as file:
    file.write(response.content)

from QRZ_Response import *
print(" ")
try:
    print(call)
except Exception:
    print("Not Listed")
try:
    print(fname+ " " + lname)
except Exception:
    print("Not Listed")
try:
    print(addr2)
except Exception:
    print("Not Listed")
try:
    print(state)
except Exception:
    print("Not Listed")
try:
    print(country)
except Exception:
    print("Not Listed")

