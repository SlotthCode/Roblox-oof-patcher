import requests, os, shutil

filename = "ouch.ogg"
def oof():
    session = requests.Session()
    #getting roblox verison
    robloxver = session.get("http://setup.roblox.com/version")
    robloxvers = robloxver.text 
    r = os.path.join("C:/Program Files (x86)/Roblox/Versions/", robloxvers, "content", "sounds", "ouch.ogg")
    t =  os.path.join("C:/Program Files (x86)/Roblox/Versions/", robloxvers, "content", "sounds")
    print("Opened " + os.path.abspath(r) + " Now writing the oof sound")
    filepath = r
    if os.path.isfile(filepath):
        os.remove(filepath)
    else:
        print("File Doesn't exist!")
    shutil.copy("./ouch.ogg", t)
    print("Done! Made by Slotth")
oof()