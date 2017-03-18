import time
from datetime import datetime
import calendar
import requests
import urllib.request


ParsedData = requests.get('https://api.thingspeak.com/channels/176340/feeds.json?results=2').json()
a = ParsedData['feeds'][0]['created_at']
print("\n Original:\t"+str(a))

abc = a.rsplit('Z',1)[0]
print("\nSplitted:\t"+str(abc))

S = (calendar.timegm(datetime.strptime(abc, "%Y-%m-%dT%H:%M:%S").timetuple()))
print("\nValue in epoch:\t"+str(S))
print("\n")
print("Local Time:\t"+str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(S))))
