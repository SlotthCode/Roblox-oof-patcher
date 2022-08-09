import requests, os, shutil
from os import path
filename = "ouch.ogg"
def oof():
    session = requests.Session()
    #getting roblox verison
    robloxver = session.get("http://setup.roblox.com/version")
    robloxvers = robloxver.text
    p2 = path.expandvars(r'%LOCALAPPDATA%') 
    p2 = p2 + "/"
    p = os.path.join(p2, "Roblox", "Versions", robloxvers, "content", "sounds")
    p1 = os.path.join(p2, "Roblox", "Versions", robloxvers, "content", "sounds", "ouch.ogg")
    filepath = p
    if os.path.isfile(p1):
        os.remove(p1)
    else:
        print("file doesnt exist")
    shutil.copy("./ouch.ogg", p)
    print("Done made by Slotth, dm me on discord if you have any questions: Slotth#7496") 

oof()