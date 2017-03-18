#This Program fetches data from thingspeak.com and sends it to initialstate.com
import time
from datetime import datetime
import calendar
import requests
import urllib.request               
from ISStreamer.Streamer import Streamer
from requests.exceptions import ConnectionError

streamer = Streamer(bucket_name="Bucket2", bucket_key="5MBXQ4JAAFFN", access_key="E8cDsPmXAKDHX32rHFDYYwCh94V5TbCW")

count = 0

#This is using 'requests', helps to parse json online
try:
    while(1):
        latest= requests.get('https://api.thingspeak.com/channels/<Channel Name>/feeds/last').json()
        ParsedData = requests.get('https://api.thingspeak.com/channels/<Channel Name>/feeds/last.json').json()
        #Syntax: print wjdata['data']['current_condition'][0]['temp_C']
        new= latest
        S = ParsedData
        a = new['created_at']
        abc = a.rsplit('Z',1)[0]
        temp = (calendar.timegm(datetime.strptime(abc, "%Y-%m-%dT%H:%M:%S").timetuple()))                  #Converted to Proper Epoch Time
        Fetch_Time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(temp))                          #Converted Epoch Time to IST
        print("\n Reading Number:\t"+str(count)+"\n")
        print("\nChannel Id:")
        print(S['channel']['id'])
        print("\nChannel Name:")
        print(S['channel']['name'])
        print("\n")
        print("\nEntry_Id:\n")
        print(new['entry_id'])
        print("\n")
        print("Last Update:\t"+str(Fetch_Time))
        print("\n")
        print(S['channel']['field1'])
        print(new['field1'])
        print(S['channel']['field2'])
        print(new['field2'])
        print(S['channel']['field3'])
        print(new['field3'])
        print(S['channel']['field4'])
        print(new['field4'])
        print(S['channel']['field5'])
        print(new['field5'])
        print(S['channel']['field6'])
        print(new['field6'])
        print(S['channel']['field7'])
        print(new['field7'])
        print(S['channel']['field8'])
        print(new['field8'])
        print("\n")
        streamer.log("Last Update", Fetch_Time)
        streamer.log("Entry_Id", new['entry_id'])
        streamer.log("Battery Temperature", new['field1'])
        streamer.log("Milk Temperature", new['field2'])
        streamer.log("Auxillary Temperature", new['field3'])
        streamer.log("Battery Voltage", new['field4'])
        streamer.log("AC Voltage", new['field5'])
        streamer.log("Compressor Current", new['field6'])
        streamer.log("Pump Current", new['field7'])
        streamer.log("Compressor Run Hr", new['field8'])
        streamer.close()
        count = count + 1
        time.sleep(50)
except ConnectionError as e:
    print (e)
except requests.exceptions.ConnectionError:
    r.status_code = "Connection refused by Thingspeak due to too much requests"
#End of Python Program
