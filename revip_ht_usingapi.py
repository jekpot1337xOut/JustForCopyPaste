from urllib import request
import time
import os
import requests
import concurrent.futures

red = "\033[91m"
la5dhar = "\033[92m"
rests = "\033[00m"
green = "\033[0;32m"
os.system("clear")
auth = """  ____  _            _      _____  _     _     _     
 |  _ \| |          | |    |  __ \| |   (_)   | |    
 | |_) | | __ _  ___| | __ | |__) | |__  _ ___| |__  
 |  _ <| |/ _` |/ __| |/ / |  ___/| '_ \| / __| '_ \ 
 | |_) | | (_| | (__|   <  | |    | | | | \__ \ | | |
 |____/|_|\__,_|\___|_|\_\ |_|    |_| |_|_|___/_| |_|
                       ______                        
                      |______|                      
        
    Name : Mass Reversip
    Team : Muslim Cyber Army-BD 
    Message: When TooL Stop, Change! \n	Your Vpn And Press Enter
                        """
headers = {
    "User-Agent": "Mozilla/6.0 (Macintosh; Intel Mac OS X 16_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}
apikey = "98218d4a307e53dd1683963230fa0c9e70af9afb06b0444d20affde92c04bd4c256085e186991e3b"
print(red + " Hello! Ripon. Welcome To")
time.sleep(2)
print(green + auth)
dorks = input(red + " [+] Enter Your IP's List: " + green)
try:
    dork = open(dorks, "r").readlines()
except:
    exit()
filename = input(red + " [+] Save Filename: " + green)"


def ck(dork):
    url = dork.strip()
    if "API count exceeded - Increase Quota with Membership" in url:
        input("Please Change Vpn And Press Enter: ")
    cp = (
        "cpanel." in url or "API count exceeded - Increase Quota with Membership" in url
    )
    mail = "mail." in url
    webdisk = (
        "webdisk." in url
        or "ns1." in url
        or "ns2." in url
        or "ns3." in url
        or "ns4." in url
        or "ns5" in url
        or "ns6" in url
        or "ns7" in url
        or "ns8" in url
        or "ns9" in url
        or "ns10" in url
    )
    webmail = "webmail." in url or "autodiscover." in url or "whm." in url or "<" in url
    if cp == True or mail == True or webdisk == True or webmail == True:
        pass
    else:
        print(green + " [+] Added: " + url)
        f = open(filename, "a")
        f.write(url + " \n")
        f.close()


def com(url):
    url = url.strip()
    try:
        file = open(filename, "r").read()
    except:
        open(filename, "w")
        file = open(filename, "r").read()
    if url in file:
        print(red + " [+] Already Exists: " + url)
    else:
        ck(url)


def auto(url):
    url = url.strip()
    data = request.Request("https://api.hackertarget.com/reverseiplookup/?q=" + url, apikey, headers=headers)
    data = request.urlopen(data, timeout=10)
    data = data.read().decode("utf-8")
    txt = data.splitlines()
    for okn in txt:
        com(okn)


try:
    with concurrent.futures.ThreadPoolExecutor(300) as executor:
        executor.map(auto, dork)
except:
    print(red + " [!] Connection Lost!")
print(green + "\n[+] All Site Grabbed Successful [+]")
