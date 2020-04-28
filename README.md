<H1 align="center">Probe_Spider</h1><br>
<p align="center">
  <img src="https://img.shields.io/badge/build-passed-brightgreen" alt="build status">
  <img src="https://img.shields.io/badge/analyze-passed-rightgreen" alt="Analyze">
  <img src="https://img.shields.io/badge/tests-477%20passed%2C%202%20failed-red" alt="version">
  <img src="https://img.shields.io/badge/coverage-75%25-green" alt="Coverage"></br>
  <img src="https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen" alt="Test">
  <img src="https://img.shields.io/badge/python-v3.7-blue" alt="Python V3.7">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-up-brightgreen" alt="status-up">
</p>
This is an Open Source Intelligence Tool made completely in Python.<br>
<br><br>

**This tool has undergone massive improvement and was re-released as a separate tool here**

## [Recon Spider](https://github.com/bhavsec/reconspider)

<br><br>

## Overview: 

* Has a module for scraping account details from Instagram, Facebook, and Twitter.
* Phone Number Lookup for Carrier Details
* Search for E-Mails in Data Breaches
* Domain module has various vulnerability scanners and web crawlers
* Metadata Analyser
* Reverse Image Search 
* IP Heatmap generator
* MAC Address Lookup
* IP2Proxy checks if an IP is using a proxy or VPN and looks for DNS Leaks if they are
* Torrent Download History
* Tool is currently only available as a Command Line Interface (CLI) application

![Tool UI](https://drive.google.com/uc?export=view&id=1z-TiU5DHUTN6a69igDzDJPZFcPNOjphF)

**Creators:**  :bust_in_silhouette:
> [Aravindha Hariharan M](https://github.com/Aravindha1234u)  
  Mail ID: aravindha1234u@gmail.com

### Prerequisites  :package:
1.Python 3.X with pip3 Installed  
If not then, pip3 installation  
```
apt install python3-pip
```  
To Check pip versioon  
```
pip3 --version
```
2.Geolite & IP2Proxy Databases  
**Geolite2 City Database**
```
https://github.com/texnikru/GeoLite2-Database/blob/master/GeoLite2-City.mmdb.gz
```

**IP2Proxy Database**
```
https://lite.ip2location.com/database/px8-ip-proxytype-country-region-city-isp-domain-usagetype-asn-lastseen
```
Download both databases and move them to Probe_Spider/src/.

### Installation  :floppy_disk:
Open Terminal and type
```
git clone https://github.com/Aravindha1234u/Probe_Spider

cd Probe_Spider
```

To Install required Python packages

```
pip3 install -r requirements.txt
```
or
```
python3 -m pip install -r requirements.txt
```

### Execution  :+1:
**Before Executing, change the API keys in the src/api.py file or it will not work**  
To Run Probe_Spider
```
python3 main.py
```
In some cases you may also need to run it with elevated privileges, in which case type:
```
sudo python3 main.py
```
You also need to fetch the requirements again with elevated privileges as well by typing:
```
sudo pip3 install -r requirements
```

### Important Message  :warning:

>This tool is for research purposes only. Hence, the developers of this tool won't be responsible for any misuse of data collected using this tool. Used by many researchers and open source intelligence (OSINT) analysts.

### License  :page_facing_up:
Probe_Spider is licensed under GNU General Public License v3.0. Take a look at the [License](https://github.com/Aravindha1234u/Probe_Spider/blob/master/LICENSE)

## Special Thanks 
[Adithyan AK](https://github.com/adithyan-ak)  
[Gowtham G](https://github.com/Gowtham-18)

### Issues
Feel free to report any bugs or other issues you encounter with this program so we may fix them.<br>
<a href="https://github.com/Aravindha1234u/Probe_Spider/issues"><img src="https://img.shields.io/badge/issues-33-yellow" /></a>


# Some Screenshot of Tool

<img src="https://drive.google.com/uc?export=view&id=1ShK23Wp78pbz2VXt_E3LEHCipjcHSPzd" height="400" width="400" />  <img src="https://drive.google.com/uc?export=view&id=1BSZaFn95XMyVVtLio1lLPvvwX0pSsJGm" height="400" width="400" />  
<img src="https://drive.google.com/uc?export=view&id=1qjdoQzwwSn2yB-Ycn0mhYPKz9Ai-whgK" height="400" width="400" />  <img src="https://drive.google.com/uc?export=view&id=1wBX-yyxPT7IzzU52UOHuxq7fv68wrXve" height="400" width="400" />
<img src="https://drive.google.com/uc?export=view&id=14hx0GuYI23lztYv0uoRkUEcdsIWjSDtX" height="400" width="400" />
