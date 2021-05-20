from requests import get

import os

os.system("cls")

print("""
 ██████╗ ██╗  ██╗██████╗ ███████╗██╗   ██╗
██╔═████╗╚██╗██╔╝╚════██╗╚════██║██║   ██║
██║██╔██║ ╚███╔╝  █████╔╝    ██╔╝██║   ██║
████╔╝██║ ██╔██╗  ╚═══██╗   ██╔╝ ██║   ██║
╚██████╔╝██╔╝ ██╗██████╔╝   ██║  ╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═════╝ 
        Github : github.com/0x37U
""")

os.system("title [-] 0x37U IP Info [-]")

ip = input("0x37U@IP:~# ").strip()

def Getinfo(i):

    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    url = f"http://ip-api.com/json/{i}"
    
    infoReq = get(url,headers=head)

    js0n = infoReq.json()

    if "success" in infoReq.text:
        ipp = js0n["query"]
        city = js0n["city"]
        country = js0n["country"]
        Telecom = js0n["isp"]
        print(f"IP : {ipp}")
        print(f"Contry : {country}")
        print(f"City : {city}")
        print(f"Telecom Company Name : {Telecom}")
    else:
        print("Plese Try Another IP !")
Getinfo(ip)