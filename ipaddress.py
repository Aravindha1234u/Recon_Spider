import requests
import gmplot
from src.api import ipstack
import webbrowser
import re
from src.api import gmap
from ipaddress import *
from webosint.who.whois import *

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

api_key = ipstack()
if api_key == "":
    print("Add your ipstack api key to src/api.py")
    exit()

def IPHeatmap():
    print(C+'''Choose
    1) Trace single IP
    2) Trace multiple IPs''')
    choice = input(C+"root@osint:"+W+"~/IPaddress# ")

    if choice == '1':
        IP = input(C+"Enter the IP : "+W)
        read_single_IP(IP)
    elif choice == '2':
        IP_file = input(C+"Enter the IP File Location : "+W)
        read_multiple_IP(IP_file)
    else:
        print(R+"\nError: Please choose an appropriate option")

def read_single_IP(IP):
    print ( W + '[+]' + G + "Processing IP: %s ..." %IP + '\n')
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",IP):
        print("Invalid IP Address")
        IPHeatmap()
    lats = []
    lons = []
    r = requests.get("http://api.IPstack.com/" + IP + "?access_key=" + api_key)
    response = r.json()
    print('')
    print(C+"IP :"+W+response['ip'])
    print(C+"Location : " +W+ response['region_name'])
    print(C+"Country : " +W+response['country_name'])
    print(C+"Latitude :"+W+" {latitude}".format(**response))
    print(C+"Longitude :"+W+" {longitude}".format(**response))
    if input(C+"Want More Whois Details (Y/N): "+W):
        whois_more(IP)
    if response['latitude'] and response['longitude']:
        lats = response['latitude']
        lons = response['longitude']
    maps_url = "https://maps.google.com/maps?q=%s,+%s" % (lats, lons)
    print("")
    openWeb = input("Open GPS location in web broser? (Y/N) ")
    if openWeb.upper() == 'Y':
        webbrowser.open(maps_url, new=2)
    else:
        pass

def read_multiple_IP(IP_file):
    lats = []
    lons = []
    try:
        f = open(IP_file, "r")
        f1 = f.readlines()
        print ( W + '[+]' + G + "Processing....." + '\n')
        for line in f1:
            IP=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",line)
            IP=IP.group()
            r = requests.get("http://api.ipstack.com/" + IP + "?access_key=" + api_key)
            response = r.json()
            if response['latitude'] and response['longitude']:
                lats.append(response['latitude'])
                lons.append(response['longitude'])
        heat_map(lats,lons)
    except IOError:
        print(R+"ERROR : File Does not Exist\n")
        IPHeatmap()


def heat_map(lats,lons):
    gmap3 = gmplot.GoogleMapPlotter(20.5937, 78.9629, 5)
    gmap3.heatmap(lats,lons)
    gmap3.scatter(lats,lons, '#FF0000', size=50, marker=False)
    gmap3.plot(lats,lons, 'cornflowerblue', edge_width = 3.0)
    save_location = input(C+"Enter the location to save file : "+W)
    gmap3.apikey = gmap()
    location = save_location + "/heatmap.html"
    gmap3.draw(location)
    print(G+"Heatmap saved at " + location)
    openWeb = input(C+"Open Heatmap in web broser? (Y/N) : "+W)
    if openWeb.upper() == 'Y':
        webbrowser.open(url=("file:///"+location))
    else:
        pass
