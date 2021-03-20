import urllib
import urllib.request
import json
import sys
print("Ip Tracker by Mr. Zax")

p = print
  

#Open Site



def getinfo(trackip):
  print("\n[*] Finding, internet connection required")
  try:
    ur = urllib.request.urlopen(f"http://ip-api.com/json/{trackip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
  except:
    print("[!] Error")
    sys.exit()
  #Load Json from site
  js = json.load(ur)
  
  if js["status"] == "fail":
    print("[!] Error, Check again Your Input\n[!]"+jss["message"])
    print("[!] {js['query']}")
    input("Enter For Continue:")
    user()
  ##Parse Json
  p("Ip Address: "+js["query"])
  p("Continent : "+js["continent"])
  p("Continent Code: "+js["continentCode"])
  p("Country: "+js["country"])
  p("Country Code: "+js["countryCode"])
  p("Region: "+js["region"])
  p("Region Name: "+js["regionName"])
  p("City: "+js["city"])
  p("District: "+js["district"])
  p("Zip: "+str(js["zip"]))
  p("Lat: "+str(js["lat"]))
  p("Lon: "+str(js["lon"]))
  p("TimeZone: "+js["timezone"])
  p("Currency: "+js["currency"])
  p("ISP: "+js["isp"])
  p("Organization: "+js["org"])
  p("As: "+js["as"])
  p("As Name: "+js["asname"])
  p("Reverse: "+js["reverse"])
  p("Mobile: ",js["mobile"])
  p("Proxy: ",js["proxy"])
  p("Hosting: ",js["hosting"])
  p("\nProvided by")
  p("www.ip-api.com")
  input("Enter For Continue: ")
  user()
  

def user():
  while True:
    print("Ip Target")
    trackip = input(">> ")
    getinfo(trackip)
    
    
user()