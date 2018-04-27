import sys
import json

import requests

print("BM DMR Query Tool")

repeaterid = input("Repeater ID \n")

apiurl = "https://api.brandmeister.network/v1.0/repeater/?action=get&q=" + repeaterid
apireq = requests.get(apiurl)
apidata = json.loads(apireq.text)

print("Static talkgroups " + apidata['callsign'] + "(ID: " + repeaterid + ") :" )

apiurl = "https://api.brandmeister.network/v1.0/repeater/?action=profile&q=" + repeaterid
apireq = requests.get(apiurl)
apidata = json.loads(apireq.text)

for i in apidata['staticSubscriptions']:
    print("Talkgroup: " + str(i['talkgroup']) + " Timeslot: " + str(i['slot']) + " Type: " + str(i['type']) + " Networkid: " + str(i['networkid']) )
