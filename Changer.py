import requests
import os
from time import sleep
from colorama import Fore

ascii_art = r"""
  _   _ _______  __      _       _ _    ___       _     ____                       _ _         
 | | | |___ /\ \/ /_ __ | | ___ (_) |_ / _ \__  _/ |   / ___|  ___  ___ _   _ _ __(_) |_ _   _ 
 | |_| | |_ \ \  /| '_ \| |/ _ \| | __| | | \ \/ / |   \___ \ / _ \/ __| | | | '__| | __| | | |
 |  _  |___) |/  \| |_) | | (_) | | |_| |_| |>  <| |    ___) |  __/ (__| |_| | |  | | |_| |_| |
 |_| |_|____//_/\_\ .__/|_|\___/|_|\__|\___//_/\_\_|___|____/ \___|\___|\__,_|_|  |_|\__|\__, |
                  |_|                             |_____|                                |___/                               
"""

print(Fore.RED + ascii_art)
print(Fore.RED + "Telegram: H3Xploit0X1  ***  Github: H3Xploit0X1")
print(Fore.MAGENTA + "Change Your IP, Every Second,Every Minutes...")
print(Fore.CYAN + "Be Sure To Have Tor Running On Your System....")
print("")

def Mail():
    change = int(input(Fore.YELLOW + "After how many seconds do you want to change your IP? "))
    os.system("service tor start")
    url = "https://httpbin.org/ip"
    proxy = {'http':'socks5://127.0.0.1:9050',
             'https':'socks5://127.0.0.1:9050'}
    while True:
        request = requests.get(url, proxies=proxy)
        if request.status_code == 200:
            print(Fore.GREEN + "Your current IP: {}".format(request.json().get('origin')))
        else:
            print(Fore.MAGENTA + "Failed to get current IP")
        sleep(change)
        os.system("service tor reload")

if __name__ == "__main__":
    Mail()
